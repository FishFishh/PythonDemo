import math

a = float(input("输入第一个边:"))
b = float(input("输入第二个边:"))
c = float(input("输入第三个边:"))
if a + b > c and a + c > b and b + c > a:
    h = (a+b+c)/2
    p = math.sqrt(h*(h-a)*(h-b)*(h-c))
    print("面积为%s" % p)
else:
    print("不是三角形")
