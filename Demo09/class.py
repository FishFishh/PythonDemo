tup_num = (10, 20, 30)
print(type(tup_num))
tup_num2 = ()
tup_num3 = (10)
print(type(tup_num3))
tup_num4 = (10,)
print(type(tup_num4))
print("==================")
tup_1 = ('a', 'b', 1, 2, 3)
print(tup_1[0])
print(tup_1[1:3])
tup_1 = ('a',)
tup_s = tup_1 + (10, 20)
print(tup_s)
tup_x = tup_1 * 3
print(tup_x)
tup_1 = ('a', 'b', 1, 2, 3)
for i in tup_1:
    print(i)
print("==================")
print(len((10, 20, 30)))
print(min((10, 20, 30)))
print(max((10, 20, 30)))
print(list((10, 20, 30)))
print(tuple([10, 20, 30]))
print("==================")
s1 = [1, 2, 3, 4]
s2 = [5, 6, 7]
print(len(s1 + s2))
print("==================")
s = 'abcdefg'
print(s[::-1])
print("==================")
print([1, 2, 3] * 3)
print("==================")

name = 250;
print("查询余额[输入1]")
print("\t存款[输入2]\t")
print("\t取款[输入3]\t")
print("\t退出[输入4]\t")
abc = input(f"{name}你好,输入:")
if abc == 1:
    print("查询余额[输入1]")
elif abc == 2:
    print("存款[输入2]")
elif abc == 3:
    print("取款[输入3]")
elif abc == 4:
    print("退出[输入4]")
else:
    print("看不懂")
