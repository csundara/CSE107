import math

num = float(input('Enter a number to use: '))
opt = input('Select an operation: sqrt (s), arcsin (a), arccos (c), arctan (t): ')

if opt == 's':
    result = math.sqrt(num)
    print('The square root of the input is ')
    print(result)
elif num < -1 or num > 1:
    print('Input should be between -1 and 1')
elif opt == 'a':
    result = math.asin(num)
    print('The arcsin of the input is: ')
    print(result)
elif opt == 'c':
    result = math.acos(num)
    print('The arccos of the input is: ')
    print(result)
elif opt == 't':
    result = math.atan(num)
    print('The arctan of the input is: ')
    print(result)
else:
    print('That option does not exist!')
