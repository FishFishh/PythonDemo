money = float(input("输入销售额: "))
if money <= 3000:
    print("薪资等于%s" % float(money*2000))
elif 3000 < money <= 7000:
    print("薪资等于%s" % float(money*1.1*2000))
elif 7000 < money <= 10000:
    print("薪资等于%s" % float(money*1.15*2000))
elif 10000 < money:
    print("薪资等于%s" % float(money*1.2*2000))
