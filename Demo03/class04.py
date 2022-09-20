a = float(input("输入第一个数: "))
b = float(input("输入第二个数: "))
c = float(input("输入第三个数: "))
if a > b and a > c:
    print("最大数为%s" % a)
elif b > a and b > c:
    print("最大数为%s" % b)
elif c > a and c > a:
    print("最大数为%s" % b)
