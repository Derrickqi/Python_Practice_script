tuple1=('两点水','twowter','liangdianshui',123,456)
print(tuple1)
tuple2 = 1,2,2,123,456
print(tuple2)
#元组中只包含一个元素时，需要在元素后面添加逗号,如果不加逗号，创建出来的就不是 元组（tuple）
tuple3 = ('123',)
print(tuple3)


list = [1,2,3,4,5]
print(tuple1[4])
print(len(tuple1))
print(max(tuple2))
print(min(tuple2))
#将列表转换为元组
print(tuple(list))
