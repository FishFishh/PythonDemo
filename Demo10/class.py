list_info = {"Lisi", True, 1.7, "江西南昌"}
dict_info = {" name": "Lisi", "sex": True, "height": 1.7, "english": 79}
dict_name = {1: "zhangsan", 2: "lisi", 3: "zhangsan"}
dict_info["english"] = 89
print("修改english：" +str(dict_info))
dict_info["java"] = 60
print("添加java："+str(dict_info))
dict_info.update({"java": 70})
print("更新java："+str(dict_info))
dict_info.pop("sex")
print("删掉sex："+str(dict_info))
dict_info.popitem()
print("删掉，最后一个："+str(dict_info))
del dict_info["english"]
print("删掉english："+str(dict_info))
a=dict_info.get("name")
print("get："+str(a))
print("直接get："+str(dict_info.get("name")))
b=dict_info.get("java",0)
print("在里面get："+str(b))
dict_info.clear()
print("清空："+str(dict_info))
