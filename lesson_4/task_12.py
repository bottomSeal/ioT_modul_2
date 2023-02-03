import turtle

turtle.shape("turtle")
color = ["red", "green", "yellow"]


for i in range(3):
    turtle.begin_fill()
    turtle.color("black", color[i])
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()
    
turtle.exitonclick()