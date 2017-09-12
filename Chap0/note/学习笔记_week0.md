- 基本任务：
    1.  使用 Python3 改写《Learn Python The Hard Way》若干个小练习，上手 Python3 的使用
        - 如果你已完成 40 个小练习，可任选 7 个小练习改写，建议选择能体现 Python3 与 Python2 变化的练习来改写，以便更熟练使用 Python3
        - 如果你尚未完成 40 个小练习，请使用 Python3 完成剩余小练习
    2. 使用 Jupyter Notebook ，写篇教程给六个月前的自己，教他 / 她更快上手编程：
        - 想象你面对未接触过 Python 的自己，你会教他 / 她如何上手编程？如何快速掌握编程基本技能？如何少走弯路？……
        - 结合代码示范，教会他 / 她实现数据类型、变量、函数、条件语句、循环语句等基础概念
    参考资料：Python 3.6.2 官方文档[Python 3.6.2 documentation](https://docs.python.org/3.6/index.html)

完成后还有余力，可翻卡片背面，完成进阶任务;-)
- 进阶任务：
猜数字（又称 Bulls and Cows ）是一种古老的密码破译类益智小游戏，起源 20 世纪中期，一般由两人或多人玩。
学有余力的你，综合运用编程基础技能，尝试实现一个猜数字小游戏吧。
    - 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
    - 程序根据用户输入，给予一定提示（大了、小了、正确）
    - 猜对或用完 10 次机会，游戏结束
如果你轻松完成以上任务，可查看后续卡片《进阶任务：开发猜数字小游戏》背面，领取升级版猜数字小游戏任务。



ex12:
python2.x
1. print是一种输出语句，和if语句，while语句一样，输出不用括号。
2. input()输入数据是int，因此需要用raw_input()输入数据才是str
python3.x
1. print是内置函数，输出的内容在括号()内。
2. input()输入是str。

ex16:
truncate函数：截断数据默认为当前位置
Syntax: file.truncate([size])
```
# test.txt contents:
# ABCD
f = open(r'C:\test.txt','r+')
f.truncate(2)
f.read()
输出：AB

```

ex18:
函数定义：
函数中*argvs用法
在函数中不知道要传递多少个参数时，可以使用*argvs
在函数中不知道要传递多少个参数时，使用**kwargs允许传递有名字的变量
```
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", argv)
test_var_args('yasoob','python','eggs','test')

result:
first normal arg: yasoob
another arg through *argv : python
another arg through *argv : eggs
another arg through *argv : test


def greet_me(**kwargs):
    if kwargs is not None:
        for key,vaule in kwargs.items():
            print("%s == %s"%(key,value))
greet_me(name="yasoob")

result:
name == yasoob  
```

参考：[*args and **kwargs in python explained](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)


ex21:
函数return的用法：函数可以有返回值。
函数可以传递多种参数：
1. Required arguments：在定义函数的时候有参数，在调用函数的时候必须要有参数。
```
def printme( str ):
   print(str)

printme()

results:
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    printme();
TypeError: printme() takes exactly 1 argument (0 given)   
```
2. Keyword arguments：使用keyword作为参数，调用函数时需要识别keyword
```
def printme( str ):
   print(str)

printme( str = "My string")

results:
My string
```
3. Default arguments：在声明参数时有默认值，调用函数时，如果不对参数赋值，参数使用默认值
```
def printinfo( name, age = 35 ):
   print("Name: ", name)
   print("Age ", age)

printinfo( name="miki" )

results；
Name:  miki
Age  35
```
4. Variable-length arguments：见ex18

参考：[tutorials point](https://www.tutorialspoint.com/python/python_functions.htm)


ex24:
1./在python2和python3中的不同
    - python2:
    ```
    >>> a = 10/4
    >>> a
    2
    >>> a = 10.0/4
    >>> a
    2.5
    ```
    - python3:
    ```
    >>> a = 10/4
    >>> a
    2.5
    ```
在python3中/可以计算的结果数据类型是float，在python2中/计算的结果数据类型是int。    



ex35:
exit(0):正常运行程序并退出程序
exit(1):非正常运行导致退出程序
in的用法：string in string返回True or False



ex39:
字典中get()用法：返回指定key的value,如果不存在返回None
dict.get(key,default=None)
```
dict = {'Name': 'Zabra', 'Age': 7}

print("Value : %s" %  dict.get('Age'))

results:
Value: 7
```
