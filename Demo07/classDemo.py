"""
测试用户输入的文本中是否含有敏感词，
如果有，请将敏感词替换为星号*，实现敏感词过滤。
"""

text = input("请输入你要输入的内容:")
text_m = "屎"
for i in text_m:
    if i in text:
        text_new = text.replace(i, "*")

print("过滤前信息为:{}".format(text))
print("过滤后信息为:{}".format(text_new))

"""
已知用户的密码均为6位数，其加密规则如下所示:
1.获取每位元素的ASCII值;
2.将所有元素的ASCI1值进行累加求和;
3.将每位元素对应的ASCII值按照从前往后的顺序进行拼接，并将拼
接后的结果进行反转;
4.将反转的结果与前面累加的结果相加，所得的结果即为加密后的密
码。
"""

password = input("请输入六位密码：")
p_s = 0
p_join = ""
for p in password:
    p_asc = ord(p)
    p_s += p_asc
    p_join = p_join + str(p_asc)
    p_server = p_join[::-1]
    p_su = p_s + int(p_server)
print("加密前信息为:{}".format(password))
print("加密后信息为:{}".format(p_su))
