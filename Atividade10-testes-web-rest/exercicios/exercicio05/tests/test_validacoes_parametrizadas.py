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

# Parte A: Validação de Email (REST)
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

@pytest.mark.parametrize("email_invalido", emails_invalidos)
def test_validacao_email_api(email_invalido):
    response = requests.post("https://reqres.in/api/register", json={
        "email": email_invalido,
        "password": "senha123"
    })
    assert response.status_code == 400

# Parte B: Validação de Senhas (REST)
senhas_invalidas = [
    ("123", "muito curta"),
    ("semNumero", "sem numero"),
    ("semmaiuscula123", "sem maiuscula"),
    ("12345678", "so numeros"),
    ("ab", "muito curta")
]

@pytest.mark.parametrize("senha,motivo", senhas_invalidas)
def test_validacao_senha(senha, motivo):
    response = requests.post("https://reqres.in/api/register", json={
        "email": "test@test.com",
        "password": senha
    })
    assert response.status_code == 400