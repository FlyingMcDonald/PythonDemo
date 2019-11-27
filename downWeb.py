
import urllib.request

url = "http://www.baidu.com"
response1 = urllib.request.urlopen(url)

print ("First the method")

print (response1.read().decode('utf-8'))

print (len(response1.read()))

print("Second the method")

request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print (response2.getcode())
print (len(response2.read()))
