import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.registroPage import RegistrationPage
from utils.user_data_utils import save_user_data
from utils.url_proyecto import url
class RegisterTest(unittest.TestCase):

    def setUp(self):
        """Parametros necesarios para ejecutar el test
        """
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = WebDriver(options=options)

    def test_register_process(self):
        driver = self.driver
        driver.get(url)
        registration_page = RegistrationPage(driver)

        # Navegar al formulario de registro
        registration_page.navigate_to_registration()

        # Rellenar el formulario
        user='Roberto'
        email='Roberto_a@example.com'
        password='3434565698thg'
        registration_page.enter_name(user)
        registration_page.enter_email(email)
        registration_page.enter_password(password)
        registration_page.enter_confirm_password(password)

        # Enviar el formulario
        registration_page.click_register()
        
        # Errores
        if "The password must be at least 8 characters." in registration_page.message_pass():
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales, la contraseña tiene menos de 8 caracteres")
            
        if "The email has already been taken." in registration_page.message_email():
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales, el email ya esta en uso.")

        save_user_data(user,email,password) #Se guardaran los registros en un json
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()