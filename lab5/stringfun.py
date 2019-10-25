
def ends():
    """ no parameters, takes user input and returns first 2 elements and last
     2 elements """
    userin = input('Enter a string >>> ')
    new = userin[0:2] + userin[-2] + userin[-1]
    print(new)


def mix():
    """ no parameters, takes in 2 stings and swaps first 2 elements """
    usera = input('String a >>> ')
    userb = input('String b >>> ')
    starta = usera[:2]
    usera = usera.replace(starta, userb[:2])
    userb = userb.replace(userb[:2], starta)

    # print(starta)
    print(usera)
    print(userb)


def main():
    ends()
    mix()


if __name__ == "__main__":
    main()
