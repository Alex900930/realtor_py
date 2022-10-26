import requests
from bs4 import BeautifulSoup

string = input('Que  ciudad quiere buscar?')
r = requests.get('https://www.realtor.com/realestateandhomes-search/{}'.format(string.replace(' ','-')))
contenido = r.content
soup = BeautifulSoup(contenido, 'html.parser')


alldivs = soup.find_all('div', {'class':'styles__StyledContainer-rui__sc-9syhji-0 bMOBXF bgheader_main-container'.replace(' ','.')})
print(alldivs)

# Array para añadir las casas


products_array= []

