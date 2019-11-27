import requests

data = {
    'file':open('/tmp/tmp-31268N2JO1EkT0rj9.tpl', 'r')
}

response = requests.post('http://httpbin.org/post', files=data)
print(response.text)