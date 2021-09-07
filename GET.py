import requests
from pprint import pprint
import json

print(requests.__version__)
print(requests.__copyright__)

r_get = requests.get('https://www.metaweather.com/api/location/2487956/2018/11/18')
pprint(r_get.headers)

data = json.loads(r_get.text)
pprint(data)


