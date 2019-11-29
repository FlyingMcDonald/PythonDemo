import re
html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
    经典老歌列表
</p>
<ul id="list" class="list-group">
    <li data-view="2">一路有你</li>
    <li data-view="7">
        <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
    </li>
    <li data-view="4" class="active">
        <a href="/3.mp3" singer="齐秦">往事随风</a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧玲">记事本</a></li>
    <li data-view="5">
        <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
    </li>
</ul>
</div>
'''
class Findall:
    def findAll_1(self):
        result = re.findall('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
        for key, value in result:
            print(key+' '+value)
    
    def findAll_2(self):
        results = re.findall('<li.*?>\\s*?(<a.*?>)?(\\w+)(</a>)?\\s*?', html, re.S)
        print(type(results))
        for result in results:
            # print(result)
            print(result[0], result[1], result[2])
    
reg = Findall()
reg.findAll_2()