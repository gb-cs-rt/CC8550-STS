"""
Classe base para Page Objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Classe base com métodos comuns para todas as páginas"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def abrir_url(self, url):
        """Abre uma URL"""
        self.driver.get(url)
    
    def encontrar_elemento(self, locator):
        """Encontra um elemento na página"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def encontrar_elementos(self, locator):
        """Encontra múltiplos elementos na página"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def clicar(self, locator):
        """Clica em um elemento"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def digitar(self, locator, texto):
        """Digita texto em um campo"""
        element = self.encontrar_elemento(locator)
        element.clear()
        element.send_keys(texto)
    
    def obter_texto(self, locator):
        """Obtém texto de um elemento"""
        element = self.encontrar_elemento(locator)
        return element.text
    
    def elemento_visivel(self, locator):
        """Verifica se elemento está visível"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
