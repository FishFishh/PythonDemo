"""
1.逻辑运算符
and or运算返回的不一定是布尔值
not运算返回的一定是布尔值

事物的取值:数值、布尔、字符串
(1)数值的取值
0 ---false
not 0 ---Ture
非0 ---Ture
(2)布尔的取值
Ture
not Ture ---False
False
not False --- Ture
(3)字符串的取值
空字符串 ---False
非空字符串 --- Ture

not 3=False
not "" =Ture

A and B
0 and 0 0
0 and 1 0
1 and 1 1
A or B
0 or 0 0
0 or 1 1
1 or 0 1
1 or 1 1

3 and 4 4
2 or 5  2

成员运算符用于判断一个元素是否在某个序列中，如字符串、列表、元组等。
运算符   举例         说明
in      X in y      在y中找到x的值返回True,否则返回False
not in  X not in y  在y中未找到x的值返回True,否则返回False

身份运算符用来判断两个变量的引用对象是否指向同一个内存对象。

例:身份运算符示例。
a =10       #创建变量a，赋值为10
b= 20       #创建变量b，赋值为20
print(a is b)   #输出表达式的值
print(a is not b)
b=10        #修改变量b的值
print(a is b)

2:身份运算符
针对可变数据类型/结构，地址是不一致的   比如列表
针对不可变数据类型/结构，地址是一致的

"""
a = 10
b = 20
print(a is b)
print(a is not b)
b = 10
print(a is b)

stu_no = input("请输入你的学号：")
print(stu_no)
print(type(stu_no))  # 变成字符串类型了

num1 = int(input("请输入一个数字："))
num2 = int(input("请输入第二个数字："))
num3 = num1 + num2
print(num3)
