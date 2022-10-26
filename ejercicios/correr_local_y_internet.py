'''
PASO 1
Si al guardar con ctrl+s la pagina no se te guarda puedes hacer esta opcion vas a este sitio

https://colab.research.google.com/drive/1QzarxqaVCVzuaVAFdvXgPXpxDO-UJPt9#scrollTo=0HGHX2nW3Rb9

el mismo le pones lo que pongo debajo y le das correr, eso te imprime el resultado, eso lo guardas
en un fichero.html ya que esa seria la salida cuando tu hagas el request al sitio en directo

ten cuidado este sitio cuando vayas a abrir la pagina esta creada por ti para mirar la estructura de los elementos
procura ya estar desconectada porque este sitio hace una peticion y carga las imagenes eso es si vas por esta via.

SI logras guardar el sitio con ctrl+s normmalmente seria directo al PASO 2
'''

import requests
from bs4 import BeautifulSoup

#corres 1 primero y despues el otro, para que puedas salvarlo

#Esto es para obtener una pagina donde salen todos los carros
url = "https://www.birchwood.ca/vehicles/"
response = requests.get(url)
content = response.content     
html = BeautifulSoup(content, "lxml")  
#este resultado lo guardas en un principal.html 
print(html) 

#Esto es para obtener una pagina donde los datos de un carro en particular
url2 = "https://www.birchwood.ca/vehicles/2021/toyota-rav4-le/T229143/"
response = requests.get(url2)
content = response.content     
html_V = BeautifulSoup(content, "lxml")  
#este resultado lo guardas en un vehiculo1.html 
print(html_V) 


'''
PASO 2

Ya estando local montaste un apache o un xammp o algo pones ese sitio dentro de la carpeta
de www o htdocs, o si tienes IIS tambien seria posible lo que hace rato no trabajo con IIS
por eso no te puedo decir mas de este. 

Bueno si ya tienes el servidor apache corriendo y tienes la pagina X dentro de la carpeta del
server nada mas quedaria llamar http://localhost/pagina.html  por ejemplo

yo te pondre el codigo desde linux pero la logica seria la misma yo despues que descargue 
el sitio puse la pagina en mi carpeta de apache y accedo a la misma de la siguiente forma 
'''

import requests
from bs4 import BeautifulSoup

url3 = "http://localhost/principal.html"
response = requests.get(url3)
content = response.content     
html = BeautifulSoup(content, "lxml")  
#ya cuando lo tienes en html puedes hacer lo que desees hacer los find etc ...
print(html) 