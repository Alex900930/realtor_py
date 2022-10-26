import json
from urllib.request import urlopen

url = "https://random-data-api.com/api/v2/credit_cards?size=10"

response = urlopen(url)
print(response.read())
data = json.loads(response.read())
for i in data:
    print(i)
    break