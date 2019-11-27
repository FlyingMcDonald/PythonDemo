import requests
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
response = requests.get('http://www.jianshu.com', headers=headers)
print(response.status_code)
print(response.cookies)
print(response.headers)
print(response.history)
print(response.request)
print(response.url)