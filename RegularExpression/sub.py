import re
content = 'YYFNB Hello 1234567 World_This is a Regex Demo YYFNB'

class RegularSub:
    def sub_1(self):
        result = re.sub('\\d+',"", content)
        print(result)
    def sub_2(self):
        result = re.sub('\\d+', 'YYFNB', content)
        print(result)
    
    def sub_3(self):
        result = re.search('^YYF.*?\\d+\\s(\\w+)\\s.*?NB$', content)
        print(result.group(1))
        result_2 = re.sub(result.group(1),'',content)
        print(result_2)

sub = RegularSub()
sub.sub_3()