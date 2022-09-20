"""
案例3：
模拟收银员收银，
输入苹果价格，单位：元/斤
输入苹果重量，单位：斤
计算输出付款金额。
"""

price = input("输入苹果价格:")
weight = input("输入苹果重量:")
money = float(price) * float(weight)
print("付款金额为:" + str(money))
