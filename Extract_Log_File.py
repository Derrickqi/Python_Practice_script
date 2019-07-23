import time

example =[
"2019-05-15 08:10:01 aaaa",
"2019-05-15 08:32:00 bbbb",
"2019-05-15 09:01:02 cccc",
"2019-05-15 09:28:23 dddd",
"2019-05-15 10:42:58 eeee",
"2019-05-15 11:08:00 ffff",
"2019-05-15 12:35:03 gggg",
"2019-05-15 13:13:24 hhhh"
]


t9 = time.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')

for i in example:
    t = time.strptime(i[:19],'%Y-%m-%d %H:%M:%S')
    if t > t12:
        break
    if t > t9:
        print(i)