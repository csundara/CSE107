import turtle


def draw(usercom):
    """ reads in list of commands then executes them """
    henery = turtle.Turtle()
    turtles = [henery]
    # turn_flag = 'false'

    for c in usercom:
        com = c.split(' ')
        for t in turtles:
            if com[0] == 'forward':     # moves turtle 100
                t.forward(int(com[1]))
            elif com[0] == 'left':      # turns turtle left
                t.left(int(com[1]))
            elif com[0] == 'right':     # turns turtle right
                t.right(int(com[1]))
            elif com[0] == 'split':
                francis = turtle.Turtle()
                francis.right(int(com[1]))
                turtles.append(francis)
            elif com[0] == 'stop':
                exit()
            else:                    # ignors input because input is invalid
                print('Invalid input, not moving.')


def main():
    # userin = input('Please enter a direction: ')
    text = input('enter file name >>>')
    validInput = False

    while not validInput:
        try:
            with open(text, "r") as f:
                usercom = []
                read = f.readline()
                while read:
                    usercom.append(read)
                    read = f.readline()
                print(usercom)
                draw(usercom)
            validInput = True
        except FileNotFoundError:
            print('file does not exist')


if __name__ == "__main__":
    main()
