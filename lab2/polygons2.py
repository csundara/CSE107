import turtle

sides = int(input('Please enter number of sides: '))

if sides <= 3:
    print('Invalid Input')
    exit()

sid_len = float(input('Please enter the side-length: '))
henery = turtle.Turtle()
ang = 360/sides

for i in range(sides):
    henery.forward(sid_len)
    henery.right(ang)
