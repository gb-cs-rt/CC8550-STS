from math import ceil

import pytest

from ecommerce import EcommerceSimulator

DURATION_S = 180
LIMIT_PER_MINUTE = 100


@pytest.fixture(scope="module")
def rate_limiting_result():
    simulator = EcommerceSimulator(random_seed=321)
    result = simulator.simulate_rate_limiting(
        users=200,
        duration_s=DURATION_S,
        limit_per_minute=LIMIT_PER_MINUTE,
        burst=0,
    )
    status = "APROVADO" if result.allowed <= LIMIT_PER_MINUTE * ceil(DURATION_S / 60) else "RECUSADO"
    print("\n[Segurança] Métrica: Rate limiting | Meta: 100 req/min/IP")
    print(
        f"  Permitidas: {result.allowed}, Bloqueadas: {result.blocked} "
        f"({result.blockage_ratio:.2f}%) -> Status: {status}"
    )
    return result


def test_rate_limit_respects_cap(rate_limiting_result):
    expected_cap = rate_limiting_result.limit_per_minute * ceil(DURATION_S / 60)
    assert (
        rate_limiting_result.allowed <= expected_cap
    ), "Rate limiting permitiu mais requisições do que o limite configurado"


def test_rate_limit_blocks_excess(rate_limiting_result):
    assert rate_limiting_result.blocked > 0, "Nenhuma requisição foi bloqueada"
    assert (
        rate_limiting_result.blockage_ratio > 50.0
    ), "Percentual de requisições bloqueadas não reflete o limite imposto"


def test_rate_limit_reports_configuration(rate_limiting_result):
    assert (
        rate_limiting_result.limit_per_minute == LIMIT_PER_MINUTE
    ), "Configuração de rate limiting divergente do esperado"
