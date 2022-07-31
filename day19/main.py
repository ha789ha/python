from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def clockwise():
    timmy.right(10)
    timmy.forward(10)

def counterclockwise():
    timmy.left(10)
    timmy.forward(10)

def clear():
    timmy.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key='d', fun=clockwise)`
screen.onkey(key='c', fun=clear)
screen.exitonclick()

