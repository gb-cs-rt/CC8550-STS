"""
Cliente para API de Usuários
"""
import requests


class UsersAPI:
    """Cliente para interagir com API de usuários"""
    
    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.session = session or requests.Session()
        self.endpoint = f"{base_url}/users"
    
    def listar_usuarios(self):
        """Lista todos os usuários"""
        response = self.session.get(self.endpoint)
        response.raise_for_status()
        return response.json()
    
    def buscar_usuario(self, user_id):
        """Busca um usuário por ID"""
        response = self.session.get(f"{self.endpoint}/{user_id}")
        response.raise_for_status()
        return response.json()
    
    def criar_usuario(self, dados):
        """Cria um novo usuário"""
        response = self.session.post(self.endpoint, json=dados)
        response.raise_for_status()
        return response.json()
    
    def atualizar_usuario(self, user_id, dados):
        """Atualiza um usuário"""
        response = self.session.patch(f"{self.endpoint}/{user_id}", json=dados)
        response.raise_for_status()
        return response.json()
    
    def deletar_usuario(self, user_id):
        """Deleta um usuário"""
        response = self.session.delete(f"{self.endpoint}/{user_id}")
        response.raise_for_status()
        return response.status_code == 200
    
    def buscar_posts_usuario(self, user_id):
        """Busca posts de um usuário"""
        response = self.session.get(f"{self.base_url}/posts?userId={user_id}")
        response.raise_for_status()
        return response.json()
    