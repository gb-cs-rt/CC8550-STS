from abc import ABC, abstractmethod
from enum import IntEnum
from enum import Enum
from datetime import datetime

class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Status(Enum):
    PENDENTE = "pendente"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"

class BaseTask(ABC):
    def __init__(self, id: int | None, titulo: str, descricao: str, prioridade: Priority, prazo: datetime, status: 'Status' = Status.PENDENTE):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self._status = Status.PENDENTE
        self.status = status

    @property
    def status(self) -> 'Status':
        return self._status

    @status.setter
    def status(self, novo_status: 'Status'):
        if not isinstance(novo_status, Status):
            raise ValueError("Status inválido.")
        self._status = novo_status

    def atualizar_status(self, novo_status: 'Status'):
        self.status = novo_status

    @abstractmethod
    def validar(self):
        """Valida os campos obrigatórios da tarefa."""

class Task(BaseTask):
    def __init__(self, id: int | None, titulo: str, descricao: str, prioridade: Priority, prazo: datetime, status: Status = Status.PENDENTE):
        super().__init__(id, titulo, descricao, prioridade, prazo, status)

    def validar(self):
        if len(self.titulo) < 3:
            raise ValueError("O título deve ter pelo menos 3 caracteres.")
        if self.prazo < datetime.now():
            raise ValueError("O prazo não pode ser uma data passada.")

class RecurringTask(Task):
    def __init__(self, id: int | None, titulo: str, descricao: str, prioridade: Priority, prazo: datetime, frequencia_dias: int, status: Status = Status.PENDENTE):
        super().__init__(id, titulo, descricao, prioridade, prazo, status)
        self.frequencia_dias = frequencia_dias

    def validar(self):
        super().validar()
        if self.frequencia_dias <= 0:
            raise ValueError("A frequencia deve ser um numero inteiro positivo.")
