
import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime

def load_csv(path):
    p = Path(path)
    return pd.read_csv(p) if p.exists() else None

def status(ok: bool) -> str:
    return " Aprovado" if ok else " Reprovado"

def main():
    cfg = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))
    tgt = cfg["targets"]
    out = []

    perf = load_csv("results/performance_p95.csv")
    if perf is not None and not perf.empty:
        p95 = float(perf.iloc[-1]["latency_p95_ms"])
        ok = p95 < tgt["perf_p95_ms"]
        out.append(f"### Desempenho (P95)\n- Valor medido: **{p95:.2f} ms**\n- Meta: **< {tgt['perf_p95_ms']} ms**\n- Resultado: {status(ok)}\n")

    load = load_csv("results/load_throughput.csv")
    if load is not None and not load.empty:
        rps = float(load.iloc[-1]["rps_ok"])
        ok = rps >= tgt["load_throughput_rps"]
        out.append(f"### Carga (Throughput)\n- Valor medido: **{rps:.2f} req/s**\n- Meta: **≥ {tgt['load_throughput_rps']} req/s**\n- Resultado: {status(ok)}\n")

    stress = load_csv("results/stress_breakpoint.csv")
    if stress is not None and not stress.empty:
        breakpoint_users = int(stress.iloc[-1]['users'])
        for _, row in stress.iterrows():
            p95 = float(row.get("p95_ms", 0) or 0)
            err = float(row.get("errors", 0) or 0)
            total = float(row.get("total", 1) or 1)
            if p95 > tgt["perf_p95_ms"] * 2 or (err / max(1,total)) > 0.05:
                breakpoint_users = int(row["users"])
                break
        ok = breakpoint_users > tgt["stress_breakpoint_users"]
        out.append(f"### Estresse (Ponto de quebra)\n- Valor medido: **~{breakpoint_users} usuários**\n- Meta: **> {tgt['stress_breakpoint_users']} usuários**\n- Resultado: {status(ok)}\n")

    scale = load_csv("results/scalability_efficiency.csv")
    if scale is not None and not scale.empty:
        df = scale[scale["instances"] > 1]
        eff_min = float(df["efficiency_pct"].min()) if not df.empty else 0.0
        ok = eff_min >= tgt["scalability_efficiency_pct"]
        out.append(f"### Escalabilidade (Eficiência Horizontal)\n- Pior eficiência medida: **{eff_min:.2f}%**\n- Meta: **≥ {tgt['scalability_efficiency_pct']}%**\n- Resultado: {status(ok)}\n")

    sec = load_csv("results/security_rate_limit.csv")
    if sec is not None and not sec.empty:
        last = sec.iloc[-1]
        sent = int(last["sent"]); rl = int(last["http_429"])
        ok = rl >= max(0, sent - tgt["security_ratelimit_per_min"])
        out.append(f"### Segurança (Rate limiting)\n- 429 recebidos: **{rl}** (de {sent} envios)\n- Política esperada: **{tgt['security_ratelimit_per_min']} req/min/IP**\n- Resultado: {status(ok)}\n")

    report = f"""# Relatório de Resultados — E-commerce Black Friday
Data: {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")}

{"".join(out) if out else "_Sem dados. Execute os testes primeiro._"}

---
_Nota:_ Este relatório analisa a **aprovação/reprovação** com base nas metas de `config.yaml`.
"""
    Path("results").mkdir(parents=True, exist_ok=True)
    Path("results/report.md").write_text(report, encoding="utf-8")
    print("Relatório gerado em results/report.md")

if __name__ == "__main__":
    main()
