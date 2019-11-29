import requests, re
url = 'https://book.douban.com'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
urlObj = requests.get(url, headers = headers)
content = urlObj.text
# print(content)
# with open('/tmp/douban.txt', 'w') as e:
#     e.write(content)
#     e.close()
content = re.sub('\\s','', content)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
# print(len(results))
print(results)
# for result in results:
#     # result_2 = re.sub('\\s', '', result)
#     author, year, publisher = result
#     year = re.sub('\\s', '', year)
#     publisher = re.sub('\\s', '', publisher)
#     print(author, year, publisher)
    # print(result)
# print(results)
# for result in results:
#     result_2 = re.findall('<li.*?>.*?author.*?>(.*?)</div>.*?</li>', result, re.S)
#     print(len(result_2))
#     for result_3 in result_2:
#         result_3 = re.sub('\\s', '', result_3)
#         result_3 = re.sub('&nbsp;', '', result_3)
#         print(result_3)
# .*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>
#  title="(.*?)">