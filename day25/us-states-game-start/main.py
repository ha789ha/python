import turtle
import pandas as pd
data = pd.read_csv('50_states.csv')
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.addshape(image)
turtle.shape(image)
screen.title("U.S States Game")
state_data = list(data['state'])
answer_state = screen.textinput(title="guess the state", prompt="what's another states name?")




xpoint = data[data['state'] == answer_state].x
ypoint = data[data['state'] == answer_state].y


def check_state(state):
    if state in state_data:
        turtle.Turtle().goto(x=xpoint, y=ypoint)
        turtle.Turtle().write(arg=state)

check_state(answer_state)

turtle.mainloop()