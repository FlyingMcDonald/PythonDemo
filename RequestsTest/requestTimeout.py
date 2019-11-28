import requests
from requests.exceptions import ReadTimeout,ConnectionError, RequestException

try:
    response = requests.get('http://httpbin.org/get', timeout=0.5)
    print(response.status_code)
except ReadTimeout as e:
    print('Connection Timeout')
except ConnectionError as e:
    print('Connetc Error')
except RequestException as e:
    print("Error")