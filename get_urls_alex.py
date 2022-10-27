# esto lo hice para trabajar Online
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# esto solo funciona con google.colab
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('chromedriver', options=chrome_options)

# esto solo funciona en vscode
driver = webdriver.Chrome("C:\\Users\\INFORMATICO\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")

driver.get("https://www.realtor.com/realestateandhomes-search/Florida")

links= driver.find_elements(By.XPATH, "//ul//div//a/@href")
print(links)
driver.close()