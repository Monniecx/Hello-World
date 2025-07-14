import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-150, 90)
t.pendown()

draw_koch_snowflake(t, 300, 2)

screen.mainloop()
