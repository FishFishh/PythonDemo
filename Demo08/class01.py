id = "4301,长沙市;4302,株洲市;4303,湘潭市;4304,衡阳市;" \
        "4305,邵阳市;4306,岳阳市;4307,常德市;4308,张家界市;" \
        "4309,益阳市;4310,郴州市;4311,永州市;4312,怀化市;" \
        "4313,娄底市;4321,株洲市;4322,岳阳地区;4323,益阳市;" \
        "4325,娄底市;4326,邵阳市;4327,衡阳市;4328,郴州市;" \
        "4329,永州市;4330,怀化市;"

list = []
list1 = []
for i in id:
    list = id.split(";")  # 分号切割
list.pop()
for i in range(len(list)):
    list1.append(list[i].split(","))  # 逗号切割
list_key = []
list_value = []
for i in range(22):
    list_key.append(list1[i][0])
    list_value.append(list1[i][1])
print(list_key)
print(list_value)
