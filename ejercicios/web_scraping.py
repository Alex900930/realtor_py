import requests
from bs4 import BeautifulSoup

website = 'https://www.realtor.com/'
result= requests.get(website)
content =result.text

soup= BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('div', class_='price-wrapper')

if box is not None:
    price = box.find('div', class_='Price__Component-rui__x3geed-0 dJwlwC card-price').get_text()
    print(price)

