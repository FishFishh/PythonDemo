score = float(input("请输入成绩："))

if score > 100 and score < 0:
    print("无意义")
elif score == 100:
    print("A")
elif score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
elif score < 60:
    print("E")
