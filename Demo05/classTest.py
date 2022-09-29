import random

player1 = int(input("请输入剪刀（0）、石头（1）、布（2）："))
player2 = random.randint(0, 2)
if ((player1 == 0 and player2 == 2)
        or (player1 == 1 and player2 == 0)
        or (player1 == 2 and player2 == 1)):
    print("玩家获胜！")
elif player1 == player2:
    print("平局！")
else:
    print("电脑获胜！")
