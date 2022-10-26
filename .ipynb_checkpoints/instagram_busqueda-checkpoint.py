from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)


driver.get("https://www.realtor.com/realestateandhomes-search/Houston_TX")

find_count_house= driver.find_element("xpath", '//*[@id="srp-header"]/div[2]/div[1]/span')





driver.quit()