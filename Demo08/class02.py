list_id = ["4301", "长沙市", "4302", "株洲市", "4303", "湘潭市", "4304", "衡阳市", "4305", "邵阳市", "4306", "岳阳市", \
           "4307", "常德市", "4308", "张家界市", "4309", "益阳市", "4310", "郴州市", "4311", "永州市", "4312", "怀化市","4313", "娄底市", \
           "4321", "株洲市", "4322", "岳阳地区", "4323", "益阳市", "4325", "娄底市", "4326", "邵阳市", "4327", "衡阳市", \
           "4328", "郴州市", "4329", "永州市", "4330", "怀化市", "4331", "湘西土家族苗族自治州"]

str_id = input("请输入您的身份证号码：")

city_id = str_id[0:4]
if city_id in list_id:
    index = list_id.index(city_id)
    print("您出生的城市是：" + list_id[index + 1])
else:
    print("未找到您出生的城市！")