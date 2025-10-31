# Atividade 11 - Testes não funcionais: desempenho, carga, estresse, escalabilidade e segurança

## Membros do Grupo:
- Felipe Orlando Lanzara - 22.225.015-1
- Pedro Henrique Lega Kramer Costa - 22.125.091-3
- Ruan Pastrelo Turola - 22.225.013-6

## Resumo do Enunciado — Teste Integrado de E-commerce (Black Friday)

### Cenário
Desenvolver um **plano de testes não funcionais** para um sistema de e-commerce que será lançado na **Black Friday**, cobrindo ao menos **uma métrica por tipo de teste**.

### Requisitos do Sistema
- **Escala:** ~10.000 usuários simultâneos no pico.
- **Desempenho:** tempo de resposta **P95 < 500 ms**.
- **Confiabilidade:** **99,9%** de disponibilidade durante o evento.
- **Segurança:** proteção contra ataques e vazamento de dados.

### Tipos de Teste e Metas

| Tipo de teste  | Métrica obrigatória       | Meta definida           |
|----------------|---------------------------|-------------------------|
| Desempenho     | Tempo de resposta **P95** | **< 500 ms**            |
| Carga          | **Throughput sustentado** | **> 2000 req/s**        |
| Estresse       | **Ponto de quebra**       | **> 15.000 usuários**   |
| Escalabilidade | **Eficiência horizontal** | **> 80%**               |
| Segurança      | **Rate limiting**         | **100 req/min/IP**      |

### Entregáveis
- Exemplos de **testes em Python** para cada tipo.
- **Métricas coletadas** para cada meta.
- **Relatório** com análise e **aprovação/reprovação** das metas.

## Simulador principal

Arquivo **`ecommerce.py`** define a classe **`EcommerceSimulator`**, responsável por gerar **latência sintética**, **throughput**, **erros progressivos** e **efeitos de sobrecarga**.

**Métodos principais**
- `simulate_stage(users, duration_s, name, jitter, base_error_rate)` — retorna métricas de um estágio (latências, erros e **throughput req/s**).  
- `simulate_load_curve(stages)` — calcula **throughput** e latências em **baseline → ramp_up → peak**.  
- `simulate_stress_test(start_users, max_users, step, duration_s, tolerated_error_pct)` — retorna o **primeiro** volume de usuários com violação (ex.: **erro ≥ 5%**).  
- `simulate_scaling(server_counts, baseline_users, duration_s)` — estima o ganho de **throughput por instância** após **scale-out** e permite calcular a **eficiência horizontal**.  
- `simulate_rate_limiting(users, duration_s, limit_per_minute, burst)` — aplica **rate limit** de *X req/min* e consolida **permitidos x bloqueados**.

**Funções auxiliares**
- `percentile` • `calculate_latency_stats` • `calculate_throughput` •  
  `calculate_horizontal_scaling_efficiency` • `enforce_rate_limit`  
- *Dataclasses* para consolidar métricas: `StageResult`, `StressTestResult`, `RateLimitResult`.

---

## Testes automatizados (pytest)

### `tests/test_desempenho.py`
```python
from ecommerce import EcommerceSimulator

def test_p95_menor_500ms_em_todas_as_fases():
    sim = EcommerceSimulator(random_seed=42, baseline_capacity=2000)
    fases = [
        ("baseline", 200, 60),
        ("ramp_up", 800, 60),
        ("peak", 1600, 60),
    ]
    for nome, users, dur in fases:
        s = sim.simulate_stage(users=users, duration_s=dur, name=nome)
        p95 = s.latency_summary()["p95_ms"]
        print(f"[Desempenho] {nome}: P95={p95:.1f}ms, Média={s.latency_summary()['avg_ms']:.1f}ms")
        assert p95 < 500
```

### `tests/test_carga.py`
```python
from ecommerce import EcommerceSimulator

def test_throughput_sustentado_maior_2000_rps():
    sim = EcommerceSimulator(random_seed=42, baseline_capacity=2000)
    s = sim.simulate_stage(users=500, duration_s=1.0, name="peak-1s")
    print(f"[Carga] Throughput={s.throughput_rps:.1f} req/s, Erros={s.error_rate:.2f}%")
    assert s.throughput_rps > 2000
```

### `tests/test_estresse.py`
```python
from ecommerce import EcommerceSimulator

def test_ponto_de_quebra_acima_15000():
    sim = EcommerceSimulator(random_seed=42, baseline_capacity=4000)
    stress = sim.simulate_stress_test(
        start_users=12000, max_users=50000, step=2000, duration_s=30, tolerated_error_pct=5.0
    )
    print(f"[Estresse] Ponto de quebra={stress.breakpoint_users} usuários | Motivo={stress.reason}")
    assert stress.breakpoint_users and stress.breakpoint_users > 15000
```

### `tests/test_escalabilidade.py`
```python
from ecommerce import EcommerceSimulator, calculate_horizontal_scaling_efficiency

def test_eficiencia_horizontal_maior_80_porcento():
    sim = EcommerceSimulator(random_seed=42, baseline_capacity=2000)
    results = sim.simulate_scaling(server_counts=[1, 2, 4, 8], baseline_users=1600, duration_s=60)
    ideal = [(srv, results[1].throughput_rps * srv) for srv in results]
    real  = [(srv, results[srv].throughput_rps) for srv in results]
    eff = calculate_horizontal_scaling_efficiency(ideal, real)
    min_eff = min(eff.values())
    print(f"[Escalabilidade] Eficiências: " + ", ".join([f"{k} srv(s)={v:.2f}%" for k,v in eff.items()]))
    assert min_eff > 80
```

### `tests/test_seguranca.py`
```python
from ecommerce import EcommerceSimulator

def test_rate_limiting_bloqueia_excesso():
    sim = EcommerceSimulator(random_seed=42, baseline_capacity=2000)
    r = sim.simulate_rate_limiting(users=300, duration_s=60, limit_per_minute=100, burst=0)
    print(f"[Segurança] Permitidas={r.allowed}, Bloqueadas={r.blocked} ({r.blockage_ratio:.2f}%)")
    assert r.blocked > 0 and r.blockage_ratio > 0.0
```

## Execução dos testes

1. Criar ambiente virtual: `python -m venv .venv`
2. Ativar:
   - **PowerShell (Windows):** `.\.venv\Scripts\Activate.ps1`
   - **CMD (Windows):** `.venv\Scripts\activate.bat`
   - **Linux/macOS:** `source .venv/bin/activate`
3. Instalar dependências: `pip install -r requirements.txt`
4. Rodar com métricas impressas: `pytest -s`

## Saída dos testes (`pytest -s`)

tests/test_carga.py [Carga] throughput=2290.2 req/s | erros=0.47% | p95=443.3ms
tests/test_desempenho.py [Desempenho] baseline p95=447.2ms média=262.4ms p99=554.5ms | ramp_up p95=446.1ms média=262.6ms p99=550.2ms | peak p95=443.6ms média=261.9ms p99=558.5ms
tests/test_escalabilidade.py [Escalabilidade] ef_min=100.00% | 1srv=100.00% | 2srvs=102.94% | 4srvs=101.65% | 8srvs=101.40%
tests/test_estresse.py [Estresse] ponto_quebra=48000 usuários | motivo=error_rate 5.13% >= 5.00%
tests/test_seguranca.py [Segurança] permitidas=300 | bloqueadas=6688 | bloqueio=95.71%

## Resultados das métricas

| **Tipo**        | **Métricas coletadas (amostra)**                                                                                  | **Meta**            | **Resultado**                           | **Status** |
|-----------------|--------------------------------------------------------------------------------------------------------------------|---------------------|-----------------------------------------|-----------|
| **Desempenho**  | **P95:** 447.2 / 446.1 / 443.6 ms (baseline/ramp/peak); **média ≈** 262 ms; **P99 ~** 554–559 ms                  | **P95 < 500 ms**    | Dentro do limite em todas as fases      | **Aprovado** |
| **Carga**       | **Throughput:** 2290.2 req/s; **erro:** 0.47%; **P95:** 443.3 ms                                                   | **> 2000 req/s**    | Acima da meta                           | **Aprovado** |
| **Estresse**    | **Ponto de quebra:** 48.000 usuários (violação por erro ≥ 5%)                                                      | **> 15.000 usuários** | Muito acima do alvo                     | **Aprovado** |
| **Escalabilidade** | **Eficiência horizontal:** 100.0%, 102.94%, 101.65%, 101.40% (1/2/4/8 servidores)                              | **> 80%**           | Escala quase linear preservada          | **Aprovado** |
| **Segurança**   | **Rate limit 100 req/min →** **permitidas:** 300 • **bloqueadas:** 6688 (95.71%)                                   | **100 req/min/IP**  | Política aplicada corretamente          | **Aprovado** |

## Análise de aprovação

- **Desempenho** — margem confortável (**P95 ~ 443–447 ms**), pior caso ainda **< 500 ms**.
- **Carga** — **2,29k req/s** sustentados **> 2k req/s**, com erro baixo (**0,47%**).
- **Estresse** — degradação ocorre somente por volta de **48k usuários**, respeitando meta **> 15k**.
- **Escalabilidade** — duplicar instâncias praticamente dobra o throughput (eficiência **~100%** observada).
- **Segurança** — **rate limiting** efetivo: grande parcela de excedentes **bloqueada** (**95,71%**).

---

## Observações de reprodutibilidade

- `random_seed=42` utilizado para garantir resultados estáveis.
- Parâmetros de cada teste documentados nos próprios arquivos em `tests/`.
- Rodar `pytest -s` reproduz as métricas exibidas acima.
