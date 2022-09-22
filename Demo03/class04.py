a = float(input("输入第一个数: "))
b = float(input("输入第二个数: "))
c = float(input("输入第三个数: "))
if a > b:
    if a > c:
        print("最大数为%s" % a)
    else:
        print("最大数为%s" % c)
else:
    if b > c:
        print("最大数为%s" % b)
    else:
        print("最大数为%s" % c)
