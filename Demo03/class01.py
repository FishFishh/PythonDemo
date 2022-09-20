print(ord('a'))  # 97
print(chr(97))  # a

score = int(input("请输入成绩："))
if score > 100 & score < 0:
    print("无意义")
elif score == 100:
    print("优秀")
elif score > 90:
    print("良好")
elif score > 90:
    print("良好")
elif score > 80:
    print("还行")
elif score > 70:
    print("一般")
elif score > 60:
    print("及格")
elif score < 60:
    print("没及格！")
