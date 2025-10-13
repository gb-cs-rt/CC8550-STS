"""Testes para o módulo service do gerenciador de tarefas."""

import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
from task_manager.service import TaskService
from task_manager.repository import TaskRepository
from task_manager.storage import InMemoryStorage
from task_manager.task import Task, Priority, Status

class TestTaskService:
    """Testes para a classe TaskService."""

    def setup_method(self):
        """Configuração antes de cada método de teste."""
        self.mock_repository = Mock(spec=TaskRepository)
        self.service = TaskService(self.mock_repository)
        self.prazo = datetime.now() + timedelta(days=1)

    def test_criar_tarefa_valida(self):
        """Teste de criação válida de uma tarefa."""
        tarefa_salva = Task(1, "Título", "Descrição", Priority.ALTA, self.prazo, Status.PENDENTE)
        self.mock_repository.save.return_value = tarefa_salva

        resultado = self.service.criar_tarefa("Título", "Descrição", Priority.ALTA, self.prazo)

        assert resultado is tarefa_salva
        self.mock_repository.save.assert_called_once()
        tarefa_enviada = self.mock_repository.save.call_args.args[0]
        assert isinstance(tarefa_enviada, Task)
        assert tarefa_enviada.id is None
        assert tarefa_enviada.titulo == "Título"

    def test_criar_tarefa_titulo_vazio(self):
        """Teste de criação com título vazio (deve lançar ValueError)."""
        with pytest.raises(ValueError):
            self.service.criar_tarefa("", "Descrição", Priority.MEDIA, self.prazo)
        self.mock_repository.save.assert_not_called()

    def test_criar_tarefa_prioridade_invalida(self):
        """Teste de criação com prioridade inválida (deve lançar ValueError)."""
        with pytest.raises(ValueError):
            self.service.criar_tarefa("Título", "Descrição", "ALTA", self.prazo)
        self.mock_repository.save.assert_not_called()

    def test_criar_tarefa_status_invalido(self):
        """Teste de criação com status inválido (deve lançar ValueError)."""
        with pytest.raises(ValueError):
            self.service.criar_tarefa("Título", "Descrição", Priority.ALTA, self.prazo, status="concluida")
        self.mock_repository.save.assert_not_called()

    def test_listar_todas(self):
        """Teste de listagem de todas as tarefas."""
        tarefas = [
            Task(1, "Desc1", "Desc 1", Priority.BAIXA, self.prazo, Status.PENDENTE),
            Task(2, "Desc2", "Desc 2", Priority.MEDIA, self.prazo, Status.EM_ANDAMENTO),
        ]
        self.mock_repository.find_all.return_value = tarefas

        resultado = self.service.listar_todas()

        assert resultado == tarefas
        self.mock_repository.find_all.assert_called_once()

    def test_atualizar_status_valido(self):
        """Teste de atualização de status válido."""
        tarefa_existente = Task(1, "Tarefa", "Desc", Priority.MEDIA, self.prazo, Status.PENDENTE)
        self.mock_repository.find_by_id.return_value = tarefa_existente
        self.mock_repository.update.return_value = tarefa_existente

        resultado = self.service.atualizar_status(1, Status.CONCLUIDA)

        assert resultado.status == Status.CONCLUIDA
        self.mock_repository.find_by_id.assert_called_once_with(1)
        self.mock_repository.update.assert_called_once_with(tarefa_existente)

    def test_atualizar_status_tarefa_nao_encontrada(self):
        """Teste de atualização quando a tarefa não é encontrada (deve lançar ValueError)."""
        self.mock_repository.find_by_id.return_value = None

        with pytest.raises(ValueError):
            self.service.atualizar_status(1, Status.CONCLUIDA)

        self.mock_repository.find_by_id.assert_called_once_with(1)
        self.mock_repository.update.assert_not_called()

    def test_atualizar_status_invalido(self):
        """Teste de atualização com status inválido (deve lançar ValueError)."""
        tarefa_existente = Task(1, "Tarefa", "Desc", Priority.MEDIA, self.prazo, Status.PENDENTE)
        self.mock_repository.find_by_id.return_value = tarefa_existente

        with pytest.raises(ValueError):
            self.service.atualizar_status(1, "concluida")

        self.mock_repository.update.assert_not_called()

    def test_remover_tarefa_existente(self):
        """Teste de remoção de uma tarefa existente."""
        self.mock_repository.delete.return_value = True

        resultado = self.service.remover_tarefa(1)

        assert resultado is True
        self.mock_repository.delete.assert_called_once_with(1)

    def test_remover_tarefa_nao_existente(self):
        """Teste de remoção de uma tarefa não existente."""
        self.mock_repository.delete.return_value = False

        resultado = self.service.remover_tarefa(1)

        assert resultado is False
        self.mock_repository.delete.assert_called_once_with(1)


def test_task_service_component_flow():
    """Teste de componente integrando TaskService, TaskRepository e InMemoryStorage."""
    storage = InMemoryStorage()
    repository = TaskRepository(storage)
    service = TaskService(repository)
    prazo = datetime.now() + timedelta(days=2)

    tarefa = service.criar_tarefa("Estudar", "Revisão de testes", Priority.MEDIA, prazo)
    assert tarefa.id == 1

    tarefas = service.listar_todas()
    assert len(tarefas) == 1

    atualizada = service.atualizar_status(tarefa.id, Status.CONCLUIDA)
    assert atualizada.status == Status.CONCLUIDA

    assert service.remover_tarefa(tarefa.id) is True
    assert service.listar_todas() == []
