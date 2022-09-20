"""
案例6：
编写一个程序，用于实现两个数的交换。
"""
a = float(input("输入第一个数:"))
b = float(input("输入第二个数:"))
c = b
b = a
a = c
print("%s,%s" % (a, b))
