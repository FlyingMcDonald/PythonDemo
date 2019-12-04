from pyquery import PyQuery as py
doc = py('http://www.baidu.com')
print(doc('body'))