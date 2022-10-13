# 学生的学号是90号
stu_no = 90
stu2_no = 202099008
print("学生的学号是%d号" % stu_no)
print("学生的学号是%d号" % stu2_no)
print("学生的学号是{}号".format(stu_no))
print(f"学生的学号是{stu_no}")
# 小李考了65分
stu_name = "小李"
stu_score = 65
print("%s考了%d分" % (stu_name, stu_score))

str1 = "hello"
print("%20s" % str1)

print("当前时间为: {:02}: {:02}".format(9, 17))
# print("当前时间为%02d:%02d"%(9, 17))
print("几种对齐方式的区别: {0:<10}.{0:>10}.{0:^10}".format("123"))
print("显示进制前面的符号，例如: {0:#o}.{0:#b}.{0:#x} ".format(20, 30))

# 标准格式化输出
# 整型--约束输出的长度n
# 操作符%0nd
# .format(){下标:0nd}
# 浮点型--约束小数的位数m
# 操作符 %.mf
# .format(){下标:.mf}
# 字符串型--文本数据对齐方式
# 操作符%s正号表示右对齐负号表示左对齐
# .format() {下标:< > ^}

word={}
