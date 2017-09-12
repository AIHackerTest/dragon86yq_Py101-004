# -*- coding:utf-8 -*-

import random
password = random.randint(1,20)
for i in range(0,10):
    datain = int(input("请输入1-20之间的一个数字 : "))
    if(datain > password):
        print("输入的数据大了,你还剩下%d 次机会" %(9-i) )
    elif(datain < password):
        print("输入的数据小了,你还剩下%d 次机会" %(9-i) )
    else:
        print("输入正确，一共使用 %d 次机会" %(i + 1) )
        exit(0)
print("已经用完10次机会,正确的答案是"%(password))
