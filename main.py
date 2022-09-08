def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
# ========
ID = '001'
name = "张三"
skill = ''' 
唱歌 
跳舞'''

skill = """
唱歌
跳舞"""

print('Hello Python')
# Python 提供了一个 input()，可以让用户输入字符串，并存放到一个变量里。
# name = input()
# print('Hi', name)

# Python 不使用 {} 来控制类、函数、逻辑判断等，而是使用缩进，缩进的空格可变。
# if True:
#     print(True)
# else:
#     print(False)

# Python 中一般以新行作为语句的结束标识，可以使用 \ 将一行语句分为多行显示
a = 128
b = 1024
c = 512
d = a + \
    b - \
    c
# 如果包含在 []、{}、() 括号中，则不需要使用 \
arr = {
    a,
    b,
    c
}

# 我是单行注释

'''
我是多行注释
我是多行注释
'''

"""
我是多行注释
我是多行注释
"""
# 在进行逻辑判断时，我们需要用到条件语句，Python 提供了 if、elif、else 来进行逻辑判断。
'''
if 判断条件1:
    执行语句1...
elif 判断条件2:
    执行语句2...
elif 判断条件3:
    执行语句3...
else:
    执行语句4...
'''
# for 循环
str1 = 'Python'
for s in str1:
    print(s)
# while 循环
sum1 = 0
m = 10
while m > 0:
    sum1 = sum1 + m
    m = m - 1
print(sum1)
# break
str2 = 'Python'
for s in str2:
    if s == 'o':
        break
    print(s)
# continue
str3 = 'Python'
for s in str3:
    if s == 'o':
        continue
    print(s)
# pass 语句
# if True:
#     pass
