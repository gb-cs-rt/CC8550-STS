
# E-commerce Black Friday — Non-Functional Test Suite (Python)

## Inicialização


### 1) Criar ambiente virtual (venv):

- python -m venv .venv 
- .venv/Scripts/Activate.ps1

### 2) Instalar as dependencias

> O venv deve estar ativado 

- pip install -r requirements.txt

### 3) Ajustar path de dependencias

```bash
ni .\src\__init__.py -Force
```

### 3) Rodar os scripts de teste:

```bash
python runner.py perf
python runner.py load
python runner.py stress
python runner.py scalability
python runner.py security
# tudo:
python runner.py all
```
> para o teste de url troque no config.yaml para a url desejada
### 4) Gere o relatório:

```bash
python report_generator.py
```

Exemplos de testes em Python para **Desempenho (P95)**, **Carga (req/s)**, **Estresse (ponto de quebra)**,
**Escalabilidade (eficiência horizontal)** e **Segurança (rate limiting)**.

## Como usar
1. Edite `config.yaml` (troque `base_url` e `endpoint_path`).
2. Instale dependências: `pip install -r requirements.txt`
3. Rode os testes:
```bash
python runner.py perf
python runner.py load
python runner.py stress
python runner.py scalability
python runner.py security
# tudo:
python runner.py all
```
4. Gere o relatório:
```bash
python report_generator.py
```

> Nota: O teste é um teste real simulado, cada teste pode demorar bastante tempo