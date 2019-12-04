from bs4 import BeautifulSoup
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
class ParentNode:
    def parentNode_1(self):#父节点
        soup = BeautifulSoup(html, 'lxml')
        print(soup.a.parent)

    def parentNode_2(self):#祖先节点
        soup = BeautifulSoup(html, 'lxml')
        # print(list(enumerate(soup.a.parents)))
        for i, value in enumerate(soup.a.parents):
            print(i, value)
nodeObj = ParentNode()
nodeObj.parentNode_2()