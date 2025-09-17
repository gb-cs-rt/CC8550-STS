# Projeto Calculadora — Testes e Cobertura

Este projeto implementa uma calculadora simples em Python, acompanhada por testes de unidade e de integração, além de relatório de cobertura de código.

## Estrutura de Pastas

```
Atividade05/
├─ src/
│  └─ calculadora.py        # Código da calculadora
├─ tests/
│  ├─ __init__.py           # Arquivo vazio
│  ├─ test_unidade.py       # Testes de unidade
│  └─ test_integracao.py    # Testes de integração
├─ requirements.txt         # Dependências
├─ READMEATV5.md            # Este README (documentação)
└─ relatorio.md             # Relatório dos testes (opcional)
```

## Requisitos

O projeto usa apenas a biblioteca padrão em tempo de execução. Para medir cobertura e gerar o relatório HTML:

```
coverage>=7.0.0
```

Instale com:

```
pip install -r requirements.txt
```

## Comandos de Execução (unittest)

- Executar todos os testes:
  - `python3 -m unittest discover -v`

- Executar com cobertura e gerar relatório HTML:
  - `python3 -m coverage run --source=src -m unittest discover`
  - `python3 -m coverage report -m`
  - `python3 -m coverage html`  (gera a pasta `htmlcov/`)

- Executar teste específico (exemplo):
  - `python3 -m unittest tests.test_unidade.TestUnidade.test_entrada_saida_soma -v`

## Abrir o Relatório HTML

- Abra `htmlcov/index.html` no navegador.

## Resultados Obtidos (referência)

- Testes: 34 executados, 34 aprovados, 0 falhas.
- Cobertura (apenas `src`): 100% em `src/calculadora.py`.

Comandos usados para aferição:

```
python3 -m unittest discover -v
python3 -m coverage run --source=src -m unittest discover && python3 -m coverage report -m && python3 -m coverage html
```

## O que foi testado

- Entrada/saída: soma, subtração, multiplicação, divisão e potência, incluindo floats e negativos.
- Tipagem: rejeição de tipos inválidos (strings, None, coleções, dicionários).
- Consistência: conteúdo e ordem do histórico, preservação do último resultado ao limpar histórico.
- Limites: zero, valores muito pequenos e muito grandes (incluindo estouro para `inf`).
- Fluxos de controle: caminhos de sucesso e de erro (divisão por zero).
- Mensagens de erro: conferência da mensagem lançada em divisão por zero.

## Ajustes/Corrigendas Realizadas

- Padronização da mensagem de erro na divisão por zero para corresponder aos testes: "Divisão por zero nao permitida".

## Exemplo de Uso da Calculadora

```python
from src.calculadora import Calculadora

calc = Calculadora()
calc.somar(2, 3)          # 5
calc.multiplicar(5, 4)    # 20
print(calc.obter_ultimo_resultado())  # 20
print(calc.historico)     # ['2 + 3 = 5', '5 * 4 = 20']
```

---
