"""
Testes de API REST
"""
import pytest
import requests
from jsonschema import validate, ValidationError


@pytest.mark.api
def test_listar_usuarios(api_base_url):
    """Testa listagem de usuários"""
    response = requests.get(f"{api_base_url}/users")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@pytest.mark.api
def test_buscar_usuario_por_id(api_base_url):
    """Testa busca de usuário específico"""
    user_id = 1
    response = requests.get(f"{api_base_url}/users/{user_id}")
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data
    assert "@" in data["email"]


@pytest.mark.api
def test_buscar_usuario_inexistente(api_base_url):
    """Testa busca de usuário que não existe"""
    response = requests.get(f"{api_base_url}/users/999999")
    
    # JSONPlaceholder retorna 404 ou objeto vazio
    assert response.status_code == 404 or response.json() == {}


@pytest.mark.api
def test_criar_usuario(api_base_url):
    """Testa criação de novo usuário"""
    novo_usuario = {
        "name": "João Silva",
        "email": "joao@exemplo.com",
        "username": "joaosilva"
    }
    
    response = requests.post(f"{api_base_url}/users", json=novo_usuario)
    
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == novo_usuario["name"]


@pytest.mark.api
def test_atualizar_usuario(api_base_url):
    """Testa atualização de usuário"""
    user_id = 1
    dados_atualizados = {
        "name": "Nome Atualizado"
    }
    
    response = requests.patch(
        f"{api_base_url}/users/{user_id}",
        json=dados_atualizados
    )
    
    assert response.status_code == 200
    assert response.json()["name"] == dados_atualizados["name"]


@pytest.mark.api
def test_deletar_usuario(api_base_url):
    """Testa deleção de usuário"""
    user_id = 1
    response = requests.delete(f"{api_base_url}/users/{user_id}")
    
    assert response.status_code == 200


@pytest.mark.api
def test_schema_usuario(api_base_url):
    """Valida schema da resposta"""
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "username": {"type": "string"}
        },
        "required": ["id", "name", "email"]
    }
    
    response = requests.get(f"{api_base_url}/users/1")
    data = response.json()
    
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Schema inválido: {e.message}")


@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_multiplos_usuarios(api_base_url, user_id):
    """Testa busca de múltiplos usuários"""
    response = requests.get(f"{api_base_url}/users/{user_id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.api
def test_listar_posts_de_usuario(api_base_url):
    """Testa listagem de posts de um usuário"""
    user_id = 1
    response = requests.get(f"{api_base_url}/posts?userId={user_id}")
    
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert all(post["userId"] == user_id for post in posts)


@pytest.mark.api
def test_crud_completo(api_base_url):
    """Teste CRUD completo de um recurso
    
    Nota: JSONPlaceholder é uma API fake que não persiste dados.
    Testamos CREATE com ID novo, mas READ/UPDATE/DELETE usam ID existente.
    """
    # CREATE - Cria um novo post (retorna ID fictício)
    novo_post = {
        "title": "Teste de Post",
        "body": "Conteúdo do post de teste",
        "userId": 1
    }
    response = requests.post(f"{api_base_url}/posts", json=novo_post)
    assert response.status_code == 201
    assert "id" in response.json()
    
    # Para READ, UPDATE e DELETE, usamos um ID que existe (1-100)
    post_id_existente = 1
    
    # READ - Buscar post existente
    response = requests.get(f"{api_base_url}/posts/{post_id_existente}")
    assert response.status_code == 200
    assert "title" in response.json()
    assert response.json()["id"] == post_id_existente
    
    # UPDATE - Atualizar post existente
    atualizado = {"title": "Título Atualizado"}
    response = requests.patch(f"{api_base_url}/posts/{post_id_existente}", json=atualizado)
    assert response.status_code == 200
    assert response.json()["title"] == "Título Atualizado"
    
    # DELETE - Deletar post existente (pode retornar 200 ou 404)
    response = requests.delete(f"{api_base_url}/posts/{post_id_existente}")
    assert response.status_code in [200, 404]