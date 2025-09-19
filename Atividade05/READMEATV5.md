# Projeto Calculadora — Testes e Cobertura

## Contexto
Projeto desenvolvido para a disciplina CC8550 - SIMULAÇÃO E TESTE DE SOFTWARE. O objetivo e praticar técnicas de teste unitário e de integração a partir de uma classe `Calculadora` que encapsula operações matemáticas básicas, histórico de execuções e consultas ao último resultado computado.

## Objetivos da atividade
- Exercitar escrita e manutenção de testes automatizados com `unittest`.
- Investigar limites de input, validações e mensagens de erro.
- Avaliar relatórios de cobertura utilizando a biblioteca `coverage`.

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
└─ relatorio.md             # Relatório dos testes
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
   ```
   python3 -m unittest discover tests -v
   ```

- Executar com cobertura e gerar relatório HTML:
  ```
  python3 -m coverage run -m unittest discover
  python3 -m coverage report -m
  python3 -m coverage html
  ```

- Executar teste específico (exemplo):
  ```
  python3 -m unittest tests.test_unidade.TestUnidade.test_entrada_saida_soma -v
  ```

## Abrir o Relatório HTML

- Abra `htmlcov/index.html` no navegador.
