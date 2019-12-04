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
class CssChooser:
    def CssChooser_1(self):
        print(soup.select('.list'))
        print(soup.select('.panel'))
        print(soup.select('#list-1'))
        print(soup.select('.panel-body #list-1 .element')[0])
    def CssChooser_2(self, ul):
        print(list(enumerate(soup.select(ul))))
        for ul in soup.select(ul):
            print(ul.find_all(text='Foo'))
    
cssChooserObj = CssChooser()
cssChooserObj.CssChooser_2('li')