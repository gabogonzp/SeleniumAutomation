import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.implicitly_wait(10)

def check_nonexistance_byXPATH(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return True
    return False

#Test para elegir elementos en un scrollbar y verificar el despliegue de mensaje de no presencia del elemento
def test_Chana():
    driver.maximize_window()
    driver.get("https://motorcredito.com.do/")

    menu = driver.find_element(By.ID, "atm-option")
    menu.click()

    marca = driver.find_element(By.ID, "marca")
    marca.click()

    chana = driver.find_element(By.XPATH, "//*[@id='marca']/option[15]")
    ActionChains(driver)\
        .scroll_to_element(chana)\

    chana.click()

    search = driver.find_element(By.CLASS_NAME, "boton")
    search.click()

    assert check_nonexistance_byXPATH("/html/body/div[8]/div/div[1]/div/div/div"), "Elemento no encontrado"
    driver.quit()
    
#Configure non existance function