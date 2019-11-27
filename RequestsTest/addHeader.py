import requests


class addHeader:
    def noAddHeader(self):
        response = requests.get("https://www.zhihu.com/explore")
        print(response.text)
    
    def addHeader(self): 
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }
        response = requests.get("https://www.zhihu.com/explore", headers = headers)
        print(response.text)

requestObj = addHeader()
requestObj.addHeader()