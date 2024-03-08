import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
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

#Test para elegir elementos en un scrollbar y verificar el despliegue de resultados asociados a los mismos
def test_RUNNER():
    driver.maximize_window()
    driver.get("https://motorcredito.com.do/")

    menu = driver.find_element(By.ID, "atm-option")
    menu.click()

    marca = driver.find_element(By.ID, "marca")
    marca.click()

    toyota = driver.find_element(By.XPATH, "//*[@id='marca']/option[104]")
    ActionChains(driver)\
        .scroll_to_element(toyota)\

    toyota.click()

    modelo = driver.find_element(By.ID, "modelo")
    modelo.click()

    fourrunner = driver.find_element(By.XPATH, "//*[@id='modelo']/option[3]")
    ActionChains(driver)\
        .scroll_to_element(fourrunner)\

    fourrunner.click()


    search = driver.find_element(By.CLASS_NAME, "boton")
    search.click()

    assert check_existance_byXPATH("/html/body/div[8]/div/div[1]/div/div[1]/div/a"), "Elemento no encontrado"
    driver.quit()


    



