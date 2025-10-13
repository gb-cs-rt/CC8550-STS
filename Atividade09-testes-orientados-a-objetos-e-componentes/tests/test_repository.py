"""Testes para o repositório de tarefas."""

from datetime import datetime
from unittest.mock import Mock
import pytest
from task_manager.repository import TaskRepository
from task_manager.storage import InMemoryStorage
from task_manager.task import Priority, Task, RecurringTask

@pytest.fixture
def storage_mock():
    return Mock(spec=InMemoryStorage)

@pytest.fixture
def repository(storage_mock):
    return TaskRepository(storage_mock)

@pytest.fixture
def storage():
    return InMemoryStorage()

@pytest.fixture
def example_task():
    return Task(
        id=None,
        titulo="Estudar testes",
        descricao="Revisar mocks e fixtures",
        prioridade=Priority.ALTA,
        prazo=datetime(2025, 1, 1),
    )

def test_save_atribui_id(repository, storage_mock, example_task):
    saved_task = repository.save(example_task)
    assert saved_task.id == 1
    storage_mock.add.assert_called_once_with(saved_task.id, saved_task)

def test_save_chama_storage_add(repository, storage_mock, example_task):
    repository.save(example_task)
    storage_mock.add.assert_called_once_with(example_task.id, example_task)

def test_save_aceita_subclasse(repository, storage_mock):
    recurring = RecurringTask(
        id=None,
        titulo="Treino diario",
        descricao="Corrida matinal",
        prioridade=Priority.MEDIA,
        prazo=datetime(2025, 1, 2),
        frequencia_dias=1,
    )
    repository.save(recurring)
    assert recurring.id == 1
    storage_mock.add.assert_called_once_with(recurring.id, recurring)

def test_find_by_id_chama_storage_get(repository, storage_mock):
    task = Mock(spec=Task)
    storage_mock.get.return_value = task
    result = repository.find_by_id(42)
    storage_mock.get.assert_called_once_with(42)
    assert result is task

def test_find_all_retorna_lista(repository, storage_mock):
    tasks = [Mock(spec=Task), Mock(spec=Task)]
    storage_mock.get_all.return_value = tasks
    result = repository.find_all()
    storage_mock.get_all.assert_called_once()
    assert result == tasks

def test_delete_chama_storage_remove(repository, storage_mock):
    repository.delete(42)
    storage_mock.remove.assert_called_once_with(42)


def test_update_chama_storage_update(repository, storage_mock, example_task):
    example_task.id = 1
    repository.update(example_task)
    storage_mock.update.assert_called_once_with(example_task.id, example_task)


def test_update_sem_id_levanta_erro(repository, example_task):
    with pytest.raises(ValueError):
        repository.update(example_task)


def test_save_com_id_levanta_erro(repository, example_task):
    example_task.id = 1
    with pytest.raises(ValueError):
        repository.save(example_task)

def test_storage_add_and_get(storage):
    item = Mock()
    storage.add(1, item)
    assert storage.get(1) is item
    assert storage.get(99) is None

def test_storage_get_all(storage):
    tarefa1 = Mock()
    tarefa2 = Mock()
    storage.add(1, tarefa1)
    storage.add(2, tarefa2)
    items = storage.get_all()
    assert tarefa1 in items
    assert tarefa2 in items

def test_storage_update(storage):
    tarefa_original = Mock()
    tarefa_atualizada = Mock()
    storage.add(1, tarefa_original)
    storage.update(1, tarefa_atualizada)
    assert storage.get(1) is tarefa_atualizada

def test_storage_remove(storage):
    tarefa = Mock()
    storage.add(1, tarefa)
    assert storage.remove(1) is True
    assert storage.get(1) is None
    assert storage.remove(1) is False

def test_storage_delete_alias(storage):
    tarefa = Mock()
    storage.add(5, tarefa)
    assert storage.delete(5) is True
    assert storage.delete(5) is False

def test_storage_clear(storage):
    storage.add(1, Mock())
    storage.add(2, Mock())
    storage.clear()
    assert storage.get_all() == []
