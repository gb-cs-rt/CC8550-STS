
import asyncio, yaml, time
from pathlib import Path
from src.http_client import HttpLoadClient
from src.utils import write_csv, now_iso

async def main():
    cfg = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))
    base_url = cfg["base_url"]
    path = cfg["endpoint_path"]
    window = int(cfg.get("rate_limit_window_s", 60))
    limit = int(cfg.get("rate_limit_max_per_ip", 100))

    client = HttpLoadClient(base_url, timeout_ms=int(cfg.get("timeout_ms", 3000)))

    total = limit + 30
    start = time.perf_counter()
    results = await client.get_many(path, n=total, concurrency=50)
    elapsed = time.perf_counter() - start

    too_many = sum(1 for _, st in results if st == 429)
    ok = sum(1 for _, st in results if st < 400)

    rows = [{
        "ts": now_iso(),
        "test": "security_rate_limit",
        "window_s": window,
        "limit_per_ip": limit,
        "sent": total,
        "ok": ok,
        "http_429": too_many,
        "elapsed_s": round(elapsed, 2)
    }]
    write_csv("results/security_rate_limit.csv", rows, ["ts","test","window_s","limit_per_ip","sent","ok","http_429","elapsed_s"])
    print("[security] results saved to results/security_rate_limit.csv")

if __name__ == "__main__":
    asyncio.run(main())
