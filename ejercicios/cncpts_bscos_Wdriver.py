from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\INFORMATICO\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")

driver.get("https://google.com")
titulo = driver.title
assert titulo == "Google"

driver.implicitly_wait(0.5)

buscar_selenium = driver.find_element(by=By.NAME,value="q")
presionar_busqueda = driver.find_element(by=By.NAME,value="btnK")

buscar_selenium.send_keys("Selenium")
presionar_busqueda.click()

buscar_selenium = driver.find_element(by=By.NAME, value="q")
valor = buscar_selenium.get_attribute("value")
# assert valor == "selenium"

driver.quit()

