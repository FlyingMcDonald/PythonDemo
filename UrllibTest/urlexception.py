import urllib.error,urllib.request,socket

class UrlException:
    def urlException_1(self):
        try:
            urllib.request.urlopen('http://www.cuiqingcai.com/index.htm')
        except urllib.error.URLError as e:
            print(e.reason)
        
    def urlException_2(self):
        try:
            urllib.request.urlopen('http://www.cuiqingcai.com/index.htm')
        except urllib.error.HTTPError as e:
            print(e.reason, e.code, e.headers, sep='\n')
        except urllib.error.URLError as e:
            print(e.reason)
        else:
            print('Request Success')
        
    def urlException_3(self):
        try:
            urllib.request.urlopen('http://www.cuiqingcai.com/index.htm')
        except urllib.error.URLError as e:
            print(type(e))
            print(e.reason)

urlObject = UrlException()
urlObject.urlException_3()
