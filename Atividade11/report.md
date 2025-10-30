# Relatório — Testes Não-Funcionais (Black Friday)
Data: 2025-10-30 01:41:46Z

Metas:
- P95 < **500 ms**
- Throughput sustentado ≥ **2000 req/s**
- Ponto de quebra > **15000 usuários**
- Eficiência horizontal ≥ **80%**
- Rate limiting: **100 req/min/IP**

### Desempenho (P95)
- Amostras: **5000** | Concorrência: **200** | Erros HTTP (>=500): **131**
- **P95 medido:** **2225.03 ms** | **Meta:** `< 500 ms`
- Resultado: ❌ Reprovado
### Carga (Throughput)
- Duração: **60s** | Concorrência: **200** | Requisições OK: **9691**
- **Throughput sustentado:** **154.89 req/s** | **Meta:** `≥ 2000 req/s`
- Resultado: ❌ Reprovado
### Estresse (Ponto de quebra)
- **Ponto de quebra estimado:** **~1000 usuários** | **Meta:** `> 15000 usuários`
- Critério: P95 > 2×500ms **ou** erros > 5% no degrau.
- Resultado: ❌ Reprovado
### Escalabilidade (Eficiência Horizontal)
- Pior eficiência (n>1): **19.79%** | **Meta:** `≥ 80%`
- Detalhes:
- n=1 | conc=200 | rps=167.83 | eff=100.00%
- n=2 | conc=400 | rps=335.20 | eff=99.86%
- n=4 | conc=800 | rps=390.70 | eff=58.20%
- n=8 | conc=1600 | rps=265.64 | eff=19.79%
- Resultado: ❌ Reprovado
### Segurança (Rate limiting)
- Enviadas: **130** | OK (<400): **129** | HTTP 429: **0**
- Política esperada: **100 req/min/IP** ⇒ excesso esperado: **30** 429
- Resultado: ❌ Reprovado

---

