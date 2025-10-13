Atividade 09 - Gerenciador de Tarefas
====================================

Sobre o Projeto
----------
O projeto implementa um gerenciador de tarefas. A aplicacao combina conceitos de orientacao a objetos (heranca, polimorfismo, encapsulamento) com boas praticas de modularizacao, persistencia em memoria e uma suite de testes automatizados que exercita cenarios unitarios e casos com `Mock`.

Principais objetivos do estudo:
- Exercitar modelagem de dominio por meio das classes `Task`, `BaseTask` e `RecurringTask`.
- Demonstrar como separar responsabilidades entre armazenamento (`InMemoryStorage`), repositorio (`TaskRepository`) e camada de servico (`TaskService`).
- Cobrir funcionalidades com testes unitarios, testes com mocks e cenarios de componente, enfatizando como validar integracoes.

O projeto usa Python 3.10+, `pytest` e `pytest-cov` para garantir feedback rapido sobre a evolucao das funcionalidades.

## Membros do Grupo

> Felipe Orlando Lanzara - 22.225.015-1

> Pedro Henrique Lega Kramer Costa - 22.125.091-3

> Ruan Pastrelo Turola - 22.225.013-6

Estrutura do projeto
--------------------

```
Atividade09-testes-orientados-a-objetos-e-componentes/
├── README.md                  # guia rápido do projeto
├── Relatorio.md               # relatorio dos testes automatizados
├── exemplo-de-uso.py          # script simples de demonstracao
├── requirements.txt           # dependencias do projeto
├── task_manager/              # codigo-fonte principal
│   ├── repository.py
│   ├── service.py
│   ├── storage.py
│   └── task.py
└── tests/                     # testes automatizados
    ├── test_repository.py
    ├── test_service.py
    └── test_task.py
```

Requisitos
----------

- Python 3.10+
- `pip` atualizado
- Ferramenta para ambientes virtuais (`venv` já vem com Python)

Primeiros passos
----------------

1. Clone o repositório e acesse a pasta do exercício:
   ```
   git clone https://github.com/gb-cs-rt/CC8550-STS.git
   cd Atividade09-testes-orientados-a-objetos-e-componentes
   ```
2. Crie e ative o ambiente virtual:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências listadas:
   ```
   pip install -r requirements.txt
   ```

Instalacao
----------

Certifique-se de estar em um ambiente virtual e instale as dependencias:

```
pip install -r requirements.txt
```

Como testar
-----------

Execute a suite de testes com:

```
pytest -v
pytest --cov=task_manager
```

Exemplo de uso
--------------

Execute o script de demonstração para ver o fluxo funcionando e também executar os testes automatizados:

```
python exemplo-de-uso.py
```
