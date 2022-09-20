"""
案例5：
输入直角三角形的两个直角边的长度a、b，求斜边c的长度。用Python语言实现。
"""
import math

a = float(input("输入第一个直角边:"))
b = float(input("输入第二个直角边:"))
c = math.sqrt(a * a + b * b)
print("斜边c的长度:", c)
