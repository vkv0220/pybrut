import requests
from pprint import pprint
import json

response = requests.get('https://httpbin.org/get')
response2 = requests.post('https://httpbin.org/post',
                          json={'login': 'admin', 'password': 'admin'})

if response.status_code == 200:
    r = response.json()
    print(pprint(r))

print('===============')

if response2.status_code == 200:
    r2 = response2.json()
    print(r2['json']['password'])