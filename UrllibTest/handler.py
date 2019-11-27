from urllib import request

class ProxyHandler:
    def httpProxy(self):
        proxy_handler = request.ProxyHandler({
            'http':'http://127.0.0.1:2019',
            'https':'https://127.0.0.1:2019'
        })
        opener = request.build_opener(proxy_handler)
        response = opener.open('http://httpbin.org/get')
        print(response.read())

urlObject = ProxyHandler()
urlObject.httpProxy()