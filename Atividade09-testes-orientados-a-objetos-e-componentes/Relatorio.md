# Relatorio de Testes

## Introducao
Este documento consolida os testes automatizados do projeto de gerenciador de tarefas. O objetivo e mostrar como a suite atual é validada, os principios de orientacao a objetos e o comportamento integrado dos componentes.

## Arquitetura Validada
- Modulagem de dominio em `task_manager/task.py`, com a hierarquia `BaseTask`, `Task` e `RecurringTask`.
- Persistencia em memoria pelo par `TaskRepository` e `InMemoryStorage`.
- Camada de servico `TaskService`, responsavel por orquestrar criacao, atualizacao, listagem e exclusao de tarefas.

## Estrategia de Testes
### Testes unitarios de dominio
- Arquivo `tests/test_task.py` cobre validacoes de titulo, prazo e mudanca de status.
- Exercicios de encapsulamento via property `status` garantem que apenas valores do enum `Status` sejam aceitos.
- A subclasse `RecurringTask` e testada quanto a validacoes proprias e comportamento polimorfico.

### Testes unitarios com mocks
- Em `tests/test_repository.py` usamos `Mock` para validar as interacoes entre `TaskRepository` e `InMemoryStorage`, incluindo atribuicao de IDs, update e remocao.
- Em `tests/test_service.py` os metodos do `TaskService` sao exercitados com um `TaskRepository` mockado, assegurando chamadas (`save`, `find_all`, `find_by_id`, `update`, `delete`) e tratamentos de erro.

### Testes de componente
- `tests/test_repository.py` tambem possui cenarios usando a implementacao real de `InMemoryStorage`, cobrindo o ciclo CRUD completo do repositorio.
- `tests/test_service.py::test_task_service_component_flow` integra `TaskService`, `TaskRepository` e `InMemoryStorage`, validando a criacao, listagem, atualizacao de status e remocao de uma tarefa real.

## Conceitos de Orientacao a Objetos Exercitados
- **Encapsulamento:** O acesso ao status e controlado por property em `BaseTask`, e os testes garantem que valores invalidos geram erro.
- **Heranca e Polimorfismo:** `RecurringTask` estende `Task`, reutiliza validacoes da classe base e adiciona regras proprias. Os testes confirmam que colecoes heterogeneas de tarefas executam `validar()` corretamente.
- **Uso de abstracoes:** A classe abstrata `BaseTask` estabelece o contrato de validacao, promovendo extensibilidade para novas variacoes de tarefa.

## Resultados dos testes

**Comando utilizado:**
```
pytest -v
```

**Saída do teste**
```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-7.4.0, pluggy-1.6.0 -- /home/ruan/Documentos/FEI/8_Semestre/CC8550-STS/Atividade09-testes-orientados-a-objetos-e-componentes/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ruan/Documentos/FEI/8_Semestre/CC8550-STS/Atividade09-testes-orientados-a-objetos-e-componentes
plugins: cov-4.0.0, mock-3.11.1
collected 35 items                                                                                                                                                                                                

tests/test_repository.py::test_save_atribui_id PASSED                                                                                                                                                       [  2%]
tests/test_repository.py::test_save_chama_storage_add PASSED                                                                                                                                                [  5%]
tests/test_repository.py::test_save_aceita_subclasse PASSED                                                                                                                                                 [  8%]
tests/test_repository.py::test_find_by_id_chama_storage_get PASSED                                                                                                                                          [ 11%]
tests/test_repository.py::test_find_all_retorna_lista PASSED                                                                                                                                                [ 14%]
tests/test_repository.py::test_delete_chama_storage_remove PASSED                                                                                                                                           [ 17%]
tests/test_repository.py::test_update_chama_storage_update PASSED                                                                                                                                           [ 20%]
tests/test_repository.py::test_update_sem_id_levanta_erro PASSED                                                                                                                                            [ 22%]
tests/test_repository.py::test_save_com_id_levanta_erro PASSED                                                                                                                                              [ 25%]
tests/test_repository.py::test_storage_add_and_get PASSED                                                                                                                                                   [ 28%]
tests/test_repository.py::test_storage_get_all PASSED                                                                                                                                                       [ 31%]
tests/test_repository.py::test_storage_update PASSED                                                                                                                                                        [ 34%]
tests/test_repository.py::test_storage_remove PASSED                                                                                                                                                        [ 37%]
tests/test_repository.py::test_storage_delete_alias PASSED                                                                                                                                                  [ 40%]
tests/test_repository.py::test_storage_clear PASSED                                                                                                                                                         [ 42%]
tests/test_service.py::TestTaskService::test_criar_tarefa_valida PASSED                                                                                                                                     [ 45%]
tests/test_service.py::TestTaskService::test_criar_tarefa_titulo_vazio PASSED                                                                                                                               [ 48%]
tests/test_service.py::TestTaskService::test_criar_tarefa_prioridade_invalida PASSED                                                                                                                        [ 51%]
tests/test_service.py::TestTaskService::test_criar_tarefa_status_invalido PASSED                                                                                                                            [ 54%]
tests/test_service.py::TestTaskService::test_listar_todas PASSED                                                                                                                                            [ 57%]
tests/test_service.py::TestTaskService::test_atualizar_status_valido PASSED                                                                                                                                 [ 60%]
tests/test_service.py::TestTaskService::test_atualizar_status_tarefa_nao_encontrada PASSED                                                                                                                  [ 62%]
tests/test_service.py::TestTaskService::test_atualizar_status_invalido PASSED                                                                                                                               [ 65%]
tests/test_service.py::TestTaskService::test_remover_tarefa_existente PASSED                                                                                                                                [ 68%]
tests/test_service.py::TestTaskService::test_remover_tarefa_nao_existente PASSED                                                                                                                            [ 71%]
tests/test_service.py::test_task_service_component_flow PASSED                                                                                                                                              [ 74%]
tests/test_task.py::TestTask::test_criacao_valida PASSED                                                                                                                                                    [ 77%]
tests/test_task.py::TestTask::test_titulo_invalido PASSED                                                                                                                                                   [ 80%]
tests/test_task.py::TestTask::test_prazo_no_passado PASSED                                                                                                                                                  [ 82%]
tests/test_task.py::TestTask::test_atualizar_status_valido PASSED                                                                                                                                           [ 85%]
tests/test_task.py::TestTask::test_atualizar_status_invalido PASSED                                                                                                                                         [ 88%]
tests/test_task.py::TestTask::test_status_property_encapsula_enum PASSED                                                                                                                                    [ 91%]
tests/test_task.py::TestTask::test_recurring_task_herda_de_task PASSED                                                                                                                                      [ 94%]
tests/test_task.py::TestTask::test_recurring_task_validar_frequencia_invalida PASSED                                                                                                                        [ 97%]
tests/test_task.py::TestTask::test_polimorfismo_validar PASSED                                                                                                                                              [100%]

=============================================================================================== 35 passed in 0.04s ================================================================================================
```

**Comando utilizado:**
```
pytest --cov=task_manager
```

**Saída do teste**
```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-7.4.0, pluggy-1.6.0
rootdir: /home/ruan/Documentos/FEI/8_Semestre/CC8550-STS/Atividade09-testes-orientados-a-objetos-e-componentes
plugins: cov-4.0.0, mock-3.11.1
collected 35 items                                                                                                                                                                                                

tests/test_repository.py ...............                                                                                                                                                                    [ 42%]
tests/test_service.py ...........                                                                                                                                                                           [ 74%]
tests/test_task.py .........                                                                                                                                                                                [100%]

---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                         Stmts   Miss  Cover
------------------------------------------------
task_manager/__init__.py         3      0   100%
task_manager/repository.py      24      0   100%
task_manager/service.py         28      0   100%
task_manager/storage.py         20      0   100%
task_manager/task.py            49      0   100%
------------------------------------------------
TOTAL                          124      0   100%


=============================================================================================== 35 passed in 0.08s ================================================================================================
```

## Conclusao
A suite de testes atual sustenta o ciclo de desenvolvimento do gerenciador de tarefas ao combinar verificacoes unitarias, exercicios de conceitos de orientacao a objetos e cenarios de componente. Isso gera feedback rapido sobre regressões e garante que a modelagem de dominio, a camada de persistencia e o servico funcionem de forma coesa.