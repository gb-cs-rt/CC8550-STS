"""Testes para o gerenciador de tarefas."""

import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

class TestTask:
    """Testes para a classe Task."""

    def setup_method(self):
        """Configuração antes de cada método de teste."""
        self.task = Task(id=None, titulo="Tarefa de Teste", descricao="Descrição da tarefa de teste", prioridade=Priority.MEDIA, prazo=datetime.now() + timedelta(days=1))

    def test_criacao_valida(self):
        """Teste de criação válida de uma tarefa."""
        prazo = datetime.now() + timedelta(days=1)
        task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
        task.validar()  # NAO DEVE LANCAR ERRO
        assert task.titulo == "Estudar"

    def test_titulo_invalido(self):
        """Teste de título inválido (deve lançar ValueError)."""
        prazo = datetime.now() + timedelta(days=1)
        task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
        with pytest.raises(ValueError):
            task.validar()

    def test_prazo_no_passado(self):
        """Teste de prazo no passado (deve lançar ValueError)."""
        prazo = datetime.now() - timedelta(days=1)
        task = Task(None, "Tarefa", "Desc", Priority.MEDIA, prazo)
        with pytest.raises(ValueError):
            task.validar()  