import turtle
import random

ws = turtle.Screen()
henery = turtle.Turtle()

for j in range(10):
    step = random.random() * 150 + 50

    for i in range(5):
        henery.forward(step)
        henery.right(144)

    henery.penup()
    henery.setposition(random.random() * 600 - 300, random.random() * 400 - 200)
    henery.pendown()

turtle.done()
