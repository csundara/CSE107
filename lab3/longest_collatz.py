import collatz

def main():
    n = 1000000
    #n = 100
    #n = 10
    greatest = 0
    great_len = 0

    for i in range(1, n):
        len = collatz.collatz_len(i)
        if len > great_len:
            great_len = len
            greatest = i

    print('{} has the longest collatz sequence for all numbers less then {}'.format(greatest, n))
    print("Length of Collatz sequence: {}".format(great_len))

if __name__ == "__main__":
    main()
