"""Gerencia persistência das tarefas."""

from task_manager.storage import InMemoryStorage
from task_manager.task import Task

class TaskRepository:
    def __init__(self, storage: InMemoryStorage):
        self.storage = storage
        self._next_id = 1

    def save(self, task: Task) -> Task:
        if task.id is not None:
            raise ValueError("A tarefa já possui um ID atribuído.")
        task.id = self._next_id
        self._next_id += 1
        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id: int) -> Task | None:
        return self.storage.get(id)

    def find_all(self) -> list[Task]:
        return self.storage.get_all()

    def update(self, task: Task) -> Task:
        if task.id is None:
            raise ValueError("Não é possível atualizar uma tarefa sem ID.")
        self.storage.update(task.id, task)
        return task

    def delete(self, id: int) -> bool:
        return self.storage.remove(id)
