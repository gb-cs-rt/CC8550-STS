"""Gerencia persistência das tarefas."""

from task_manager.storage import InMemoryStorage
from task_manager.task import Task

class TaskRepository:
    def __init__(self, storage: InMemoryStorage):
        self.storage = storage
        self._next_id = 1

    def save(self, task: Task) -> Task:
        if task.id is None:
            task.id = self._next_id
            self._next_id += 1
        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id: int) -> Task | None:
        return self.storage.get(id)

    def find_all(self) -> list[Task]:
        return self.storage.get_all()

    def delete(self, id: int) -> bool:
        return self.storage.delete(id)