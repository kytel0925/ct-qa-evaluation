import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.loginPage import LoginPage
from utils.url_proyecto import url

class LoginFaileTest(unittest.TestCase):

    def setUp(self):
        """Parametros necesarios para ejecutar el test
        """
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = WebDriver(options=options)

    def test_login_faile_process(self):
        self.driver.get(url) # Navegar a la URL
        login_page = LoginPage(self.driver) # Crear una instancia de LoginPage
        
        email = 'example_faile@example.com'
        password = 'failefaile123123'
        
        login_page.click_login()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_save_login()
        
        if "These credentials do not match our records." in login_page.message():
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()