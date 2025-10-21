"""
Test para o módulo de login utilizando Page Object Model (POM).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

"""
Refatore os testes do Exercício 1 usando Page Object Model.
"""

def wait_for_error_message(driver, expected_text, timeout=20):
    WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element((By.ID, "error"), expected_text)
    )
    return driver.find_element(By.ID, "error")

@pytest.mark.web
def test_login_credenciais_validas():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("student", "Password123")

        dashboard_page = DashboardPage(driver)
        assert dashboard_page.is_loaded()
        print("Login realizado com sucesso!")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_email_invalido():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("incorrectUser", "Password123")

        error_message = wait_for_error_message(driver, "Your username is invalid!")
        assert "Your username is invalid!" in error_message.text
        print("Login nao realizado: email inválido.")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_senha_invalida():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("student", "incorrectPassword")

        error_message = wait_for_error_message(driver, "Your password is invalid!")
        assert "Your password is invalid!" in error_message.text
        print("Login nao realizado: senha inválida.")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_credenciais_vazias():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("", "")

        error_message = wait_for_error_message(driver, "Your username is invalid!")
        assert "Your username is invalid!" in error_message.text
        print("Login nao realizado: credenciais vazias.")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_verificar_mensagens_erro_apropriadas():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login_page = LoginPage(driver)
        login_page.load()
        
        # Testar email inválido
        login_page.login("incorrectUser", "Password123")

        error_message = wait_for_error_message(driver, "Your username is invalid!")
        assert "Your username is invalid!" in error_message.text
        print("Mensagem de erro apropriada para email inválido verificada.")

        login_page.load()

        # Testar senha inválida
        login_page.login("student", "incorrectPassword")

        error_message = wait_for_error_message(driver, "Your password is invalid!")
        assert "Your password is invalid!" in error_message.text
        print("Mensagem de erro apropriada para senha inválida verificada.")

        login_page.load()

        # Testar credenciais vazias
        login_page.login("", "")

        error_message = wait_for_error_message(driver, "Your username is invalid!")
        assert "Your username is invalid!" in error_message.text
        print("Mensagem de erro apropriada para credenciais vazias verificada.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_credenciais_validas()
    test_login_email_invalido()
    test_login_senha_invalida()
    test_login_credenciais_vazias()
    test_login_verificar_mensagens_erro_apropriadas()