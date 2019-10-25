import math

shape = input('Please enter a shape: ')

if shape == 'circle':
    rad = float(input('Please enter the radius of the cirlce: '))

    cirum = 2 * math.pi * rad
    area = math.pi * pow(rad, 2)

    print('The circumference of the circle is: ')
    print(cirum)
    print('The area of the cirlce is: ')
    print(area)
elif shape == 'square':
    width = float(input('Please enter the width of the square: '))

    para = 4 * width
    area = width * width

    print('The parameter of the square is: ')
    print(para)
    print('The area of the square is: ')
    print(area)
elif shape == 'rectangle':
    width = float(input('Please enter the width of the rectangle: '))
    height = float(input('Please enter the height of the rectangle: '))

    para = (2 * width) + (2 * height)
    area = width * height

    print('The parameter of the rectangle is: ')
    print(para)
    print('The area of the rectangle is: ')
    print(area)
else:
    print('I don\'t recognize that shape')
