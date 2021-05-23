import os
import turtle


#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("SpaceInvaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

turtle.exitonclick()