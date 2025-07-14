import turtle
import math

def drawCircle(t, x, y, radius):
   
    t.penup()
    t.goto(x + radius, y)
    t.pendown()

    step_length = (2.0 * math.pi * radius) / 120.0

    for _ in range(120):
        t.forward(step_length)
        t.left(3)

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(0)

drawCircle(t, 0, 0, 100)

screen.mainloop()
