import requests
from requests.packages import urllib3

urllib3.disable_warnings()

class CertificateVerify: 
    def addVerify(self):
        response = requests.get('https://www.12306.cn')
        print(response.status_code)
    def noVerify(self):
        response = requests.get('http://www.12306.cn', verify = False)
        print(response.status_code)

requestObj = CertificateVerify()
requestObj.noVerify()