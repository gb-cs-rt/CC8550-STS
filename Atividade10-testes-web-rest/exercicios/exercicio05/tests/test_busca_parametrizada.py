""""
Testes Parametrizados (REST + Web)
Crie testes parametrizados para validar múltiplos cenários de entrada.

Parte A: Validação de Email (REST)
Cenários de email inválido:

emails_invalidos = [
    "sem-arroba.com",
    "@sem-usuario.com",
    "sem-dominio@",
    "espacos no meio@teste.com",
    "caracteres!especiais@teste.com",
    "..pontos@teste.com",
    "teste@",
    "@teste.com"
]
Implementação com pytest:

@pytest.mark.parametrize("email_invalido", emails_invalidos)
def test_validacao_email_api(email_invalido):
    response = requests.post("https://reqres.in/api/register", json={
        "email": email_invalido,
        "password": "senha123"
    })
    assert response.status_code == 400
Parte B: Validação de Senhas (REST)
Cenários de senha inválida:

senhas_invalidas = [
    ("123", "muito curta"),
    ("semNumero", "sem número"),
    ("semmaiuscula123", "sem maiúscula"),
    ("12345678", "só números"),
    ("ab", "muito curta")
]
Implementação:

@pytest.mark.parametrize("senha,motivo", senhas_invalidas)
def test_validacao_senha(senha, motivo):
    response = requests.post("https://reqres.in/api/register", json={
        "email": "test@test.com",
        "password": senha
    })
    assert response.status_code == 400
Parte C: Busca Parametrizada (Web)
Testar busca com múltiplos termos:

@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_google(chrome_driver, termo_busca):
    driver = chrome_driver
    driver.get("https://www.google.com")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(termo_busca)
    search_box.submit()
    
    # Aguardar resultados
    time.sleep(2)
    
    assert termo_busca.lower() in driver.page_source.lower()
Estrutura esperada:
tests/
├── test_validacoes_parametrizadas.py
└── test_busca_parametrizada.py
"""

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pages.google_page import GooglePage


# Parte C: Busca Parametrizada (Web)

@pytest.mark.web
@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_multiplos_termos(chrome_driver, termo_busca):
        """Testa busca com múltiplos termos"""
        google_page = GooglePage(chrome_driver)
        google_page.abrir()
        google_page.buscar(termo_busca)

        assert google_page.tem_resultados()

