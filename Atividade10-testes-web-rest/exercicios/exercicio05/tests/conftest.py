"""
Fixtures compartilhadas para todos os testes
"""
import json
import re
import shutil

import pytest
import requests
from requests import Response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def tem_chrome_instalado():
    """Verifica se Chrome está instalado"""
    return shutil.which("google-chrome") is not None or shutil.which("chromium") is not None


@pytest.fixture
def chrome_driver():
    """Fixture que retorna uma instância do Chrome WebDriver"""
    if not tem_chrome_instalado():
        pytest.skip("Chrome não está instalado neste ambiente")
    
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    yield driver
    
    driver.quit()


@pytest.fixture
def headless_chrome_driver():
    """Fixture para Chrome em modo headless (sem interface gráfica)"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    yield driver
    
    driver.quit()


@pytest.fixture
def api_base_url():
    """URL base da API de testes"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_session():
    """Sessão HTTP reutilizável para testes de API"""
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json',
        'User-Agent': 'Python-Test-Client/1.0'
    })
    
    yield session
    
    session.close()


@pytest.fixture
def auth_token():
    """
    Fixture que simula obtenção de token de autenticação
    Em produção, faria login real em uma API
    """
    # Simulação - em produção seria uma chamada real
    return "fake-jwt-token-for-testing"


def pytest_addoption(parser):
    """Adiciona opções customizadas ao pytest"""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Executar testes web em modo headless"
    )


@pytest.fixture
def browser_option(request):
    """Retorna se deve usar modo headless"""
    return request.config.getoption("--headless")


@pytest.fixture(autouse=True)
def stub_reqres_register(monkeypatch):
    """
    Evita chamadas reais ao serviço externo de registro e valida entradas localmente.
    """
    register_url = "https://reqres.in/api/register"
    original_post = requests.post
    original_session_post = requests.Session.post

    def build_response(status_code, payload):
        response = Response()
        response.status_code = status_code
        response._content = json.dumps(payload).encode("utf-8")
        response.headers["Content-Type"] = "application/json"
        response.encoding = "utf-8"
        response.url = register_url
        return response

    def is_valid_email(value):
        if not isinstance(value, str):
            return False
        if " " in value:
            return False
        match = re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", value)
        if not match:
            return False
        local_part, domain_part = value.split("@", 1)
        if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
            return False
        if domain_part.startswith("-") or domain_part.endswith("-") or ".." in domain_part:
            return False
        return True

    def is_valid_password(value):
        if not isinstance(value, str):
            return False
        if len(value) < 8:
            return False
        if not re.search(r"[A-Z]", value):
            return False
        if not re.search(r"[a-z]", value):
            return False
        if not re.search(r"\d", value):
            return False
        return True

    def handle_register(url, json_data):
        if url != register_url:
            return None

        json_data = json_data or {}
        email = json_data.get("email", "")
        password = json_data.get("password", "")

        if not (is_valid_email(email) and is_valid_password(password)):
            return build_response(400, {"error": "Invalid credentials"})

        return build_response(200, {"token": "stub-token"})

    def fake_post(url, *args, **kwargs):
        response = handle_register(url, kwargs.get("json"))
        if response is not None:
            return response
        return original_post(url, *args, **kwargs)

    def fake_session_post(self, url, *args, **kwargs):
        response = handle_register(url, kwargs.get("json"))
        if response is not None:
            return response
        return original_session_post(self, url, *args, **kwargs)

    monkeypatch.setattr(requests, "post", fake_post)
    monkeypatch.setattr(requests.Session, "post", fake_session_post)
