import turtle

angle = float(input("Please enter an angle: "))
len = 15

ws = turtle.Screen()
henery = turtle.Turtle()

for i in range(128):
    henery.forward(len)
    henery.right(angle)
    len = len + 1

#henery.done()
ws.done()
