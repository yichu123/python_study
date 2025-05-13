# import turtle
# import math

# # 设置画布
# turtle.setup(600, 400)
# turtle.bgcolor("red")
# t = turtle.Turtle()
# t.hideturtle()
# t.speed(0)

# def draw_star(x, y, r, angle=0):
#     t.up()
#     t.goto(x, y)
#     t.setheading(angle)
#     t.forward(r)
#     t.right(162)
#     t.down()
#     t.fillcolor("yellow")
#     t.begin_fill()
#     for _ in range(5):
#         t.forward(2 * r * math.sin(math.pi / 5))
#         t.right(144)
#     t.end_fill()
#     t.up()

# # 大五角星
# draw_star(-200, 120, 50)

# # 四个小五角星的位置和角度
# small_stars = [
#     (-120, 170, 15, -30),
#     (-90, 140, 15, 0),
#     (-90, 100, 15, 15),
#     (-120, 70, 15, 30)
# ]

# for x, y, r, angle in small_stars:
#     # 计算小星星朝向大星星的角度
#     dx = -200 - x
#     dy = 120 - y
#     theta = math.degrees(math.atan2(dy, dx))
#     draw_star(x, y, r, theta)

# turtle.done()

import turtle as t

t.penup()
t.goto(-330,220)
t.pendown()
a=1
t.fillcolor('red')
t.color('red')
t.begin_fill()
while a<=4:
    if a%2==1:
        t.fd(660)
    else:
        t.fd(440)
    t.rt(90)
    a+=1
t.end_fill()
#画五角星
t.penup()
t.goto(-286,132)
b=1
t.fillcolor('yellow')
t.color('yellow')
t.begin_fill()
while b<=5:
    t.fd(132)
    t.right(144)
    b+=1
t.end_fill()

t.penup()
t.goto(-88,176)
b=1
t.fillcolor('yellow')
t.begin_fill()
t.right(156)
while b<=5:
    t.fd(44)
    t.right(144)
    b+=1
t.end_fill()

t.penup()
t.goto(-88,132)
b=1
t.fillcolor('yellow')
t.begin_fill()
t.right(180)
while b<=5:
    t.fd(44)
    t.right(144)
    b+=1
t.end_fill()

t.penup()
t.goto(-66,88)
b=1
t.fillcolor('yellow')
t.begin_fill()
t.right(90)
while b<=5:
    t.fd(44)
    t.right(144)
    b+=1
t.end_fill()

t.penup()
t.goto(-88,22)
b=1
t.fillcolor('yellow')
t.begin_fill()
t.right(90)
while b<=5:
    t.fd(44)
    t.right(144)
    b+=1
t.end_fill()

t.penup()
t.goto(500,0)
t.done()

