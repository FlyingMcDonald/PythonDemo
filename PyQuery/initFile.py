from pyquery import PyQuery as py
doc = py(filename='demo.html')
print(doc('li'))