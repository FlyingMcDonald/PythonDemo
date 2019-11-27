import requests

response = requests.get('http://httpbin.org/get')
print(type(response), response.text)
print(response.json())