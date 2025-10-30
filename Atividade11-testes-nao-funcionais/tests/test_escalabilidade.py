import pytest

from ecommerce import EcommerceSimulator, calculate_horizontal_scaling_efficiency


@pytest.fixture(scope="module")
def scaling_results():
    simulator = EcommerceSimulator(random_seed=7, baseline_capacity=4000)
    stages = simulator.simulate_scaling(
        server_counts=[1, 2, 4, 8],
        baseline_users=4000,
        duration_s=60,
    )
    return stages


def test_horizontal_efficiency_above_threshold(scaling_results):
    baseline_throughput = scaling_results[1].throughput_rps
    expected = [(servers, baseline_throughput * servers) for servers in scaling_results]
    actual = [(servers, stage.throughput_rps) for servers, stage in scaling_results.items()]
    efficiency = calculate_horizontal_scaling_efficiency(expected, actual)
    for servers, eff in efficiency.items():
        assert eff >= 80.0, f"Eficiência horizontal {eff:.2f}% abaixo do limite para {servers} nós"


def test_throughput_scales_with_servers(scaling_results):
    throughputs = [stage.throughput_rps for _, stage in sorted(scaling_results.items())]
    assert throughputs == sorted(
        throughputs
    ), "Throughput não cresce conforme adicionamos servidores"
