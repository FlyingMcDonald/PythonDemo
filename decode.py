import base64
s = input("请输入密文:")
for k in range(-1, 25):
    t = ""
    for c in s:
        if 'a' <= c <= 'z': #str是可以直接比较的
            t += chr( ord('a') + ((ord(c)-ord('a')) - k )%26 )
        elif 'A'<=c<='Z':
            t += chr( ord('A') + ((ord(c)-ord('A')) - k )%26 )
        else:
            t += c
    #print(t)
    #str_change = str_raw.lower()
    #str_list = list(str_change)
    #str_list_decry = str_list
    #i = 0
    #while i < len(str_list):
    #    if ord(str_list[i]) >= 97+k: str_list_decry[i] = chr(ord(str_list[i]) - k)
    #    else: str_list_decry[i] = chr(ord(str_list[i]) + 26 - k)
    #    i = i+1
    #print ("解密结果为:"+"".join(str_list_decry))
    #base = t
    #base = str(base)
    t = str(t)
    #print(type(t))
    #print(base)
    result = base64.b64decode(t)
    result = str(result,'utf-8')
    print("解密密码为:"+result)
