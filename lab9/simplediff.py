# import
def col_match(sent1, sent2):
    """ takes in 2 strings and returns the number column where they start
     to differ """

    for i in range(len(sent1)):
        if sent1[i] != sent2[i]:
            return i


def print_lines(f1, f2, row):
    """ Prints 2 lines read from different files that are different """
    column = col_match(f1, f2)
    print('{}c{}'.format(row, column))
    print(f1)
    print('---')
    print(f2)


def main():
    file1 = input('Enter file name 1 >>> ')
    file2 = input('Enter file name 2 >>> ')
    validInput = False

    while not validInput:
        try:
            with open(file1, "r") as read1:
                with open(file2, "r") as read2:
                    linef1 = read1.readline()
                    linef2 = read2.readline()
                    row = 0

                    while linef1 and linef2:
                        row = row + 1
                        if linef1 != linef2:
                            print_lines(linef1, linef2, row)
                        linef1 = read1.readline()
                        linef2 = read2.readline()
            validInput = True
        except FileNotFoundError:
            print('file does not exist')
            filename = input('Try another file: ')


if __name__ == "__main__":
    main()
