# Librerias
import time
from telnetlib import EC

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

# opciones de navegacion
options= webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver_path= 'C:\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get('https://eltiempo.es')

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ','.'))))\
        .click()    

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#term')))\
        .send_keys('Madrid')    

