per_id = input("请输入身份证号码: ")

while len(per_id) != 18:
    str_id = input("您输入的身份证号位数不对，请重新输入: ")

if per_id[0:2] == "43":
    province = "湖南省"

birthday = per_id[6:14]

if int(per_id[-2]) % 2 == 0:  # 偶数为女性
    sex = "女"
else:
    sex = "男"

show_id = per_id.replace(per_id[-8:-4], "****")

print("-" * 20)
print("该人的身份信息如下:")
print("所在省份:", province)
print("出生日期:", birthday)
print("性别:", sex)
print("-" * 20)
print("身份证保密显示如下:", show_id)
