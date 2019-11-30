from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
class childNode:
    def method_1(self):
        print(soup.p.contents)
        for result in soup.p.contents:
            # print(type(result))
            result = re.sub('\\s', '', result.string)
            print(result)
        
    def method_2(self): #输出字节点
        print(soup.p.children)
        for i, child in enumerate(soup.p.children):
            print(i, child)
    def method_3(self):
        print(soup.p.descendants)
        for i, child in enumerate(soup.p.descendants):
            print(i, child)

obj = childNode()
obj.method_3()