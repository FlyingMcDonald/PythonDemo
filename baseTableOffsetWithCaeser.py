baseTable = 'ABCDEFGHIJKLMNPORSTUVWXYZabcdefghIjklmnopqrstuvwxyz0123456789+/='
def getBinaryStr(Str):
    binaryStr=''
    for a in Str:
        binary = bin(ord(a)).replace('0b', '')
        while len(binary) < 8:
            binary='0'+binary
        binaryStr+=binary
    print(binaryStr)
    return binaryStr

def subBinaryStr(binaryStr):
    strList = []
    
    for num in range(0,int(len(binaryStr)/6)):
        index = num*6
        sub = (num+1)*6
        strList.insert(num, binaryStr[index:sub])
    print(strList)
subBinaryStr(getBinaryStr('ad'))