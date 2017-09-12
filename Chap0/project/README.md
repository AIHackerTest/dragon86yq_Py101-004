~ 用于存放本周任务成果。

#### “猜数字游戏”说明
1. 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
2. 程序根据用户输入，给予一定提示（大了、小了、正确）
3. 猜对或用完 10 次机会，游戏结束

#### 猜数字进阶版说明
- 程序内部使用0 - 9 生成一个4位数，每个数位上的数字不重复，且首位数字不为零，如1942
- 用户输入4位数进行猜测，程序返回相应提示：
    - 用A表示数字和位置都正确。
    - 用B表示数字正确但位置错误。
    - 用户猜测后，程序返回A和B的数量
    - 比如：2A1B表示用户所猜数字，有2个数字，数字、位置都正确，有1个数字，数字正确但位置错误
- 猜完或用完10次机会，游戏结束

#### 修改记录
修改时间：20170809
1. 修改bulls_and_cows_advance.py代码。
- 去掉函数user_num()中参数parameter、flag
- 去掉函数user_num() 中return paramter,flag 语句
- 增加
```
    new_num_list = user_num() 
    return new_num_list
    new_num_list1 = user_num()
    return new_num_list1
```
- 去掉main()函数中
```
#        user_flag = True
#        while user_flag:
#            num_list,user_flag = user_num()
```
- 在main()函数中增加num_list = user_num()
2. 修改原因：
- 在user_num函数中设计return paramter,flag是为了确保user_num能够返回一个非None的list。
- 参考[关于递归函数返回值的问题](https://github.com/AIHackers/Py101-004/issues/23)，发现自己遇到的问题与该问题在本质上是一样，在循环调用函数的时候，子函数返回值是一个局部变量，没有将其赋值给主函数中的变量，导致循环调用函数的时候，子函数有返回值，但是主函数的返回值为None。借鉴该例子，在循环调用函数的时候，将子函数的返回值赋值给了主函数中的变量，保证主函数的有一个非None的返回值。


#### 修改记录
修改时间：20170812

修改内容：
1. 修改user_num()函数：
    - 删除对输入的4位数据的每个数字的提取
2. 修改checknum(gennum,unum)函数：
    - 删掉以前2个4位数依依比较的方法。
    -  使用lambda函数、set()集合操作进行判断
3.lambda函数、set集合用法请参考：[成长日志170812  0wd6](https://github.com/dragon86yq/Py101-004/blob/master/Chap0/note/%E6%88%90%E9%95%BF%E6%97%A5%E5%BF%97W0.md)
