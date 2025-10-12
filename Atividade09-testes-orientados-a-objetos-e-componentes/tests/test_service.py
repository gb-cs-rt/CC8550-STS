"""Testes para o módulo service do gerenciador de tarefas."""

import pytest
from datetime import datetime, timedelta
from task_manager.service import TaskService
from task_manager.repository import TaskRepository
from task_manager.task import Task, Priority
from unittest.mock import Mock

class TestTaskService:
    """Testes para a classe TaskService."""

    def setup_method(self):
        """Configuração antes de cada método de teste."""
        self.mock_repository = Mock()
        self.service = TaskService(self.mock_repository)

    def test_criar_tarefa_valida(self):
        """Teste de criação válida de uma tarefa."""
        tarefa = self.service.criar_tarefa(1, "Descrição", "pendente")
        assert tarefa["id"] == 1
        assert tarefa["descricao"] == "Descrição"
        assert tarefa["status"] == "pendente"
        self.mock_repository.add.assert_called_once_with(1, tarefa)

    def test_criar_tarefa_descricao_vazia(self):
        """Teste de criação com descrição vazia (deve lançar ValueError)."""
        with pytest.raises(ValueError):
            self.service.criar_tarefa(1, "", "pendente")

    def test_criar_tarefa_status_invalido(self):
        """Teste de criação com status inválido (deve lançar ValueError)."""
        with pytest.raises(ValueError):
            self.service.criar_tarefa(1, "Descrição", "invalido")

    def test_listar_todas(self):
        """Teste de listagem de todas as tarefas."""
        self.mock_repository.get_all.return_value = [
            {"id": 1, "descricao": "Desc1", "status": "pendente"},
            {"id": 2, "descricao": "Desc2", "status": "concluída"}
        ]
        tarefas = self.service.listar_todas()
        assert len(tarefas) == 2
        self.mock_repository.get_all.assert_called_once()

    def test_atualizar_status_valido(self):
        """Teste de atualização de status válido."""
        tarefa_existente = {"id": 1, "descricao": "Desc", "status": "pendente"}
        self.mock_repository.get.return_value = tarefa_existente
        tarefa_atualizada = self.service.atualizar_status(1, "concluída")
        assert tarefa_atualizada["status"] == "concluída"
        self.mock_repository.get.assert_called_once_with(1)
        self.mock_repository.add.assert_called_once_with(1, tarefa_atualizada)

    def test_atualizar_status_tarefa_nao_encontrada(self):
        """Teste de atualização quando a tarefa não é encontrada (deve lançar ValueError)."""
        self.mock_repository.get.return_value = None
        with pytest.raises(ValueError):
            self.service.atualizar_status(1, "concluída")
        self.mock_repository.get.assert_called_once_with(1)
