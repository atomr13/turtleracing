import random
from turtle import Turtle, Screen

race = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Place Your Bet","Which Turtle Will Win the Race: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
startx = -230
starty = -100
color = 0
turtles=[]

for x in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[color])
    turtle.goto(startx, starty)
    color += 1
    starty += 40
    turtles.append(turtle)

if user_bet:
    race = True

while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've Won! The {winner} turtle won the race!")
            else:
                print(f"You've Lost! The {winner} turtle won the race!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
