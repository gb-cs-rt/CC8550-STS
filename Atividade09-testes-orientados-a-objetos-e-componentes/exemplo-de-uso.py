"""Demonstração ponta a ponta do gerenciador de tarefas."""

from datetime import datetime, timedelta
from subprocess import CalledProcessError, run
from unittest.mock import Mock

from task_manager.repository import TaskRepository
from task_manager.service import TaskService
from task_manager.storage import InMemoryStorage
from task_manager.task import Priority, RecurringTask, Status, Task


def print_header(titulo: str):
    print("\n" + "=" * len(titulo))
    print(titulo)
    print("=" * len(titulo))


def mostrar_tarefas(origem: str, tarefas: list[Task]):
    print(f"\n{origem}:")
    if not tarefas:
        print("- Nenhuma tarefa cadastrada.")
        return
    for tarefa in tarefas:
        tipo = tarefa.__class__.__name__
        frequencia = getattr(tarefa, "frequencia_dias", "-")
        print(
            f"- [{tipo}] #{tarefa.id} {tarefa.titulo} | prioridade={tarefa.prioridade.name} "
            f"status={tarefa.status.value} frequencia={frequencia}"
        )


def fluxo_real():
    """Executa o fluxo real usando storage, repositorio e serviço verdadeiros."""
    print_header("Fluxo real com TaskService + TaskRepository + InMemoryStorage")
    storage = InMemoryStorage()
    repository = TaskRepository(storage)
    service = TaskService(repository)

    prazo_estudar = datetime.now() + timedelta(days=3)
    prazo_ler = datetime.now() + timedelta(days=5)

    tarefa1 = service.criar_tarefa(
        titulo="Estudar testes",
        descricao="Revisar mocks e fixtures",
        prioridade=Priority.ALTA,
        prazo=prazo_estudar,
    )
    tarefa2 = service.criar_tarefa(
        titulo="Ler documentação",
        descricao="Explorar pytest e plugins",
        prioridade=Priority.MEDIA,
        prazo=prazo_ler,
        status=Status.EM_ANDAMENTO,
    )

    mostrar_tarefas("Após criação via serviço", service.listar_todas())

    atualizada = service.atualizar_status(tarefa1.id, Status.CONCLUIDA)
    print(f"\nStatus da tarefa #{atualizada.id} atualizado para {atualizada.status.value}")

    # Demonstrar uso direto do repositório com uma subclasse polimórfica
    tarefa_recorrente = RecurringTask(
        id=None,
        titulo="Backup semanal",
        descricao="Executar backup do banco de dados",
        prioridade=Priority.BAIXA,
        prazo=datetime.now() + timedelta(days=7),
        frequencia_dias=7,
    )
    tarefa_recorrente.validar()
    repository.save(tarefa_recorrente)
    print(f"\nRecurringTask salva com ID {tarefa_recorrente.id}")

    mostrar_tarefas("Após adicionar tarefa recorrente", service.listar_todas())

    service.remover_tarefa(tarefa2.id)
    mostrar_tarefas(f"Após remover tarefa #{tarefa2.id}", service.listar_todas())


def fluxo_com_mock():
    """Exibe como validar o serviço isoladamente utilizando Mock do repositório."""
    print_header("Fluxo de testes com Mock para o TaskService")

    repository_mock = Mock(spec=TaskRepository)
    service = TaskService(repository_mock)

    prazo_mock = datetime.now() + timedelta(days=2)
    tarefa_salva = Task(
        id=1,
        titulo="Mock Task",
        descricao="Criada em teste",
        prioridade=Priority.MEDIA,
        prazo=prazo_mock,
        status=Status.PENDENTE,
    )

    repository_mock.save.return_value = tarefa_salva
    repository_mock.find_all.return_value = [tarefa_salva]
    repository_mock.find_by_id.return_value = tarefa_salva
    repository_mock.update.return_value = tarefa_salva
    repository_mock.delete.return_value = True

    criada = service.criar_tarefa(
        titulo="Mock Task",
        descricao="Criada em teste",
        prioridade=Priority.MEDIA,
        prazo=prazo_mock,
    )
    print(f"Tarefa criada via mock: #{criada.id} - {criada.titulo}")

    repository_mock.save.assert_called_once()
    args_salvos = repository_mock.save.call_args.args
    print(f"Objeto enviado ao mock.save: {args_salvos[0].__class__.__name__}")

    service.listar_todas()
    repository_mock.find_all.assert_called_once()

    service.atualizar_status(criada.id, Status.CONCLUIDA)
    repository_mock.find_by_id.assert_called_once_with(criada.id)
    repository_mock.update.assert_called_once()
    print("Status atualizado com sucesso utilizando o mock.")

    service.remover_tarefa(criada.id)
    repository_mock.delete.assert_called_once_with(criada.id)
    print("Remoção validada com mock.")


def executar_pytest(args: list[str]):
    """Executa comandos pytest exibindo saída no console."""
    titulo = f"Executando {' '.join(args)}"
    print_header(titulo)
    try:
        run(args, check=True)
    except CalledProcessError as erro:
        print(f"Comando retornou código {erro.returncode}. Consulte a saída acima para detalhes.")


MENU_OPCOES = {
    "1": ("Fluxo real (serviço + repositório + storage)", fluxo_real),
    "2": ("Fluxo com Mock do repositório", fluxo_com_mock),
    "3": ("Executar pytest -v", lambda: executar_pytest(["pytest", "-v"])),
    "4": ("Executar pytest --cov=task_manager", lambda: executar_pytest(["pytest", "--cov=task_manager"])),
    "0": ("Sair", None),
}


def exibir_menu():
    print_header("Menu de demonstrações e testes")
    for chave, (descricao, _) in MENU_OPCOES.items():
        print(f"{chave} - {descricao}")


def main():
    while True:
        exibir_menu()
        escolha = input("\nSelecione uma opção: ").strip()
        if escolha == "0":
            print("\nEncerrando demonstração.")
            break
        acao = MENU_OPCOES.get(escolha)
        if not acao:
            print("Opção inválida. Tente novamente.\n")
            continue
        _, funcao = acao
        funcao()
        input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    main()
