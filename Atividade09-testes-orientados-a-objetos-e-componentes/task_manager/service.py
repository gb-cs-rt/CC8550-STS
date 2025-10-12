"""Classe TaskService
Atributo:
• repository: TaskRepository (recebe no construtor)
Métodos:
• criar_tarefa(...): Cria, valida e salva
• listar_todas(): Retorna todas
• atualizar_status(id, status): Atualiza status"""

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