import requests
from bs4 import BeautifulSoup



r = requests.get('https://www.realtor.com/realestateandhomes-search/Florida')
soup = BeautifulSoup(r.text, 'lxml')

print(soup)