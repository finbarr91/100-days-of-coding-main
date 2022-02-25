from turtle import Turtle,Screen
import random

is_race_on =False
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)
color = ['red','green','yellow','blue','purple', 'orange']

y_position = [0,50,-50,100,-100,150]

all_turtles = []
for index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color ==user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def counter_clockwise():
#     tim.setheading(tim.heading()-10)
#
# def clockwise():
#     tim.setheading(tim.heading()+10)
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key='w',fun= move_forward)
# screen.onkey(key='a',fun=counter_clockwise)
# screen.onkey(key='d',fun=clockwise)
# screen.onkey(key='c',fun=clear_drawing)
# screen.onkey(key='s', fun=move_backward)







screen.exitonclick()