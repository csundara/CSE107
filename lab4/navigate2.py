import turtle


def main():
    henery = turtle.Turtle()
    userin = input('Please enter directions: ')

    direction = userin.split(',')

    # while userin != 'stop':
    for inst in range(len(direction)):
        if direction[inst] == 'forward':     # moves turtle 100
            henery.forward(100)
        elif direction[inst] == 'left':      # turns turtle left
            # angle = input('How many degrees? ')  # determines how far to
            # turn turtle
            inst = inst + 1
            angle = direction[inst]
            # turns turtle if user input is proper
            if angle.isdigit():
                henery.left(int(angle))
            else:
                # ignors input because input is invalid
                print('Invalid number, not moving.')
        elif direction[inst] == 'right':     # turns turtle right
            # angle = input('How many degrees? ')
            # # determines how far to turn turtle
            inst = inst + 1
            angle = direction[inst]
            # turns turtle if user input is proper
            if angle.isdigit():
                henery.right(int(angle))
            else:
                # ignors input because input is invalid
                print('Invalid number, not moving.')
        elif direction[inst] == 'stop' or direction[inst].isdigit():
            continue
        else:
            # ignors input because input is invalid
            print('Invalid input, not moving.')

        # userin = input('Please enter a direction: ')


if __name__ == "__main__":
    main()
