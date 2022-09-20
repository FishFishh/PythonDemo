"""
案例2：录入某一个学生的个人信息：
姓名：小李
年龄：18
身高：1.75
健康情况：良好
并查看变量数据类型

把自己的学生信息（学号、姓名、年龄、身高、家庭地址）
从键盘手动输入，
再通过print()函数输出，（尝试使用格式化输出（%））

"""
stu_name = "小李"
stu_age = 18
stu_height = 1.75
stu_healthy = "良好"
print("姓名：" + stu_name + "年龄：" + str(stu_age) + " 身高：" + str(stu_height) + " 健康情况：" + stu_healthy)
print(type(stu_name))
print(type(stu_age))
print(type(stu_height))
print(type(stu_healthy))

sno = input("请输入学号：")
name = input("请输入姓名：")
age = input("请输入年龄：")
height = input("请输入身高：")
height = input("请输入家庭地址：")

print("学号：%s,姓名：%s,年龄：%s,身高：%s,家庭地址：%s" % (sno, name, age, height, height))
