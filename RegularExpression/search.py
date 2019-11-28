import re

content = 'YYFNB Hello 1234567 World_This is a Regex Demo YYFNB'
result = re.search('Hello.*?(\\d+).*?Demo', content)
print(result)
print(result.group())
print(result.span())