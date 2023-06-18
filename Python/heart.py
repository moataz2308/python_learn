import turtle
pen=turtle.Turtle()
def curve():
    for i in range (200): 
        pen.right(1)
        pen.forward(1)
        
    
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
def txt():
    pen.down()
    pen.setpos(-68,95)
    pen.down()
    pen.color('green')
    pen.write("Best dad:)",font=("Verdana",24,"bold"))
    pen.hideturtle()

heart()
txt()
pen.ht()
input()

    
    


