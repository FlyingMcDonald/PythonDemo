#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

import urllib.request
import urllib.parse
import socket
import urllib.error

class UrlOpenTest:
    __response = ''
    def urlOpen(self):
        __response = urllib.request.urlopen('http://www.baidu.com')
        print(__response.read().decode('utf-8'))

    def urlPost(self):
        data = bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf-8')
        __response = urllib.request.urlopen('http://httpbin.org/post' ,data = data)
        print(__response.read())
    def urlError(self):
        try:
            __response = urllib.request.urlopen('http://httpbin.org/get',timeout = 0.1)
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                print('TIMEOUT')
    def urlResponse(self):
        __response = urllib.request.urlopen('http://www.baidu.com')
        print(type(__response))
        print(__response.status)
        print(__response.getheaders())
        print(__response.getheader('Content-Type'))

urlObject = UrlOpenTest()
urlObject.urlResponse()