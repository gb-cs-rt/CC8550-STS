"""
Página de login com métodos para interagir com a página de login.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")

    def load(self):
        """Abre a página de login padrão."""
        self.abrir_url(self.URL)

    def abrir(self, url):
        self.abrir_url(url)

    def preencher_email(self, email):
        self.digitar(self.EMAIL_INPUT, email)

    def preencher_senha(self, senha):
        self.digitar(self.PASSWORD_INPUT, senha)

    def clicar_login(self):
        self.clicar(self.LOGIN_BUTTON)

    def fazer_login(self, username, password):
        self.digitar(self.EMAIL_INPUT, username)
        self.digitar(self.PASSWORD_INPUT, password)
        self.clicar(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Alias em inglês para compatibilidade com os testes."""
        self.fazer_login(username, password)
