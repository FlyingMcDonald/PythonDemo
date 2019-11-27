from urllib import request, parse


class UrlRequest:
    def UrlRequest(self):
        url = request.Request('http://www.baidu.com')
        response = request.urlopen(url)
        print(response.read().decode('utf-8'))
    
    def UrlRequestByPost(self):
        url = 'http://httpbin.org/post'
        headers = {
            'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
            'Host:httpbin.org'
        }
        dict = {
            'name':'yyf'
        }
        data = bytes(parse.urlencode(dict), encoding='utf-8')
        req = request.Request(url = url, data = data, headers = headers, method='POST')
        response = request.urlopen(req)
        print(response.read().decode('utf-8'))

    def UrlRequestByPost_2(self):
        url = 'http://httpbin.org/post'
        dict = {
            'name':'yyf'
        }
        data = bytes(parse.urlencode(dict), encoding='utf-8')
        req = request.Request(url=url, data=data, method='POST')
        req.add_header('User-Agent', 'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)')
        response = request.urlopen(req)
        print(response.read().decode('utf-8'))

urlObject = UrlRequest()
urlObject.UrlRequestByPost_2()