program = ['c++','python','java','php']
print(program)
print(program[0])
#第三个字符首字母大写
print(program[2].title())
#修改第四个字符
program[3] = 'c#'
print(program)
#末尾增加shell
program.append('shell')
print(program)
#在第二个元素中插入perl
program.insert(1,'perl')
print(program)
#copy列表中的所有元素
program2 = program[:]
print(program2)
#将末尾的元素弹出
lan = program.pop()
print(program)
#弹出第二个元素
lan = program.pop(1)
print(program)
#删除第二个元素，再不需要使用时效率高于pop
del program[1]
print(program)
#删除c++
wlan = program.remove('c++')
print(program)
#队列表永久排序
program2.sort()
print(program2)
#反向排序
program2.sort(reverse=True)
print(program2)
#temp sort 临时排序
tempsort = sorted(program2)
print(tempsort)
print(program2)
#range 产生自然数列生成器，左闭右开
for value in range(1,5):
    print(value,end='\t')
print(list(range(1,5)))
#指定步长，生成偶数数列
even_numbers = list(range(0,10,2))
print(even_numbers)
#列表自动生成器
squares = [i for i in range(1,11)]
print(squares)
#切片
strlist = ['https','www','baidu','com']
print(strlist[0:3])
#不指定:前索引，则从列表第一个元素开始
print(strlist[:3])
#不指定:后数量，则取出直到列表末尾所有元素
print(strlist[:2])
#从倒数第三个元素取，直到末尾
print(strlist[-3:])
#遍历切片,取出前三字符串，并title
for element in strlist[:]:
    print(element.title())