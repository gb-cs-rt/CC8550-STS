
import asyncio, aiohttp, time
from typing import List, Tuple

class HttpLoadClient:
    def __init__(self, base_url: str, timeout_ms: int = 3000):
        self.base_url = base_url.rstrip("/")
        self.timeout = aiohttp.ClientTimeout(total=timeout_ms/1000.0)

    async def get_many(self, path: str, n: int, concurrency: int = 50) -> List[Tuple[float, int]]:
        sem = asyncio.Semaphore(concurrency)
        results: List[Tuple[float, int]] = []

        async def one():
            async with sem:
                t0 = time.perf_counter()
                try:
                    async with aiohttp.ClientSession(timeout=self.timeout) as sess:
                        async with sess.get(self.base_url + path) as resp:
                            await resp.read()
                            dt = (time.perf_counter() - t0) * 1000.0
                            results.append((dt, resp.status))
                except Exception:
                    dt = (time.perf_counter() - t0) * 1000.0
                    results.append((dt, 599))
        tasks = [asyncio.create_task(one()) for _ in range(n)]
        await asyncio.gather(*tasks)
        return results

    async def hammer_for(self, path: str, seconds: int, concurrency: int = 100) -> List[Tuple[float, int]]:
        results: List[Tuple[float, int]] = []
        stop_at = asyncio.get_event_loop().time() + seconds
        sem = asyncio.Semaphore(concurrency)

        async def worker():
            nonlocal results
            while asyncio.get_event_loop().time() < stop_at:
                async with sem:
                    t0 = time.perf_counter()
                    try:
                        async with aiohttp.ClientSession(timeout=self.timeout) as sess:
                            async with sess.get(self.base_url + path) as resp:
                                await resp.read()
                                dt = (time.perf_counter() - t0) * 1000.0
                                results.append((dt, resp.status))
                    except Exception:
                        dt = (time.perf_counter() - t0) * 1000.0
                        results.append((dt, 599))
        workers = [asyncio.create_task(worker()) for _ in range(concurrency)]
        await asyncio.gather(*workers, return_exceptions=True)
        return results
