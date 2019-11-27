import requests

class KeepSession:
    def noSession(self):
        requests.get('http://httpbin.org/cookies/set/number/123456789')
        response = requests.get('http://httpbin.org/cookies')
        print(response.text)

    def addSession(self):
        s = requests.session()
        s.get('http://httpbin.org/cookies/set/number/123456789')
        response = s.get('http://httpbin.org/cookies')
        print(response.text)

requestObj = KeepSession()
requestObj.addSession()
