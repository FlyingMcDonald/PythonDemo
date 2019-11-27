import requests

class RequestPost:
    def postTest(self):
        data = {
            'name':'Joker',
            'address':'jju'
        }
        response = requests.post('http://httpbin.org/post', data=data)
        print(response.text)
    
requestObj = RequestPost()
requestObj.postTest()