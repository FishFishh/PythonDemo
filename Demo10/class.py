list_info = {"Lisi", True, 1.7, "江西南昌"}
dict_info = {" name": "Lisi", "sex": True, "height": 1.7, "english": 79}
dict_name = {1: "zhangsan", 2: "lisi", 3: "zhangsan"}
dict_info["english"] = 89
print("修改english：" + str(dict_info))
dict_info["java"] = 60
print("添加java：" + str(dict_info))
dict_info.update({"java": 70})
print("更新java：" + str(dict_info))
dict_info.pop("sex")
print("删掉sex：" + str(dict_info))
dict_info.popitem()
print("删掉，最后一个：" + str(dict_info))
del dict_info["english"]
print("删掉english：" + str(dict_info))
a = dict_info.get("name")
print("get：" + str(a))
print("直接get：" + str(dict_info.get("name")))
b = dict_info.get("java", 0)
print("在里面get：" + str(b))
dict_info.clear()
print("清空：" + str(dict_info))
print("==============")

dict_info = {" num": 123, "name": "小明", "age": 18, " sex": True}
for i in dict_info.items():
    print(i)
print("==============")
for i, j in dict_info.items():
    print(i, j)
print("==============")
stu_info1 = {"name": "欧阳", "sex": "F", "age": 21}
stu_info2 = {"name": "小李", "sex": "M", "age": 20}
stu_info3 = {"name": "小刘", "sex": "F", "age": 19}
student = [stu_info1, stu_info2, stu_info3]
for s in student:
    print(s)
stu_class = {"欧阳": ["C语言", "Python程序设计"], "小李": ["Java基础", "Python程序设计"],"小刘": ["前端技术", "Java基础"]}
for name, clas in stu_class.items():
    print("学生姓名为", name)
    for c1 in clas:
        print("学生选课为", c1)
stu_info = {"欧阳": {"sex": "F", "age": 21}, "小李": {"sex": "M", "age": 20}, "小刘": {"sex": "F", "age": 19}}
for name, info in stu_info.items():
    print("学生姓名为", name, "学生性别为", info["sex"], "学生年龄为", info["age"])
