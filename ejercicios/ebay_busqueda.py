import time
from datetime import date
from lib2to3.pgen2 import driver

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

ubicacion = 'C:\\Users\\INFORMATICO\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = ubicacion )

home_link = 'https://www.ebay.com/'

driver.get(home_link+'/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=iphone+x&_sacat=0')

page = BeautifulSoup(driver.page_source,'html.parser')

bloque = page.find('li',attrs={'class':'s-item.s-item__pl-on-bottom', 'data-view':True})
print(bloque)