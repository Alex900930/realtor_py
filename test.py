from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# configure webdriver
options = Options()
options.headless = True  # hide GUI
options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")  # ensure window is full-screen
# configure chrome browser to not load images and javascript
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.images": 2}
)

driver = webdriver.Chrome(options=options, chrome_options=chrome_options)
driver.get("https://www.realtor.com/realestateandhomes-search/Florida")

sel = Selector(text=driver.page_source)
parsed = []
for item in sel.xpath("//ul//div//a/@href"):
    parsed.append({
        'url': item.css('.jsx-1534613990 card-anchor::attr(href)').get(),
    })

print(json.dumps(parsed, indent=2))