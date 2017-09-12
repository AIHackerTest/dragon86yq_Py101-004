# -*- coding:utf-8 -*-

import random
first_number = random.randint(1,9)
second_number = random.randint(0,9)
third_number = random.randint(0,9)
forth_number = random.randint(0,9)

guess_number = first_number*1000 + second_number*100 + third_number*10 + forth_number

datain = int(input("请输入一个4位数："))

Num= 0
Location = 0

for i in range(0,10):
    datain = int(input("请输入一个4位数："))
    datain_1 = datain // 1000
    remainder = datain - datain_1*1000
    datain_2 = remainder // 100
    remainder = remainder - datain_2*100
    datain_3 = remainder // 10
    remainder = remainder - datain_3*10
    
    if first_number == datain_1 | first_number == datain_2 | first_number == datain_3 | first_number == datain_4:
        Num = Num + 1
    if second_number == datain_1 | second_number == datain_2 | second_number == datain_3 | second_number == datain_4:
       Num = Num + 1

    if first_number == datain_1 & second_number == datain_2 & third_number == datain_3 & forth_number == remainder:
        print("恭喜你在%d次猜对了，正确的数字是%d" %(i+1, guess_number))
    else:
        if    

if 