"""
Página do Dashboard após login bem-sucedido.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .base_page import BasePage

class DashboardPage(BasePage):
    SUCCESS_MESSAGE = (By.CLASS_NAME, "post-title")
    SUCCESS_URL_FRAGMENT = "/logged-in-successfully/"

    def esta_logado(self): # Retorna True/False
        return self.is_loaded()

    def obter_mensagem_boas_vindas(self):
        return self.obter_texto(self.SUCCESS_MESSAGE)

    def is_loaded(self):
        """Confirma se o dashboard foi carregado após o login."""
        url_ok = self.SUCCESS_URL_FRAGMENT in self.driver.current_url
        return url_ok and self.elemento_visivel(self.SUCCESS_MESSAGE)
