from __future__ import annotations

import math
import random
import statistics
from collections import Counter, deque
from dataclasses import dataclass, field
from typing import Deque, Dict, Iterable, List, Optional, Sequence, Tuple


def percentile(values: Sequence[float], pct: float) -> float:
    """Return the percentile value for a sorted sequence."""
    if not values:
        raise ValueError("percentile requires a non-empty sequence")
    if pct <= 0:
        return float(values[0])
    if pct >= 100:
        return float(values[-1])
    rank = (pct / 100) * (len(values) - 1)
    lower = math.floor(rank)
    upper = math.ceil(rank)
    weight = rank - lower
    if lower == upper:
        return float(values[int(rank)])
    return float(values[lower] * (1 - weight) + values[upper] * weight)


def calculate_latency_stats(
    latencies_ms: Sequence[float], percentiles: Sequence[float] = (50, 90, 95, 99)
) -> Dict[str, float]:
    """
    Compute summary statistics for latency samples.

    Returns a dictionary with average, min, max, standard deviation and requested percentiles.
    """
    if not latencies_ms:
        raise ValueError("latency stats require at least one latency sample")
    ordered = sorted(latencies_ms)
    stats: Dict[str, float] = {
        "avg_ms": float(statistics.fmean(ordered)),
        "min_ms": float(ordered[0]),
        "max_ms": float(ordered[-1]),
    }
    if len(ordered) > 1:
        stats["stdev_ms"] = float(statistics.stdev(ordered))
    for pct in percentiles:
        stats[f"p{int(pct)}_ms"] = percentile(ordered, pct)
    return stats


def calculate_throughput(total_requests: int, duration_s: float) -> float:
    """Compute throughput (req/s) given total requests and elapsed seconds."""
    if duration_s <= 0:
        raise ValueError("duration must be positive")
    if total_requests < 0:
        raise ValueError("total_requests cannot be negative")
    return total_requests / duration_s


def calculate_horizontal_scaling_efficiency(
    expected_throughput: Sequence[Tuple[int, float]],
    actual_throughput: Sequence[Tuple[int, float]],
) -> Dict[int, float]:
    """
    Calculate horizontal scaling efficiency per server count.

    expected_throughput: ideal throughput per (servers, req/s)
    actual_throughput: measured throughput per (servers, req/s)
    Returns mapping server_count -> efficiency (0-100%).
    """
    expected = {servers: thr for servers, thr in expected_throughput}
    efficiency: Dict[int, float] = {}
    for servers, real_thr in actual_throughput:
        ideal = expected.get(servers)
        if ideal is None or ideal <= 0:
            continue
        efficiency[servers] = (real_thr / ideal) * 100
    return efficiency


def enforce_rate_limit(
    timestamps_s: Sequence[float], limit_per_minute: int, burst: int = 0
) -> Tuple[List[float], List[float]]:
    """
    Enforce a fixed-window rate limit.

    Returns allowed and blocked timestamps based on the provided limit and burst allowance.
    """
    if limit_per_minute <= 0:
        raise ValueError("limit_per_minute must be positive")
    window_seconds = 60.0
    allowed: List[float] = []
    blocked: List[float] = []
    queue: Deque[float] = deque()
    capacity = limit_per_minute + max(0, burst)
    for ts in sorted(timestamps_s):
        while queue and ts - queue[0] >= window_seconds:
            queue.popleft()
        if len(queue) < capacity:
            allowed.append(ts)
            queue.append(ts)
        else:
            blocked.append(ts)
    return allowed, blocked


@dataclass
class StageResult:
    """Stores aggregated metrics for a single simulation stage."""

    name: str
    users: int
    duration_s: float
    total_requests: int
    errors: int
    latencies_ms: List[float] = field(default_factory=list)

    @property
    def throughput_rps(self) -> float:
        return calculate_throughput(self.total_requests, self.duration_s)

    @property
    def error_rate(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return (self.errors / self.total_requests) * 100

    def latency_summary(self) -> Dict[str, float]:
        if not self.latencies_ms:
            return {}
        return calculate_latency_stats(self.latencies_ms)


@dataclass
class StressTestResult:
    """Records the progression of a stress test until failure."""

    stages: List[StageResult]
    breakpoint_users: Optional[int]
    reason: Optional[str]


@dataclass
class RateLimitResult:
    """Summarises rate limiting behaviour across simulated requests."""

    limit_per_minute: int
    burst: int
    total_requests: int
    allowed: int
    blocked: int
    blockage_ratio: float


class EcommerceSimulator:
    """
    Simplified e-commerce simulator focused on non-functional testing scenarios.

    The simulator generates synthetic metrics using mock catalogue data and probabilistic user flows.
    """

    ACTION_LATENCIES_MS: Dict[str, Tuple[int, int]] = {
        "browse_catalog": (110, 220),
        "view_product": (180, 320),
        "search_product": (200, 340),
        "add_to_cart": (240, 380),
        "checkout": (320, 520),
        "confirm_payment": (380, 640),
    }

    ACTION_WEIGHTS: Dict[str, int] = {
        "browse_catalog": 25,
        "view_product": 30,
        "search_product": 20,
        "add_to_cart": 15,
        "checkout": 7,
        "confirm_payment": 3,
    }

    CATALOG: List[Dict[str, object]] = [
        {"sku": "SKU-001", "name": "Smartphone X", "price": 2499.90},
        {"sku": "SKU-002", "name": "Notebook Pro", "price": 5999.00},
        {"sku": "SKU-003", "name": "Fone Bluetooth", "price": 399.99},
        {"sku": "SKU-004", "name": "Teclado Mecânico", "price": 699.50},
        {"sku": "SKU-005", "name": "Monitor 27\"", "price": 1899.00},
    ]

    def __init__(self, random_seed: Optional[int] = None, baseline_capacity: int = 2000):
        self.random = random.Random(random_seed)
        self.baseline_capacity = max(100, baseline_capacity)

    def simulate_stage(
        self,
        users: int,
        duration_s: float,
        name: str = "stage",
        jitter: float = 0.35,
        base_error_rate: float = 0.8,
    ) -> StageResult:
        """
        Simulate a stage with a fixed number of concurrent users.

        jitter defines variability applied to latency based on system strain.
        base_error_rate is expressed as percentage of errors at baseline capacity.
        """
        if users <= 0:
            raise ValueError("users must be positive")
        if duration_s <= 0:
            raise ValueError("duration_s must be positive")

        strain = users / self.baseline_capacity
        latency_multiplier = 1 + max(0, strain - 1) * jitter * 2
        progressive_error = (base_error_rate / 100) * max(1, strain**1.4)

        total_requests = 0
        errors = 0
        latencies: List[float] = []

        for _ in range(users):
            planned_actions = self.random.randint(3, 8)
            actions = self.random.choices(
                population=list(self.ACTION_LATENCIES_MS.keys()),
                weights=[self.ACTION_WEIGHTS[a] for a in self.ACTION_LATENCIES_MS],
                k=planned_actions,
            )
            for action in actions:
                base_low, base_high = self.ACTION_LATENCIES_MS[action]
                latency = self.random.uniform(base_low, base_high) * latency_multiplier
                if self.random.random() < progressive_error:
                    errors += 1
                else:
                    latencies.append(latency)
                total_requests += 1

        return StageResult(
            name=name,
            users=users,
            duration_s=duration_s,
            total_requests=total_requests,
            errors=errors,
            latencies_ms=latencies,
        )

    def simulate_load_curve(
        self,
        stages: Sequence[Tuple[str, int, float]],
        jitter: float = 0.35,
        base_error_rate: float = 0.8,
    ) -> List[StageResult]:
        """
        Simulate multiple stages emulating a load curve (baseline, ramp-up, pico).

        stages: iterable of tuples (name, users, duration_seconds).
        """
        results: List[StageResult] = []
        for name, users, duration in stages:
            results.append(
                self.simulate_stage(
                    name=name,
                    users=users,
                    duration_s=duration,
                    jitter=jitter,
                    base_error_rate=base_error_rate,
                )
            )
        return results

    def simulate_stress_test(
        self,
        start_users: int,
        max_users: int,
        step: int,
        duration_s: float,
        tolerated_error_pct: float = 5.0,
    ) -> StressTestResult:
        """
        Run a stress test increasing users until reaching error threshold.
        """
        if start_users <= 0 or max_users <= 0 or step <= 0:
            raise ValueError("start_users, max_users and step must be positive")
        stages: List[StageResult] = []
        breakpoint_users: Optional[int] = None
        reason: Optional[str] = None

        users = start_users
        while users <= max_users:
            stage_name = f"stress_{users}"
            result = self.simulate_stage(
                name=stage_name,
                users=users,
                duration_s=duration_s,
                jitter=0.45,
                base_error_rate=1.0,
            )
            stages.append(result)
            if result.error_rate >= tolerated_error_pct or not result.latencies_ms:
                breakpoint_users = users
                reason = (
                    f"error_rate {result.error_rate:.2f}% >= {tolerated_error_pct:.2f}%"
                )
                break
            users += step

        return StressTestResult(stages=stages, breakpoint_users=breakpoint_users, reason=reason)

    def simulate_scaling(
        self,
        server_counts: Sequence[int],
        baseline_users: int,
        duration_s: float,
    ) -> Dict[int, StageResult]:
        """
        Simulate horizontal scaling by distributing users across server counts.
        """
        if baseline_users <= 0:
            raise ValueError("baseline_users must be positive")
        results: Dict[int, StageResult] = {}
        base_users_per_server = max(1, baseline_users // max(server_counts))
        for servers in server_counts:
            users = base_users_per_server * servers
            stage = self.simulate_stage(
                name=f"scale_{servers}",
                users=users,
                duration_s=duration_s,
                jitter=0.30,
                base_error_rate=0.6,
            )
            results[servers] = stage
        return results

    def simulate_rate_limiting(
        self,
        users: int,
        duration_s: float,
        limit_per_minute: int,
        burst: int = 0,
    ) -> RateLimitResult:
        """
        Simulate rate limiting under concurrent usage.

        Generates random timestamps for user requests and enforces the provided limit.
        """
        if users <= 0:
            raise ValueError("users must be positive")
        if duration_s <= 0:
            raise ValueError("duration_s must be positive")
        timestamps: List[float] = []
        for _ in range(users):
            requests = self.random.randint(10, 60)
            for _ in range(requests):
                timestamps.append(self.random.uniform(0, duration_s))
        allowed, blocked = enforce_rate_limit(timestamps, limit_per_minute, burst=burst)
        total = len(timestamps)
        blocked_ratio = (len(blocked) / total) * 100 if total else 0.0
        return RateLimitResult(
            limit_per_minute=limit_per_minute,
            burst=burst,
            total_requests=total,
            allowed=len(allowed),
            blocked=len(blocked),
            blockage_ratio=blocked_ratio,
        )

    def session_value_distribution(self, stage: StageResult) -> Counter:
        """
        Generate mock revenue distribution for a stage based on completed actions.

        Useful to correlate performance behaviour with business impact.
        """
        completed_sessions = stage.total_requests - stage.errors
        values: Counter = Counter()
        for _ in range(max(0, completed_sessions // 6)):
            product = self.random.choice(self.CATALOG)
            ticket = product["price"] * self.random.uniform(0.8, 1.2)
            bucket = round(ticket, -1)
            values[bucket] += 1
        return values
