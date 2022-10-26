from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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

url = "https://www.realtor.com/realestateandhomes-search/New-York"
init_Script(url)

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
data = soup.find_all(by=By.TAG_NAME, tag="a")
print(data)