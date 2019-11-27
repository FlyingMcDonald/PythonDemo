import requests

file = {
    'file':open('/tmp/cookie.txt', 'r')
}

response = requests.post('http://httpbin.org/post', files=file)
print(type(response))