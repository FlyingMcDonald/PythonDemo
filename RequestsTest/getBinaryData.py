import requests

response = requests.get('https://flyingmcdonald.github.io/favicon.ico')
print(type(response.text), type(response.content))
print(response.content)
with open('/tmp/favicon.ico', 'wb') as image:
    image.write(response.content)
    image.close()