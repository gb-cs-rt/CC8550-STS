from datetime import datetime, timedelta
from task_manager.storage import InMemoryStorage
from task_manager.repository import TaskRepository
from task_manager.service import TaskService
from task_manager.task import Priority, Status

# Criar componentes
storage = InMemoryStorage()
repository = TaskRepository(storage)
service = TaskService(repository)

# Criar e salvar tarefa via serviço
prazo = datetime.now() + timedelta(days=5)
tarefa_criada = service.criar_tarefa(
    titulo="Estudar",
    descricao="Python",
    prioridade=Priority.ALTA,
    prazo=prazo,
)
print(f"ID da tarefa salva: {tarefa_criada.id}")

# Buscar todas as tarefas
todas = service.listar_todas()
print(f"Número total de tarefas: {len(todas)}")

# Atualizar status
atualizada = service.atualizar_status(tarefa_criada.id, Status.CONCLUIDA)
print(f"Status atualizado: {atualizada.status.name}")

# Remover tarefa
removida = service.remover_tarefa(tarefa_criada.id)
print(f"Tarefa removida: {removida}")
