import requests

print(requests.post('http://httpbin.org/post'))
print(requests.get('http://httpbin.org/get'))
print(requests.delete('http://httpbin.org/delete'))
print(requests.options('http://httpbin.org/headers'))
print(requests.head('http://httpbin.org/headers'))
