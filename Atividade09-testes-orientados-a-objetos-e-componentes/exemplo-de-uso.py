from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.storage import InMemoryStorage
from task_manager.repository import TaskRepository
# from task_manager.service import TaskService

# Criar componentes 
storage = InMemoryStorage()
repository = TaskRepository(storage)
# service = TaskService(repository)

# Criar tarefa
prazo = datetime.now() + timedelta(days=5)
task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
task.validar()

# Salvar 
task_salva = repository.save(task)
print(f"ID da tarefa salva: {task_salva.id}")

# Buscar
encontrada = repository.find_by_id(1)
print(f"Titulo da tarefa encontrada: {encontrada.titulo}, Prioridade: {encontrada.prioridade.name}")

# Listar todas
todas = repository.find_all()
print(f"Número total de tarefas: {len(todas)}")