# esto lo hice para trabajar Online
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(executable_path="C:\\Users\\INFORMATICO\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe", chrome_options=options)

driver.get("https://www.realtor.com/")

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#search-bar'))).send_keys('Kansas')

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#search-bar'))).send_keys(Keys.ENTER)

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/section[1]/ul')))

links= driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/section[1]/ul')
links= links.text()
print(links)

