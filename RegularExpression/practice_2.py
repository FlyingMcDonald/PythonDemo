import requests, re
url = 'https://book.douban.com'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
urlObj = requests.get(url, headers = headers)
content = urlObj.text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
print(results)
for result in results:
    result = re.sub('\\s', '', result)
    url, author, year, publisher = result
    print(url, author, year, publisher)
# print(results)
# for result in results:
#     result_2 = re.findall('<li.*?>.*?author.*?>(.*?)</div>.*?</li>', result, re.S)
#     print(len(result_2))
#     for result_3 in result_2:
#         result_3 = re.sub('\\s', '', result_3)
#         result_3 = re.sub('&nbsp;', '', result_3)
#         print(result_3)