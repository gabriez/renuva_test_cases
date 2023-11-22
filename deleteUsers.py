
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from helpers import init_page

### This is for testing the creation and editing of areas

baseUrl = "https://dev.renuva.com.py/login"
driver = init_page(baseUrl)
wait = WebDriverWait(driver, 8)


## Defining variables to keep information

errors_deleting = []

## Login
email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')
email.clear()
password.clear()
email.send_keys('gabriel.torres@gmail.com')
password.send_keys('gt.123456')
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/form/button').click()

## Checking URL changed
def checkUrlChanges(desired_url, url_jump):
    wait.until(lambda driver: driver.current_url == desired_url)
    driver.get(url_jump)
    # driver.find_element(By.ID, 'dropClientes').click()

def deleteUsers(index_deploy = 0, index_delete = 0):
    buttons_deploy = driver.find_elements(By.XPATH, '//*[@class="btn btn-primary listadeudas"]')
        
    next_index_delete = index_delete
    next_index_deploy = index_deploy

    buttons_deploy[index_deploy].click()
    container_delete = driver.find_element(By.XPATH, '//*[@class="listadeudas no-hover"]')
    buttons_trash = container_delete.find_elements(By.CSS_SELECTOR, "[title~='Eliminar']")
    # '//*[@class="fa fa-trash"]//parent::button'
    buttons_trash[index_delete].click()
    # delete = 
    driver.execute_script("arguments[0].click();",wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn btn-primary mt-4"]'))))
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/header/div/div[2]/span[1]")))
        errors_deleting.append(element.text)
        print("errors ===> ", element.text)
        driver.get('https://dev.renuva.com.py/clientes/duplicados')
        if len(buttons_trash) - 1 > next_index_delete:
            deleteUsers(next_index_deploy, next_index_delete + 1)
        else:
            deleteUsers(next_index_deploy + 1)
    except Exception: 
        print('Hola')

checkUrlChanges('https://dev.renuva.com.py/clientes/agenda', 'https://dev.renuva.com.py/clientes/duplicados')
deleteUsers()
print(errors_deleting)