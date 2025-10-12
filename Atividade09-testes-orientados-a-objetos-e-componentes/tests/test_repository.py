"""Testes para o repositório de tarefas."""

from datetime import datetime
from unittest.mock import Mock

import pytest

from task_manager.repository import TaskRepository
from task_manager.storage import InMemoryStorage
from task_manager.task import Priority, Task


@pytest.fixture
def storage_mock():
    return Mock(spec=InMemoryStorage)


@pytest.fixture
def repository(storage_mock):
    return TaskRepository(storage_mock)


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
