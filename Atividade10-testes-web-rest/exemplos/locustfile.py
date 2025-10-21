"""
Testes de carga com Locust
"""
from locust import HttpUser, task, between


class APIUser(HttpUser):
    """Simulação de usuário fazendo requisições na API"""
    
    wait_time = between(1, 3)  # Aguarda entre 1-3 segundos entre tarefas
    host = "https://jsonplaceholder.typicode.com"
    
    @task(3)
    def listar_usuarios(self):
        """Lista usuários (executado 3x mais)"""
        self.client.get("/users")
    
    @task(2)
    def buscar_usuario(self):
        """Busca usuário específico"""
        self.client.get("/users/1")
    
    @task(1)
    def criar_post(self):
        """Cria um post"""
        self.client.post("/posts", json={
            "title": "Teste de Carga",
            "body": "Conteúdo do teste",
            "userId": 1
        })
    
    @task(2)
    def listar_posts(self):
        """Lista posts"""
        self.client.get("/posts")
