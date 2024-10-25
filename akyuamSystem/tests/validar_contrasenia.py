from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

try:

    driver.get("http://127.0.0.1:8000/") 

    time.sleep(2)  
    username_input = driver.find_element(By.NAME, "username") 
    username_input.send_keys("administrador@gmail.com") 
    password_input = driver.find_element(By.NAME, "password") 
    password_input.send_keys("Akyuamprueba1") 

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  
    login_button.click()


    time.sleep(3)  

    print("Título de la página después del inicio de sesión:", driver.title)
    
finally:
    driver.quit()
