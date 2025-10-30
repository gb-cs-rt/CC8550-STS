
import asyncio, yaml, time
from pathlib import Path
from src.http_client import HttpLoadClient
from src.utils import write_csv, now_iso

async def measure_rps(client, path, duration_s: int, concurrency: int) -> float:
    t0 = time.perf_counter()
    results = await client.hammer_for(path, seconds=duration_s, concurrency=concurrency)
    elapsed = time.perf_counter() - t0
    ok = sum(1 for _, st in results if st < 500)
    return ok / elapsed if elapsed > 0 else 0.0

async def main():
    cfg = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))
    base_url = cfg["base_url"]
    path = cfg["endpoint_path"]
    duration = int(cfg.get("duration_s", 60))
    instances_list = cfg.get("scalability_instances", [1,2,4,8])

    base_conc = int(cfg.get("concurrency", 200))
    client = HttpLoadClient(base_url, timeout_ms=int(cfg.get("timeout_ms", 3000)))

    results = []
    rps1 = None
    for n in instances_list:
        conc = base_conc * n
        rps = await measure_rps(client, path, duration, conc)
        if n == 1:
            rps1 = rps
        efficiency = (rps / (rps1 * n) * 100.0) if (rps1 and rps1 > 0) else 0.0
        results.append({
            "ts": now_iso(),
            "test": "scalability_efficiency",
            "instances": n,
            "concurrency": conc,
            "rps_ok": round(rps, 2),
            "efficiency_pct": round(efficiency, 2)
        })

    write_csv("results/scalability_efficiency.csv", results, ["ts","test","instances","concurrency","rps_ok","efficiency_pct"])
    print("[scalability] results saved to results/scalability_efficiency.csv")

if __name__ == "__main__":
    asyncio.run(main())
