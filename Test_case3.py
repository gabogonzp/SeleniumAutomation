import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://motorcredito.com.do/")

menu = driver.find_element(By.XPATH, "//*[@id='hamburgerResponsive2']/img")
menu.click()

#Test para verificar la visibilidad y luego interactuar con elemento dinamico en menu acordion

def test_Plan_Ready():

    element = driver.find_element(By.XPATH, "//*[@id='accordion']/div[1]/div[1]/a")
    element.click()
    dynelement= WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//*[@id='menuPrestamos']/div/a[2]")))
    dynelement.click()

    assert "Plan Ready" in driver.title

    driver.quit()