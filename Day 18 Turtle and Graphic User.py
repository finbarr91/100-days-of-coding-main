from turtle import Turtle,Screen
import random
import turtle
turtle.colormode(255)

tim = Turtle()
tim.shape()

# print(timmy_the_turtle.position())
# timmy_the_turtle.fd(200)
# print(timmy_the_turtle.position())
# timmy_the_turtle.right(90)


# print(timmy_the_turtle.position())
# for movement in range(4):
#     timmy_the_turtle.fd(100)
#     timmy_the_turtle.right(90)

# timmy_the_turtle.home()
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pd()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pu()
# tim.home()
# angle =360
# length_of_sides = 100
# lst_of_color = ['red','blue','black','green','purple','orange','pink','indigo','yellow']
# for number_of_sides in range(3,11):
#     tim.color(random.choice(lst_of_color))
#     for n in range(number_of_sides):
#         tim.fd(length_of_sides)
#         tim.right(360/number_of_sides)

# tim.home()
#
# def draw_shape(number_of_sides):
#     lst_of_color = ['red', 'blue', 'black', 'green', 'purple', 'orange', 'pink', 'indigo', 'yellow']
#     tim.color(random.choice(lst_of_color))
#     angle = 360/number_of_sides
#     length_of_sides = 100
#     for number_of_sides in range(number_of_sides):
#         tim.fd(length_of_sides)
#         tim.right(angle)
#
# for n in range(3,11):
#     draw_shape(number_of_sides=n)

def random_color():
    r= random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

#
#
# directions = [0,90,180,270]
# tim.speed('fastest')
# tim.width(8)
# for _ in range(300):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
tim.speed("fastest")
def circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(radius=100)
        current_heading = tim.heading()
        tim.setheading(current_heading+size_of_gap)


circle(5)


screen = Screen()
screen.exitonclick()



