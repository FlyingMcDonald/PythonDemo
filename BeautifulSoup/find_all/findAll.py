html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
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
class FindAll:
    def findAll_1(self):
        print(soup.find_all('ul'))
        print(soup.find_all('ul')[1])
    def findAll_2(self):
        for li in soup.find_all('ul'):
            print(li.find_all('li'))

findAllObj = FindAll()
findAllObj.findAll_2()