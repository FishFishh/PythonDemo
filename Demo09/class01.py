import random

code_list = []
for i in range(6):  # 控制验证码的位数
    # 条件语句控制随机生成哪一类符 号
    state = random.randint(1, 3)  # 生成状态码
    if state == 1:
        # 当随机生成数字1，即抽取一个大写字母(ASCII码范围是65~90 )
        first_kind = random.randint(65, 90)  # 大写字母
        # 将数字转换为字符串
        random_uppercase = chr(first_kind)
        code_list.append(random_uppercase)
    elif state == 2:
        # 当随机生成数字2，即抽取一个小写字母(ASCII码范围是97~122)
        second_kinds = random.randint(97, 122)  # 小写字母
        random_lowercase = chr(second_kinds)
        code_list.append(random_lowercase)
    elif state == 3:
        # 当随机生成数字3，即抽取一个数字( ASCII码范围是0~9)
        third_kinds = random.randint(0, 9)  # 数字
    code_list.append(str(third_kinds))
verification_code = "".join(code_list)  # 将列表元素连接成字符串
print(verification_code)
