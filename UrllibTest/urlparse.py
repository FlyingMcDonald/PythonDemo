from urllib import request, parse

class UrlParse:
    def urlParse_1(self):
        result = parse.urlparse('http://www.baidu.com/index.html;user?id=1')
        print(type(result), result)

    def urlParse_2(self):
        result = parse.urlparse('www.baidu.com', scheme='hppts')
        print(result)

    def urlUnparse(self):
        result = ['https', 'www.baidu.com', '/index.htm', 'user', 'id=1', 'comment']
        print(parse.urlunparse(result))
    
    def urlJoin(self):
        print(parse.urljoin('http://www.baidu.com', 'FAQ.htm'))
        print(parse.urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.htm'))
        print(parse.urljoin('http://www.baidu.com/about.htm', 'https://cuiqingcai.com/FAQ.htm?id=1'))
        print(parse.urljoin('http://www.bilibili.com', 'http://www.baidu.com/123.htm'))
    
    def urlEncode(self):
        params = {
            'name':'yyf',
            'age':'21'
        }
        url = 'http:www.baidu.com?'
        print(url+parse.urlencode(params))

urlObject = UrlParse()
urlObject.urlEncode()