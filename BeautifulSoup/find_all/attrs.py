html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-smail" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
class Attrs:
    def attrs_method_1(self):
        print(soup.find_all(attrs={'id':'list-1'}))
        print(soup.find_all(attrs={'class':'list'}))
        print(soup.find_all(attrs={'class':'element'}))
        print(soup.find_all(attrs={'name':'elements'}))
    
    def attrs_method_2(self):
        print(soup.find_all(id='list-1'))
        print(soup.find_all(class_='element'))
        # print(soup.find_all(name_='elements'))

attrsObj = Attrs()
attrsObj.attrs_method_2()