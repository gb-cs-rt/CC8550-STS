import pytest

from ecommerce import EcommerceSimulator


@pytest.fixture(scope="module")
def stress_result():
    simulator = EcommerceSimulator(random_seed=42, baseline_capacity=15000)
    return simulator.simulate_stress_test(
        start_users=8000,
        max_users=60000,
        step=2000,
        duration_s=60,
        tolerated_error_pct=5.0,
    )


def test_breakpoint_exceeds_target(stress_result):
    assert (
        stress_result.breakpoint_users
        and stress_result.breakpoint_users >= 15000
    ), f"Ponto de quebra abaixo da meta: {stress_result.breakpoint_users}"


def test_reason_reports_error_threshold(stress_result):
    assert (
        stress_result.reason is not None
    ), "Ponto de quebra não apresentou justificativa"
    assert "error_rate" in stress_result.reason


def test_throughput_increases_with_load(stress_result):
    throughputs = [stage.throughput_rps for stage in stress_result.stages]
    assert throughputs == sorted(
        throughputs
    ), "Throughput não aumenta conforme a carga progride"
