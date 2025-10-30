import subprocess, sys, os

# script para inicialização dos testes na paste de testes

# Para rodar no console usar:

##python runner.py security
#python runner.py scalability
#python runner.py stress
#python runner.py load
#python runner.py perf
# tudo:
#python runner.py all


def run(cmd):
    print("+", " ".join(cmd))
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd() + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.run([sys.executable, *cmd], check=True, env=env)

def main():
    if len(sys.argv) < 2:
        print("Usage: python runner.py [perf|load|stress|scalability|security|all]")
        raise SystemExit(1)
    target = sys.argv[1]
    if target in ("perf","all"):
        run(["tests/performance_p95.py"])
    if target in ("load","all"):
        run(["tests/load_throughput.py"])
    if target in ("stress","all"):
        run(["tests/stress_breakpoint.py"])
    if target in ("scalability","all"):
        run(["tests/scalability_efficiency.py"])
    if target in ("security","all"):
        run(["tests/security_rate_limit.py"])

if __name__ == "__main__":
    main()
