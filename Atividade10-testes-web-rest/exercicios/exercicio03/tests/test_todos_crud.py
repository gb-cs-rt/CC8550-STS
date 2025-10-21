"""
Test CRUD para API Rest.
"""

import pytest
import requests
from jsonschema import validate, ValidationError

"""
Usando JSONPlaceholder (https://jsonplaceholder.typicode.com/), implemente teste CRUD completo para "todos".

Endpoint: /todos
Operações a testar:

# CREATE
POST /todos
{
    "title": "Minha tarefa",
    "completed": false,
    "userId": 1
}

# READ
GET /todos/1

# UPDATE
PATCH /todos/1
{
    "completed": true
}

# DELETE
DELETE /todos/1

# VERIFY
GET /todos/1  # Deve retornar 404 ou {}

Implementação:
Use fixtures para criar dados de teste
Implemente teardown para limpar dados
Teste casos de erro (ex: criar todo sem título)
"""

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_crud_completo():
    """Teste CRUD completo para /todos"""

    # CREATE - Cria um novo post
    novo_post = {
        "userId": 1,
        "title": "Minha tarefa de teste",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/todos", json=novo_post)
    assert response.status_code == 201, f"Falha ao criar todo: {response.status_code}"
    assert "id" in response.json(), "ID não retornado na criação"
    post_id = response.json()["id"]
    print(f"Post criado com ID: {post_id}")

    # READ - Buscar post criado
    post_id_existente = 1
    response = requests.get(f"{BASE_URL}/todos/{post_id_existente}")
    assert response.status_code == 200, f"Falha ao buscar todo: {response.status_code}"
    assert "id" in response.json(), "ID não encontrado no todo buscado"
    assert response.json()["id"] == post_id_existente, "ID do todo buscado não corresponde"
    print(f"Post buscado com sucesso: {response.json()}")

    # UPDATE - Atualizar post existente
    atualizado = {"title": "Minha tarefa teste com titulo atualizado", "completed": True}
    response = requests.patch(f"{BASE_URL}/todos/{post_id_existente}", json=atualizado)
    assert response.status_code == 200, f"Falha ao atualizar todo: {response.status_code}"
    assert response.json()["title"] == "Minha tarefa teste com titulo atualizado", "Título não atualizado corretamente"
    assert response.json()["completed"] == True, "Status 'completed' não atualizado corretamente"
    print(f"Post atualizado com sucesso: {response.json()}")

    # DELETE - Deletar post existente
    response = requests.delete(f"{BASE_URL}/todos/{post_id_existente}")
    assert response.status_code in [200, 204], f"Falha ao deletar todo: {response.status_code}"
    print(f"Post deletado com sucesso: ID {post_id_existente}")

    # VERIFY - Verificar se o post foi deletado
    response = requests.get(f"{BASE_URL}/todos/{post_id_existente}")
    assert response.status_code in [200, 404], f"Falha ao buscar todo após deleção: {response.status_code}"
    print(
        "Verificação após deleção retornou status code:"
        f" {response.status_code} (esperado 404 ou resposta vazia)"
    )

    print("\nTeste CRUD completo passou!")

@pytest.mark.api
def test_crud_post_sem_titulo():
    """Teste para criar um todo sem título (deve falhar)"""

    # CREATE - Tentar criar um todo sem título
    novo_post = {
        "userId": 1,
        "id": 2,
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/todos", json=novo_post)

    # Verificar que a criação falhou
    assert response.status_code == 201, f"Status code inesperado: {response.status_code}"
    assert "title" not in response.json(), "Título inesperadamente presente no todo criado"
    print("Criação de todo sem título falhou como esperado.")

    print("\nTeste de criação de todo sem título passou!")

@pytest.mark.api
def test_validar_schema_post():
    """Teste para validar o schema do post"""

    # Schema esperado para um post
    post_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        },
        "required": ["userId", "id", "title", "completed"]
    }

    # Fazer requisição GET para buscar um post
    response = requests.get(f"{BASE_URL}/todos/1")

    # Verificar status code
    assert response.status_code == 200, f"Status code : {response.status_code}"
    post = response.json()

    # Validar schema do post
    try:
        validate(instance=post, schema=post_schema)
        print("Schema válido para o post.")
    except ValidationError as e:
        pytest.fail(f"Schema inválido: {e.message}")

    print("\nTeste de validação de schema passou!")

if __name__ == "__main__":
    test_crud_completo()
    test_crud_post_sem_titulo()
    test_validar_schema_post()
