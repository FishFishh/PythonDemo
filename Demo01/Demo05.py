# 重命名turtle 和random
import turtle as t
import random as r


def randomcolor():
    # 随机的颜色
    color = (r.random(), r.random(), r.random())
    return color


def pink():
    # 随机颜色
    color = (1, r.random(), 1)
    return color


def randomrange(min, max):
    # 返回介于min和max之间的随机整数
    return min + (max - min) * r.random()


def moveto(x, y):
    # 抬起画笔
    t.penup()
    # 移动到(x,y)处
    t.goto(x, y)
    # 放下画笔
    t.pendown()


# 这里应该是心形的代码部分
def heart(r, a):
    factor = 180
    # 朝向a度方向
    t.seth(a)
    # 画圆
    t.circle(-r, factor)
    t.fd(2 * r)
    t.right(90)
    t.fd(2 * r)
    t.circle(-r, factor)


t.setup(800, 800, 200, 200)
t.speed(9)
t.pensize(1)
t.pencolor(randomcolor())
t.fillcolor(randomcolor())
t.penup()
for i in range(20):
    # 画笔去往
    t.goto(randomrange(-300, 300), randomrange(-300, 300))
    t.begin_fill()
    t.fillcolor(pink())
    # 填充颜色
    # 是否能够修改内部数值？
    # 能
    heart(randomrange(10, 50), randomrange(0, 90))
    t.end_fill()
moveto(400, -400)
