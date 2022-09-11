## 인스턴스
# timmy, tommy를 turtle의 객체들이라 할 때 둘을 instance라 부를 수 있다
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title= 'make your bet', prompt='어떤 거북이가 우승할까요? 색깔을 입력하세요')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-235, -100 + 50 * i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.color()
            print(win_color)
            if user_bet == win_color:
                print('you win!')
            else:
                print('you lost')
            break
        random_distance = random.randint(0 ,10)
        print(turtle.color())
        turtle.forward(random_distance)




screen.exitonclick()


