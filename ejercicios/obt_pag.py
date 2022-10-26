# si lo vas a ejecutar local es a partir de aca

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import lxml.html as html
import time


def init_Driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome('chromedriver', options=chrome_options)
    return wd
 
    
def init_Script(dir):
    wd = init_Driver()
    wd.get(dir)
    time.sleep(2)
    element = wd.find_element(By.XPATH, '//*')
    # print(element.get_attribute('innerHTML'))
    wd.quit()
    
    
# url = "https://www.realtor.com/realestateandhomes-search/New-York"
url = "http://localhost/casas_florida.html" 
root_url= "http://localhost/"   
init_Script(url)

# obtener links de las casas
links_houses = '//ul[@class="jsx-343105667 property-list list-unstyle"]/li//a/@href'

req = requests.get(url)
home = req.content.decode('utf8')
parser = html.fromstring(home)
categorias_url= parser.xpath(links_houses)
categorias_url= [root_url+x for x in categorias_url]
print(categorias_url)