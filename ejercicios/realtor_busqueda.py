import time
from datetime import date
from lib2to3.pgen2 import driver

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

ubicacion = 'C:\\Users\\INFORMATICO\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = ubicacion )

home_link = 'https://www.realtor.com'

r = requests.get('https://www.realtor.com/realestateandhomes-search/Houston_TX')

page = BeautifulSoup(driver.page_source,'html.parser')

soup = BeautifulSoup(r.text, 'lxml')
print(soup)


# bloque = page.find('li',attrs={'id':'item_7473481475', 'data-view':True})
# print(page)