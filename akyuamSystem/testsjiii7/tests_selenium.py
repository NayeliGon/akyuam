from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(LiveServerTestCase):

    def setUp(self):
        # Configurar el driver de Chrome
        chrome_options = Options()
        chrome_service = Service(executable_path=r'C:\chromedriver_win32\chromedriver.exe')  # Ruta en formato raw
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
        # Establecer un tiempo de espera implícito (opcional)
        self.driver.implicitly_wait(10)

    def test_login(self):
        # Abrir la URL de la aplicación Django en el servidor de prueba
        self.driver.get(self.live_server_url + '/login/')

        # Esperar a que los elementos del formulario de login estén presentes
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.ID, 'login_button')

        # Rellenar los campos del login y hacer clic
        username_input.send_keys('sheily@gmail.com')
        password_input.send_keys('Akyuamprueba')
        login_button.click()

        # Verificar que el login fue exitoso buscando algo en el dashboard
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Dashboard')]"))
        )

        self.assertIn('Dashboard', self.driver.page_source)

    def tearDown(self):
        # Cerrar el navegador después de la prueba
        self.driver.quit()
