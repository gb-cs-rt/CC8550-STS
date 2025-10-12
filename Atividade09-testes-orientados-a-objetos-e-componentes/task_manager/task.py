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

class Task:
    def __init__(self, id: int | None, titulo: str, descricao: str, prioridade: Priority, prazo: datetime, status: Status = Status.PENDENTE):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status

    def validar(self):
        if len(self.titulo) < 3:
            raise ValueError("O título deve ter pelo menos 3 caracteres.")
        if self.prazo < datetime.now():
            raise ValueError("O prazo não pode ser uma data passada.")

    def atualizar_status(self, novo_status: Status):
        if not isinstance(novo_status, Status):
            raise ValueError("Status inválido.")
        self.status = novo_status
