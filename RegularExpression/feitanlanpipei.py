import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\\d+).*mo', content)
print(result)
print(result.group(1))
print(result.span())