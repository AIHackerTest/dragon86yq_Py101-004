# -*- coding:utf-8 -*-
import random
import re

"""
函数：generate_num()
作用：产生一个四位随机数
原理：
1. 使用range(0,9)产生一个0-9的序列
2. 使用ramdom.sample从产生的序列中随机采用5个数据
返回值：产生产生的含有4个元素的list: gnum
"""
def generate_num():
    gnum = random.sample(range(0,9),4)
    while gnum[0] == 0: 
        gnum = random.sample(range(0,9),4)
    return gnum

"""
函数：user_num()
作用：产生输入
原理：
1. 使用正则表达式匹配输入的字符串，如果检测到非0-9的数字，给出警告
2. 提取输入的4为数字
3. 使用ramdom.shuffle将采用的5个数据进行乱序排列
返回值：长度为4的list，list中的元素从0 - 3分别存储输入数据高位到低位。
        重复判断标志flag
"""
def user_num():
    num = input("请输入一个首位非零的四位数:")
    match_num = re.compile(r'\D')
    result = match_num.search(num)
# 第一次输入四位数字，第二次输入非四位数字或异常数字，第三次再输入四位数字
# user_num()函数会循环执行，此时需要保证返回的list参数长度为4，否则会出现异常。
    #parameter = [0,0,0,0]
    if result :      
        print("输入非法数据，请重新输入四位数字")
        #flag = True
        #return parameter,flag
        #new_num_list = user_num()
        #return new_num_list
        return user_num()
    else:
        user_length = len(num)
        if user_length == 4:
            num = int(num)
            a = num // 1000
            b = (num % 1000) // 100
            c = (num % 100) // 10
            d = num % 10
            num_list = [a,b,c,d]
            #flag = False  
            #return num_list,flag
            return num_list
        else:
            print("输入的数字不在范围之内，请重新输入")   
            #flag = True
            #return parameter,flag                
            #new_num_list1 = user_num()
            #return new_num_list1
            return user_num()


"""
函数：checknum
作用：比较产生的随机数gennum和输入的数字unum
原理：
1. 使用for语句，循环4次，判断gennum和unum在位置和数值上使用一样
2. 使用for语句，循环4次，通过 in 判断unum中的数字是否存在于gennum
返回值：返回1中判断的结果corretc和2中判断的结果location
"""
def checknum(gennum,unum):  
    correct = 0
    location = 0
    for i in range(0,4):  
        if gennum[i] == unum[i]:
            correct += 1
        else:
            continue

    for j in gennum:  
        if j in unum:
            location += 1
        else:
            continue

    location = location - correct
    
    return correct, location  

def main():
    print("欢迎来到猜数字游戏")
    answer = generate_num()
# 循环10次
    for i in range(0,10):
#        user_flag = True
# 判断是否输入异常数字，正确输入四位数字才会往后执行        
#        while user_flag:
#            num_list,user_flag = user_num()
        num_list = user_num()
        [correct,location] = checknum(answer,num_list)
        if correct == 4:
            print("恭喜你在第%d次，猜到正确结果" % (i+1))
            exit(0)
        else:
            print("这是你第%d次猜，本次结果是%dA%dB，你还剩下%d次机会" %(i+1,correct,location,9-i))            
    print("10次机会已经用完游戏结束,结果是%s" %(str(answer)))
    result = input("请输入start，重新开始游戏，或者输入其他任意符号结束游戏:")
# 继续重复玩游戏
    if result == "start":  
        main() 
    else:
        exit(0)

main()








