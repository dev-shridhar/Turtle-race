import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500, 400)
screen.title("Turtle Race")
bet = screen.textinput(title="Which Turtle will win the race?", prompt="Red, Blue, Green, Black, Yellow, Purple, Orange")
colors = ["Red", "Blue", "Green", "Black", "Yellow", "Purple", "Orange"]
distance = [-70, -40, -10, 20, 50, 80, 110]

is_race_on = False

turtles = []
for i in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(-230, distance[i])
    tim.color(colors[i])
    turtles.append(tim)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                screen.title(f"You've won! The {winning_color} turtle wins the race")
            else:
                screen.title(f"You've lost! The {winning_color} turtle wins the race")

        turtle.forward(random.randint(0, 10))
screen.exitonclick()
