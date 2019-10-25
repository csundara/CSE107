import turtle


def cesaro_pattern(henery, width, depth):
    """ additional functions """

    if depth == 0:
        henery.forward(width)
    else:
        nwidth = 2 * width / 5
        cesaro_pattern(henery, nwidth, depth - 1)
        henery.right(80)
        cesaro_pattern(henery, nwidth, depth - 1)
        henery.left(160)
        cesaro_pattern(henery, nwidth, depth - 1)
        henery.right(80)
        cesaro_pattern(henery, nwidth, depth - 1)


def main():
    user = input('depth?(or stop to end) ')
    while user != 'stop':
        henery = turtle.Turtle()
        henery.speed('fastest')
        henery.penup()
        henery.setposition(-250, 0)
        henery.pendown()
        # cesaro_pattern(500, 0)
        cesaro_pattern(henery, 500, int(user))
        user = input('depth?(or stop to end) ')


if __name__ == "__main__":
    main()
