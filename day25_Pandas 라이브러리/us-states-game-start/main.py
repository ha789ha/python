import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.addshape(image)
turtle.Turtle().shape(image)
screen.title("U.S States Game")
state_data = list(data['state'])


class StateName(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def state_name(self, state):
        if state in state_data:
            xpoint = int(data[data['state'] == state].x)
            ypoint = int(data[data['state'] == state].y)
            self.goto(xpoint, ypoint)
            self.write(arg=state)


guessed_states = []
s = StateName()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="guess the state", prompt="what's another states name?")
    s.state_name(answer_state)
    if answer_state in state_data:
        guessed_states.append(answer_state)


print(guessed_states)


turtle.mainloop()
