import turtle

def main():
    henery = turtle.Turtle()
    userin = input('Please enter a direction: ')

    while userin != 'stop':
        if userin == 'forward':     #moves turtle 100
            henery.forward(100)
        elif userin == 'left':      #turns turtle left
            angle = input('How many degrees? ')     #determines how far to turn turtle
            if angle.isdigit():                     #turns turtle if user input is proper
                henery.left(int(angle))
            else:
                print('Invalid number, not moving.')    #ignors input because input is invalid
        elif userin == 'right':     #turns turtle right
            angle = input('How many degrees? ')     #determines how far to turn turtle
            if angle.isdigit():                     #turns turtle if user input is proper
                henery.right(int(angle))
            else:
                print('Invalid number, not moving.')    #ignors input because input is invalid
        else:                                           #ignors input because input is invalid
            print('Invalid input, not moving.')

        userin = input('Please enter a direction: ')

if __name__ == "__main__":
    main()
