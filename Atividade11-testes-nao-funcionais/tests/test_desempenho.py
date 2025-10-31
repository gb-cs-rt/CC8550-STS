import pytest

from ecommerce import EcommerceSimulator


@pytest.fixture(scope="module")
def performance_results():
    simulator = EcommerceSimulator(random_seed=123, baseline_capacity=10000)
    stages = [
        ("baseline", 3000, 60),
        ("ramp_up", 6000, 90),
        ("peak", 10000, 120),
    ]
    results = simulator.simulate_load_curve(stages)
    stage_map = {stage.name: stage for stage in results}
    print("\n[Desempenho] Métrica: Tempo de resposta P95 | Meta: < 500ms")
    for name in ("baseline", "ramp_up", "peak"):
        stage = stage_map[name]
        latencies = stage.latency_summary()
        p95 = latencies["p95_ms"]
        status = "APROVADO" if p95 < 500 else "RECUSADO"
        print(
            f"  - {name}: P95={p95:.1f}ms, Média={latencies['avg_ms']:.1f}ms, "
            f"P99={latencies['p99_ms']:.1f}ms -> Status: {status}"
        )
    return stage_map


def test_p95_latency_within_target(performance_results):
    peak = performance_results["peak"]
    p95_latency = peak.latency_summary()["p95_ms"]
    assert p95_latency < 500, f"P95 acima do limite: {p95_latency:.2f}ms"


def test_error_rate_stays_below_one_percent(performance_results):
    peak = performance_results["peak"]
    assert peak.error_rate < 1.0, f"Taxa de erro elevada: {peak.error_rate:.2f}%"


def test_throughput_meets_baseline_expectation(performance_results):
    baseline = performance_results["baseline"]
    assert baseline.throughput_rps > 150, "Throughput baixo na carga de referência"
