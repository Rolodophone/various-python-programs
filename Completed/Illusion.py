import turtle
canvas = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.up()
pen.goto(0,-200)
pen.down()

x = 200
for i in range(1000):
    x*=0.99
    pen.circle(x,45)
