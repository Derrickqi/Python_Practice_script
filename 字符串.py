str1 = 'this is a string'
#首字母大写
print(str1.title())
#全部大写
print(str1.upper())
#全部小写
print(str1.upper().lower())
#字符串拼接
firstName = 'wang'
secondName = 'hao'
lastName = 'yu'
fullName = firstName + ' ' + secondName + ' ' + lastName
print(fullName)
print(fullName.title())
#重复输出字符串
print(fullName * 2)
#输出某个位置的字符
print(fullName[2])
#输出字符串，索引1-3
print(fullName[1:3])

if 'w' in fullName:
    print('%s in fullname' %  'w')

if 'W' not in fullName:
    print('%s not in fullname' % 'w')
#转化为二进制字节
nameBytes = fullName.encode(encoding='utf-8')
print('encode utf-8 %s' % nameBytes)
#转化为unicode string
nameBytes = fullName.encode(encoding='utf-8').decode(encoding='utf-8')
print('encode utf-8 %s' % nameBytes)

#index 查找某个字符串在字符串中的位置，没有则返回异常

try:
    nameBytes.index('w',1,len(fullName))
    print("'s' is in %s" % fullName)
except:
    print("'s' is not in %s" % fullName)
#利用 sort 的 key 参数 将'‘b’ 放到第一行
temp = [('a', 1, 1.5),
        ('b', 2, 5.1),
        ('c', 9, 4.3)]
temp.sort(key = lambda x:x[0]!='b')
print(temp)

#find 查找字符串在字符串中的位置，没有则返回-1
findindex = nameBytes.find('s',0,len(nameBytes))
print(findindex)