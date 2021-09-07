import requests
from pprint import pprint
import json

#print(requests.__version__)
#print(requests.__copyright__)

r_get = requests.get('https://swapi.dev/api/planets/5')
#pprint(r_get.headers)
print('status = ',r_get.status_code,'\n')
data = json.loads(r_get.text)
pprint(data)


