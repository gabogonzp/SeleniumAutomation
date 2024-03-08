import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.implicitly_wait(10)

#Creacion de una funcion para la verificacion de la existencia de un elemento mediante XPATH

def check_nonexistance_byXPATH(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

#Test para realizar busqueda con termino no presente en searchbar y verificar elemento vacio
def test_Search_Wrong():
    driver.maximize_window()
    driver.get("https://motorcredito.com.do/")
    searchbttn = driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/div[2]/button")
    searchbttn.click()
    searchbar = driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/div[2]/ul/li/form/input")
    searchbar.send_keys("jeep", Keys.RETURN)
    assert  check_nonexistance_byXPATH("//*[@id='content']/div/div/div[1]/ol"), "Elemento encontrado"

    driver.quit()