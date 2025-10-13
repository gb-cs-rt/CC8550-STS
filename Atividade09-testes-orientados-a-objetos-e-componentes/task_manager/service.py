"""Serviço para gerenciar tarefas."""

from datetime import datetime
from task_manager.repository import TaskRepository
from task_manager.task import Task, Priority, Status

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def criar_tarefa(
        self,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
        status: Status = Status.PENDENTE,
    ) -> Task:
        if not isinstance(prioridade, Priority):
            raise ValueError("Prioridade inválida")
        if not titulo:
            raise ValueError("Título não pode ser vazio")
        if not isinstance(status, Status):
            raise ValueError("Status inválido")
        nova_tarefa = Task(
            id=None,
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            prazo=prazo,
            status=status,
        )
        nova_tarefa.validar()
        return self.repository.save(nova_tarefa)

    def listar_todas(self) -> list[Task]:
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Task:
        if not isinstance(status, Status):
            raise ValueError("Status inválido")
        tarefa = self.repository.find_by_id(id)
        if tarefa is None:
            raise ValueError("Tarefa não encontrada")
        tarefa.atualizar_status(status)
        return self.repository.update(tarefa)

    def remover_tarefa(self, id: int) -> bool:
        return self.repository.delete(id)
