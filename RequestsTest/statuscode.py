import requests

response = requests.get('http://httpbin.org/get')
if response.status_code == 200:
    print('request success')
    