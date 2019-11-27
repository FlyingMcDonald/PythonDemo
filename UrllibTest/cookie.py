import http.cookiejar
import urllib.request

class CookieTest:
    def getCookie(self):
        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        opener.open('http://www.baidu.com')
        for item in cookie:
            print(item.name+'='+item.value)

    def saveCookieByMozillaCookieJar(self):
        filename = '/tmp/cookie.txt'
        cookie = http.cookiejar.MozillaCookieJar(filename)
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        opener.open('http://www.baidu.com')
        cookie.save(ignore_discard=True, ignore_expires=True)   
        #ignore_discard:save even cookie set to be discarded
        #ignore_expires:save even cookie that have expires the file is overwritten if it already exists
    
    def saveCookieByLWPJar(self):
        filename = '/tmp/cookie.txt'
        cookie = http.cookiejar.LWPCookieJar(filename)
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        opener.open('http://www.baidu.com')
        cookie.save(ignore_discard=True, ignore_expires=True)
    
    def loadCookie(self):
        cookie = http.cookiejar.MozillaCookieJar()
        cookie.load('/tmp/cookie.txt', ignore_expires=True, ignore_discard=True)
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        response = opener.open('http://www.baidu.com')
        print(response.read().decode('utf-8'))
    
urlObject = CookieTest()
urlObject.loadCookie()