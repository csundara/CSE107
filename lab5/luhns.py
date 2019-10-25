# Note: check lists formed in double_dig and single_dig to make sure
# collecting and parsing numbers correctly


def get_dig(num):
    """ takes a string and returns list of it's charaters """
    new_dig = []
    for c in range(len(num)):
        new_dig.append(num[c])
    return new_dig


def double_dig(lst):
    """ takes list of credit card digits and returns list of digits to be
    doubled """
    doub = []

    start = len(lst) - 2
    if start % 2 == 1:
        end = 0
    else:
        end = -1
    for i in range(start, end, -2):
        doub.append(int(lst[i]))
    return doub


def single_dig(lst):
    """ takes list of credit card digits and returns list of digits not to be
     doubled """
    sing = []
    start = len(lst) - 1
    if start % 2 == 1:
        end = 0
    else:
        end = -1
    for i in range(start, end, -2):
        sing.append(int(lst[i]))
    return sing


def sum(lst):
    """ takes list of numbers and returns sum """
    sum = 0
    for i in lst:
        sum = sum + i
    return sum


def validate(creditCard):
    """ takes in a credit card number and calidates it """
    digits = get_dig(creditCard)

    doubs = double_dig(digits)
    singles = single_dig(digits)

    for d in range(len(doubs)):
        doubs[d] = 2 * doubs[d]

    new_dig = []
    for c in range(len(doubs)):
        dig = [int(dig) for dig in str(doubs[c])]
        if isinstance(dig, int):
            new_dig.append(dig)
        else:
            for i in dig:
                new_dig.append(i)

    for i in singles:
        new_dig.append(i)
    sum_dig = sum(new_dig)

    valid = True
    if sum_dig % 10 == 0:
        print('Valid Card')
    else:
        # print('NOT Valid Card')
        valid = False

    return valid


def main():
    creditCard = input('Please enter the credit card number: ')
    # creditCard = '6767676767'


if __name__ == "__main__":
    main()
