
import asyncio, yaml, time
from pathlib import Path
from src.http_client import HttpLoadClient
from src.utils import write_csv, now_iso

async def main():
    cfg = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))
    base_url = cfg["base_url"]
    path = cfg["endpoint_path"]
    duration = int(cfg.get("duration_s", 60))
    conc = int(cfg.get("concurrency", 200))

    client = HttpLoadClient(base_url, timeout_ms=int(cfg.get("timeout_ms", 3000)))

    t0 = time.perf_counter()
    results = await client.hammer_for(path, seconds=duration, concurrency=conc)
    elapsed = time.perf_counter() - t0
    ok = sum(1 for _, st in results if st < 500)
    rps = ok / elapsed if elapsed > 0 else 0.0

    rows = [{
        "ts": now_iso(),
        "test": "load_throughput",
        "duration_s": duration,
        "concurrency": conc,
        "requests_ok": ok,
        "rps_ok": round(rps, 2)
    }]
    write_csv("results/load_throughput.csv", rows, ["ts","test","duration_s","concurrency","requests_ok","rps_ok"])
    print(f"[load] sustained throughput={rps:.2f} req/s (saved: results/load_throughput.csv)")

if __name__ == "__main__":
    asyncio.run(main())
