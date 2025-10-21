"""
Testes para a API de Produtos Rest.
"""
import pytest
import requests
from jsonschema import validate, ValidationError

BASE_URL = "https://fakestoreapi.com"

@pytest.mark.api
def test_listar_todos_os_produtos():
    """Teste para listar todos os produtos."""

    # Fazer requisição GET 
    response = requests.get(f"{BASE_URL}/products")

    # Verificar status code
    assert response.status_code == 200, f"Status code : {response.status_code}"

    # Verificar estrutura dos dados
    assert isinstance(response.json(), list), "Resposta não é uma lista"
    assert len(response.json()) > 0, "Nenhum produto encontrado"
    assert "id" in response.json()[0], "Campo 'id' não encontrado no produto"
    assert "title" in response.json()[0], "Campo 'title' não encontrado no produto"
    assert "price" in response.json()[0], "Campo 'price' não encontrado no produto"
    assert "description" in response.json()[0], "Campo 'description' não encontrado no produto"
    assert "category" in response.json()[0], "Campo 'category' não encontrado no produto"
    assert "image" in response.json()[0], "Campo 'image' não encontrado no produto"
    assert "rating" in response.json()[0], "Campo 'rating' não encontrado no produto"
    print("Estrutura JSON válida para todos os produtos.")

    # Verificar valores

    for product in response.json():
        assert product["id"] > 0, f"ID inválido para o produto: {product}"
        assert product["title"], f"Título vazio para o produto: {product}"
        assert product["price"] >= 0, f"Preço inválido para o produto: {product}"
        assert product["description"], f"Descrição vazia para o produto: {product}"
        assert product["category"], f"Categoria vazia para o produto: {product}"
        assert product["image"], f"Imagem vazia para o produto: {product}"
        assert product["rating"]["rate"] >= 0, f"Rating inválido para o produto: {product}"
        assert product["rating"]["count"] >= 0, f"Count inválido para o produto: {product}"
    print("Todos os produtos possuem valores válidos.")

    print(f"Total de produtos encontrados: {len(response.json())}")
    print(f"Primeiro produto: {response.json()[0] ['title']}")

    print("\nTeste passou!")

@pytest.mark.api
def test_buscar_produtos_por_id():
    """Teste para buscar produtos por ID."""

    # Fazer requisição GET
    response = requests.get(f"{BASE_URL}/products")

    # Verificar status code
    assert response.status_code == 200, f"Status code : {response.status_code}"

    # Verificar cada produto por ID
    for product in response.json():
        product_id = product["id"]
        product_response = requests.get(f"{BASE_URL}/products/{product_id}")
        assert product_response.status_code == 200, f"Status code : {product_response.status_code} para o produto ID: {product_id}"
        product_data = product_response.json()
        assert product_data["id"] == product_id, f"ID do produto não corresponde para o produto ID: {product_id}"
    print("Todos os produtos foram buscados com sucesso por ID.")

    print("\nTeste passou!")

@pytest.mark.api
def test_filtrar_produtos_por_categoria():
    """Teste para filtrar produtos por categoria."""

    # Fazer requisição GET
    response = requests.get(f"{BASE_URL}/products")

    # Verificar status code
    assert response.status_code == 200, f"Status code : {response.status_code}"

    # Verificar categorias disponíveis
    categories_response = requests.get(f"{BASE_URL}/products/categories")
    assert categories_response.status_code == 200, f"Status code : {categories_response.status_code}"
    categories = categories_response.json()
    assert len(categories) > 0, "Nenhuma categoria encontrada"
    assert "electronics" in categories, "Categoria 'electronics' não encontrada"
    assert "jewelery" in categories, "Categoria 'jewelery' não encontrada"
    assert "men's clothing" in categories, "Categoria 'men's clothing' não encontrada"
    assert "women's clothing" in categories, "Categoria 'women's clothing' não encontrada"
    print("Categorias válidas encontradas.")

    # Verificar produtos por categoria
    for category in categories:
        category_response = requests.get(f"{BASE_URL}/products/category/{category}")
        assert category_response.status_code == 200, f"Status code : {category_response.status_code} para a categoria: {category}"
        products_in_category = category_response.json()
        assert len(products_in_category) > 0, f"Nenhum produto encontrado na categoria: {category}"
        for product in products_in_category:
            assert product["category"] == category, f"Produto com categoria incorreta encontrado: {product}"
    print("Todos os produtos foram filtrados com sucesso por categoria.")

    print("\nTeste passou!")

@pytest.mark.api
def test_validar_schema_da_resposta():
    """Teste para validar o schema da resposta."""

    # Definir o schema esperado
    product_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "price": {"type": "number"},
            "description": {"type": "string"},
            "category": {"type": "string"},
            "image": {"type": "string"},
            "rating": {
                "type": "object",
                "properties": {
                    "rate": {"type": "number"},
                    "count": {"type": "integer"}
                },
                "required": ["rate", "count"]
            }
        },
        "required": ["id", "title", "price", "description", "category", "image", "rating"]
    }

    # Fazer requisição GET
    response = requests.get(f"{BASE_URL}/products")

    # Verificar status code
    assert response.status_code == 200, f"Status code : {response.status_code}"


    # Validar schema de cada produto
    for product in response.json():
        try:
            validate(instance=product, schema=product_schema)
        except ValidationError as e:
            pytest.fail(f"Schema inválido para o produto ID: {product['id']}. Erro: {e.message}")
    print("Schema válido para todos os produtos.")

    print("\nTeste passou!")

@pytest.mark.api
def test_limite_de_produtos_retornados():
    """Teste para verificar o limite de produtos retornados."""

    # Fazer requisição GET
    response = requests.get(f"{BASE_URL}/products")

    # Verificar status code
    assert response.status_code == 200, f"Status code : {response.status_code}"

    # Verificar limite de produtos
    max_limit = 20  # Definir um limite máximo esperado

    # Verificar se o número de produtos retornados não excede o limite
    assert len(response.json()) <= max_limit, f"Número de produtos retornados excede o limite de {max_limit}"
    print(f"Número de produtos retornados está dentro do limite de {max_limit}.")

    print("\nTeste passou!")

if __name__ == "__main__":
    test_listar_todos_os_produtos()
    test_buscar_produtos_por_id()
    test_filtrar_produtos_por_categoria()
    test_validar_schema_da_resposta()
    test_limite_de_produtos_retornados()
