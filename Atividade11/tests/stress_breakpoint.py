
import asyncio, yaml
from pathlib import Path
from src.http_client import HttpLoadClient
from src.utils import write_csv, now_iso, percentile

async def run_step(client, path, users, hold_s):
    results = await client.hammer_for(path, seconds=hold_s, concurrency=users)
    latencies = [ms for ms, st in results if st < 500]
    p95 = percentile(latencies, 95) if latencies else float("inf")
    err = sum(1 for _, st in results if st >= 500)
    return p95, err, len(results)

async def main():
    cfg = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))
    base_url = cfg["base_url"]
    path = cfg["endpoint_path"]
    steps = cfg["ramp_steps"]
    client = HttpLoadClient(base_url, timeout_ms=int(cfg.get("timeout_ms", 3000)))
    target_p95 = int(cfg["targets"]["perf_p95_ms"])

    breakpoint_users = None
    rows = []
    for step in steps:
        users, hold_s = int(step["users"]), int(step["hold_s"])
        p95, err, total = await run_step(client, path, users, hold_s)
        rows.append({
            "ts": now_iso(),
            "test": "stress_breakpoint",
            "users": users,
            "hold_s": hold_s,
            "p95_ms": round(p95, 2) if p95 == p95 else "",
            "errors": err,
            "total": total
        })
        if p95 > target_p95 * 2 or err / max(1,total) > 0.05:
            breakpoint_users = users
            break

    write_csv("results/stress_breakpoint.csv", rows, ["ts","test","users","hold_s","p95_ms","errors","total"])
    if breakpoint_users:
        print(f"[stress] breakpoint ~ {breakpoint_users} users (saved: results/stress_breakpoint.csv)")
    else:
        print("[stress] breakpoint not reached within configured steps (saved: results/stress_breakpoint.csv)")

if __name__ == "__main__":
    asyncio.run(main())
