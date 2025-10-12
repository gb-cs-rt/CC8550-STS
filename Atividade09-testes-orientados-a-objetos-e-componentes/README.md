Atividade 09 - Gerenciador de Tarefas
====================================

Projeto de exemplo usado na disciplina CC8550 (STS) para demonstrar como organizar um pequeno gerenciador de tarefas com foco em testes orientados a objetos e componentes.

Instalacao
----------

Certifique-se de estar em um ambiente virtual e instale as dependencias:

```
pip install -r requirements.txt
```

Testes
------

Execute a suite de testes com:

```
pytest -v
```

Estrutura do projeto
--------------------

```
.
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
