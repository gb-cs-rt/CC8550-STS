
import asyncio, yaml, os
from pathlib import Path
from src.http_client import HttpLoadClient
from src.utils import percentile, write_csv, now_iso

async def main():
    cfg = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))
    base_url = cfg["base_url"]
    path = cfg["endpoint_path"]
    conc = int(cfg.get("concurrency", 200))

    client = HttpLoadClient(base_url, timeout_ms=int(cfg.get("timeout_ms", 3000)))
    n = int(os.getenv("REQS", "5000"))
    results = await client.get_many(path, n=n, concurrency=conc)

    latencies = [ms for ms, st in results if st < 500]
    p95 = percentile(latencies, 95) if latencies else float("nan")
    errors = sum(1 for _, st in results if st >= 500)

    rows = [{
        "ts": now_iso(),
        "test": "performance_p95",
        "n": n,
        "concurrency": conc,
        "latency_p95_ms": round(p95, 2) if p95 == p95 else "",
        "errors": errors
    }]
    write_csv("results/performance_p95.csv", rows, ["ts","test","n","concurrency","latency_p95_ms","errors"])
    print(f"[performance] P95={p95:.2f} ms, errors={errors}/{len(results)} (saved: results/performance_p95.csv)")

if __name__ == "__main__":
    asyncio.run(main())
