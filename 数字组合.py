num_list = [1,2,3,4]

NumList = []
for o in num_list:
    for t in num_list:
        for tr in num_list:
            for f in num_list:
                if o != t and t != tr and tr != f and f != o:
                    Num = o,t,tr,f
                    NumList.append(Num)
print(NumList,end=' ')
print("总共出现的次数为%s" % (len(NumList)))