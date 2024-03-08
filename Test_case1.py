import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.implicitly_wait(10)

#Creacion de una funcion para la verificacion de la existencia de un elemento mediante XPATH

def check_existance_byXPATH(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


#Test para realizar busqueda en searchbar y verificar despliegue de resultado asociado a termino de busqueda
def test_search():
    driver.maximize_window()
    driver.get("https://motorcredito.com.do/")
    searchbttn = driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/div[2]/button")
    searchbttn.click()
    searchbar = driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/div[2]/ul/li/form/input")
    searchbar.send_keys("sucursal", Keys.RETURN)
    assert check_existance_byXPATH("//*[@id='content']/div/div/div[1]/ol/li[1]"), "Elemento no encontrado"
    driver.quit()

