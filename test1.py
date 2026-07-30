import turtle
t = turtle.Turtle()
t.speed(0)
t.color("hotpink")
t.pensize(2)

for i in range(36):
    t.circle(50)
    t.left(10)

turtle.done()