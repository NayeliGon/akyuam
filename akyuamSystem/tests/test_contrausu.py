from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://127.0.0.1:8000/") 

    time.sleep(2)  # Espera a que la página cargue

    # Ingreso de credenciales
    username_input = driver.find_element(By.NAME, "username") 
    username_input.send_keys("akyuam.cejav@yahoo.es") 
    password_input = driver.find_element(By.NAME, "password") 
    password_input.send_keys("akYu4m1021") 

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  
    login_button.click()

    time.sleep(3)  # Espera a que la página de inicio se cargue
    print("Título de la página después del inicio de sesión:", driver.title)

    # Selecciona "Administrador de Usuarios"
    admin_users_option = driver.find_element(By.XPATH, "//a[contains(@class, 'menu-item')]/p[text()='Administrar usuarios']")
    admin_users_option.click()

    time.sleep(3)  # Espera a que la página de Administrador de Usuarios cargue
    print("Título de la página de Administrador de Usuarios:", driver.title)

    # Espera a que el formulario de registro esté presente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "nombre"))  # Cambia "nombre" si es necesario
    )

    # Llenar el formulario de registro
    nombre_input = driver.find_element(By.NAME, "nombre")
    nombre_input.send_keys("NombrePrueba")

    apellido_input = driver.find_element(By.NAME, "apellido")
    apellido_input.send_keys("ApellidoPrueba")

    correo_input = driver.find_element(By.NAME, "correo")
    correo_input.send_keys("correo.prueba@example.com")

    contrasena_input = driver.find_element(By.NAME, "contraseña")
    contrasena_input.send_keys("1234")

    # Seleccionar el nivel de usuario usando Select
    nivel_usuario_select = Select(driver.find_element(By.NAME, "nivel-usuario"))
    nivel_usuario_select.select_by_value("1")  # Cambia "1" por el valor correspondiente al nivel de usuario que deseas

    # Hacer clic en el botón de registro
    registrar_button = driver.find_element(By.CLASS_NAME, "submit-btn")  # Selecciona el botón por su clase
    registrar_button.click()

    time.sleep(3)  # Espera a que el registro se complete
    print("Registro completado. Título de la página actual:", driver.title)

finally:
    driver.quit()
