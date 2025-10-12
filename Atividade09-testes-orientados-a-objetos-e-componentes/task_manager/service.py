"""Serviço para gerenciar tarefas."""

class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def criar_tarefa(self, id, descricao, status):
        if not descricao:
            raise ValueError("Descrição não pode ser vazia")
        if status not in ["pendente", "em andamento", "concluída"]:
            raise ValueError("Status inválido")
        tarefa = {"id": id, "descricao": descricao, "status": status}
        self.repository.add(id, tarefa)
        return tarefa

    def listar_todas(self):
        return self.repository.get_all()

    def atualizar_status(self, id, status):
        tarefa = self.repository.get(id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada")
        if status not in ["pendente", "em andamento", "concluída"]:
            raise ValueError("Status inválido")
        tarefa["status"] = status
        self.repository.add(id, tarefa)
        return tarefa

    def remover_tarefa(self, id):
        return self.repository.remove(id)
