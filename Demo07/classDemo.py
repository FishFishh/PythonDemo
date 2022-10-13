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
