from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def wait_for_error_message(driver, expected_text, timeout=20):
    WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element((By.ID, "error"), expected_text)
    )
    return driver.find_element(By.ID, "error")


@pytest.mark.web
def test_login_credenciais_validas():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        WebDriverWait(driver, 20).until(EC.url_contains("/logged-in-successfully/"))

        assert "/logged-in-successfully/" in driver.current_url

        sucess_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "post-title")))
        assert "Logged In Successfully" in sucess_message.text
        print("Login realizado com sucesso!")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_email_invalido():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("incorrectUser")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        error_message = wait_for_error_message(driver, "Your username is invalid!")
        assert "Your username is invalid!" in error_message.text
        print("Login nao realizado: email inválido.")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_senha_invalida():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("incorrectPassword")
        driver.find_element(By.ID, "submit").click()

        error_message = wait_for_error_message(driver, "Your password is invalid!")
        assert "Your password is invalid!" in error_message.text
        print("Login nao realizado: senha inválida.")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_credenciais_vazias():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "submit").click()

        error_message = wait_for_error_message(driver, "Your username is invalid!")
        assert "Your username is invalid!" in error_message.text
        print("Login nao realizado: credenciais vazias.")
    finally:
        driver.quit()

@pytest.mark.web
def test_login_verificar_mensagens_erro_apropriadas():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        
        # Testar email inválido
        driver.find_element(By.ID, "username").send_keys("incorrectUser")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        error_message = wait_for_error_message(driver, "Your username is invalid!")
        assert "Your username is invalid!" in error_message.text
        print("Mensagem de erro apropriada para email inválido verificada.")

        driver.refresh()

        # Testar senha inválida
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("incorrectPassword")
        driver.find_element(By.ID, "submit").click()

        error_message = wait_for_error_message(driver, "Your password is invalid!")
        assert "Your password is invalid!" in error_message.text
        print("Mensagem de erro apropriada para senha inválida verificada.")

        driver.refresh()

        # Testar credenciais vazias
        driver.find_element(By.ID, "submit").click()

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
