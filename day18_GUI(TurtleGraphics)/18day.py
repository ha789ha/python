import random
import turtle
from turtle import  Turtle, Screen
from random import  randint
# import turtle as t 이런 식으로 별칭을 정해줄 수 있음
timmy = Turtle()
timmy.shape('classic')
# timmy.color('aquamarine')

# 정사각형 만들기
for i in range(4):
    timmy.forward(100)
    timmy.left(90)

# 점선 그리기
for i in range(15):
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)
    timmy.down()

# 다각형 겹쳐서 그리기

for i in range(4, 10):
    turtle.colormode(255)
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    for j in range(i):
        timmy.pencolor(R, G, B)
        timmy.forward(100)
        timmy.left(360/i)


## 무작위 행보
def walk(n):
    angle_list = [90, 180, 270, 360]
    timmy.speed(10)
    timmy.shape('classic')
    timmy.width(10)
    for i in range(n):
        random_color()
        timmy.setheading(random.choice(angle_list))
        timmy.forward(30)


def random_color():
    turtle.colormode(255)
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    timmy.pencolor(R, G, B)

# walk(200)

## 기하학 원모양 만들기
def draw_circle(count, angle):
    timmy.speed(11)
    timmy.width(1)
    for i in range(count):
        random_color()
        timmy.left(angle)
        timmy.circle(100)

## 데미안 허스트의 점 작품 만들기
color_list = [(237, 231, 214), (218, 234, 224), (141, 176, 206), (25, 32, 48), (28, 105, 156), (208, 161, 112), (238, 222, 234),
 (230, 211, 94), (131, 31, 64), (5, 162, 195), (182, 45, 84), (217, 60, 85), (226, 80, 44), (195, 129, 168),
 (54, 167, 116), (29, 61, 115), (108, 181, 91), (109, 99, 88), (2, 102, 119), (193, 187, 47), (241, 204, 1),
 (19, 22, 21), (52, 149, 109), (171, 211, 173), (226, 170, 186), (150, 207, 222), (234, 169, 160), (184, 186, 210),
 (115, 38, 37)]

for i in range(10):
    timmy.speed()
    timmy.up()
    timmy.sety(-100 + 50*i)
    timmy.setx(-100)
    for j in range(10):
        random_color()
        timmy.down()
        timmy.dot(20)
        timmy.up()
        timmy.forward(50)






screen = Screen()
screen.exitonclick() # 클릭하기 전까지 창이 사라지지 않음



