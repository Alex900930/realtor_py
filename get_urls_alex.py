# esto lo hice para trabajar en Local

import requests
import lxml.html as html


url = "https://www.realtor.com/realestateandhomes-search/New-York" 
root_url= "https://www.realtor.com/"



def get_url(url):
    root_url= "http://localhost/"
    
    # obtengo los links de las casas en esta pagina con el xpath
    links_houses = '//ul[@class="jsx-343105667 property-list list-unstyle"]/li//a/@href'

    #luego obtengo el html de la casa con el request.get
    req = requests.get(url)
    
    # obtengo el content de la pagina con el req.content
    home = req.content.decode('utf8')
    
    # parseamos la pagina con el html.fromstring
    parser = html.fromstring(home)
    
    # obtengo las house urls con el parser.xpath 
    house_url= parser.xpath(links_houses)
    
    # luego concateno las urls con su url root(o raiz)
    house_url= [root_url+x for x in house_url]
    
    return house_url
print(get_url(url))