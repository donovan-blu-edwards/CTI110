# Donovan Edwards
# Apr. 21st 2026
# P4LAB1
# Python script for drawing houses

import turtle

turtle.bgcolor("#5ba8ff")
turtle.pensize(15)

squareSize = 200

turtle.color("#151515")
squa_i = 0
while squa_i < 4:
    turtle.forward(squareSize)
    turtle.right(90)
    squa_i += 1

triangleSize = 350

turtle.forward((squareSize / 2) - (triangleSize / 2))

turtle.color("#024aca")
tri_i = 0
while tri_i < 3:
    turtle.forward(triangleSize)
    turtle.left(120)
    tri_i += 1

turtle.exitonclick()
