"""
Testes de Integração
"""
import pytest
import requests


@pytest.mark.integration
def test_integracao_usuario_posts(api_base_url):
    """Testa integração entre usuários e seus posts"""
    # Buscar usuário
    user_response = requests.get(f"{api_base_url}/users/1")
    assert user_response.status_code == 200
    user = user_response.json()
    
    # Buscar posts do usuário
    posts_response = requests.get(f"{api_base_url}/posts?userId={user['id']}")
    assert posts_response.status_code == 200
    posts = posts_response.json()
    
    # Verificar integridade
    assert len(posts) > 0
    assert all(post["userId"] == user["id"] for post in posts)


@pytest.mark.integration
def test_integracao_post_comentarios(api_base_url):
    """Testa integração entre posts e comentários"""
    post_id = 1
    
    # Buscar post
    post_response = requests.get(f"{api_base_url}/posts/{post_id}")
    assert post_response.status_code == 200
    
    # Buscar comentários do post
    comments_response = requests.get(f"{api_base_url}/posts/{post_id}/comments")
    assert comments_response.status_code == 200
    comments = comments_response.json()
    
    # Verificar integridade
    assert len(comments) > 0
    assert all(comment["postId"] == post_id for comment in comments)
    