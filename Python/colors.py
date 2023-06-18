import turtle
w=turtle.getscreen()
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.pensize(2)
for x in range(50):
    for colors in("blue","purple","red","green","yellow","brown","grey","white"):
        t.color(colors)
        t.circle(100)
        t.right(10)









w.exitonclick()
