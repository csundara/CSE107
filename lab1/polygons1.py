import turtle
#import random

len = input('Please enter a positive integer: ')
len = int(len)

window = turtle.Screen()
window.setup(width=1.0, height=1.0, startx=None, starty=None)
henery = turtle.Turtle()

x = -5*len - 10
y = 0
henery.penup()
henery.setposition(x, y)
henery.pendown()

for j in range(3,8):
    ang_in = (j-2)*180/j
    angle = 180 - ang_in

    for i in range(j):
        henery.forward(len)
        henery.left(angle)

    x = x + 2.5*len
    henery.penup()
    henery.setposition(x, y)
    henery.pendown()

#henery.done()
