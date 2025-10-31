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

## Simulador (`ecommerce.py`) — visão geral

APIs principais:
- `simulate_stage` (estágio fixo com latências, erros, throughput)  
- `simulate_load_curve` (baseline → ramp_up → peak)  
- `simulate_stress_test` (acha o ponto de quebra por erro tolerado)  
- `simulate_scaling` (scale-out por servidores + eficiência)  
- `simulate_rate_limiting` (aplica janela 1 min, retorna permitidos/bloqueados)

Auxiliares: `percentile`, `calculate_latency_stats`, `calculate_throughput`, `calculate_horizontal_scaling_efficiency`, `enforce_rate_limit`.  
Dataclasses: `StageResult`, `StressTestResult`, `RateLimitResult`.

---

## Execução dos testes

```bash
python -m venv .venv
# PowerShell: .\.venv\Scripts\Activate.ps1  |  Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
pytest -s
