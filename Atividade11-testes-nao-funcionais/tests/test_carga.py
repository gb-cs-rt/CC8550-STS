import pytest

from ecommerce import EcommerceSimulator


@pytest.fixture(scope="module")
def load_result():
    simulator = EcommerceSimulator(random_seed=202, baseline_capacity=50000)
    stage = simulator.simulate_stage(
        name="black_friday_sustained",
        users=50000,
        duration_s=120,
        jitter=0.25,
        base_error_rate=0.5,
    )
    latency = stage.latency_summary()
    status = "APROVADO" if stage.throughput_rps > 2000 else "RECUSADO"
    print("\n[Carga] Métrica: Throughput sustentado | Meta: > 2000 req/s")
    print(
        f"  Resultado: {stage.throughput_rps:.1f} req/s, "
        f"Erros={stage.error_rate:.2f}%, P95={latency['p95_ms']:.1f}ms -> "
        f"Status: {status}"
    )
    return stage


def test_throughput_exceeds_target(load_result):
    assert (
        load_result.throughput_rps > 2000
    ), f"Throughput sustentado abaixo da meta: {load_result.throughput_rps:.1f} req/s"


def test_error_rate_remains_controlled(load_result):
    assert (
        load_result.error_rate < 2.0
    ), f"Taxa de erro elevada sob carga sustentada: {load_result.error_rate:.2f}%"


def test_latency_p95_stays_under_threshold(load_result):
    p95_latency = load_result.latency_summary()["p95_ms"]
    assert p95_latency < 500, f"P95 excede limite durante carga: {p95_latency:.2f}ms"
