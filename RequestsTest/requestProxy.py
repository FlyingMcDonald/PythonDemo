import requests

class RequestProxy:
    def httpProxy(self):
        proxies = {
            'http':'http://127.0.0.1:2019',
            'https':'https://127.0.0.1:2019'
        }
        response = requests.get('https://www.taobao.com', proxies=proxies)
        print(response.status_code)
    
    def sockesProxy(self):
        proxies = {
            'http':'socks5://127.0.0.1:2019',
            'https':'socks5://127.0.0.1:2019'
        }
        response = requests.get('https://www.taobao.com', proxies=proxies)
        print(response.status_code)
    
requestObj = RequestProxy()
requestObj.sockesProxy()