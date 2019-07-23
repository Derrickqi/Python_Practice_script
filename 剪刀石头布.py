import random


all_choices = ['石头','剪刀','布']

win_choice = [['石头','剪刀'],['剪刀','布'],['布','石头']]

prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """

cpu = random.choice(all_choices)
ind = int(input(prompt))
player = all_choices[ind]



print("你选择得是%s,电脑选择得是%s" % (player,cpu))

if [player,cpu] in win_choice:
    print('\033[31;1mYou WIN!!!\033[0m')
elif player == cpu:
    print('\033[32;1m平局\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')


