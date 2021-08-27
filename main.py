import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = Turtle()
game_is_on = True
data = pandas.read_csv("50_states.csv")
l_states = data.state.tolist()
n = 0
while game_is_on:
    answer = screen.textinput(f"Guessed {n}/50", "What's the next state?").title()
    if answer == "Exit":
        break
    for state in l_states:
        if answer == state:
            st = data[data.state == state]
            x = int(st.x)
            y = int(st.y)
            writer.hideturtle()
            writer.penup()
            writer.goto(x, y)
            writer.write(state, align="center")
            l_states.remove(state)
            n += 1
        if not l_states:
            writer.goto(0, 0)
            writer.write(f"{state}", align="center", font=24)
            game_is_on = False

list_of_states = pandas.DataFrame(l_states)
list_of_states.to_csv("my_states.csv")
