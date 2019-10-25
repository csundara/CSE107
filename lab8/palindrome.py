# import


def letter_comp(word):
    """ Takes in string, compairs first and last characters. If they match call
    function on substring with first and last letters removed, if string is
    less than 2 characters return True, and if letters don't match return
    False """
    if len(word) == 1 or len(word) == 0:
        return True
    elif word[0] == word[-1]:
        return letter_comp(word[1:-1])
    else:
        return False


def main():
    word = input('Is this a palindrome? : ')
    while word != 'stop':
        palin = letter_comp(word)
        print(palin)
        word = input('Is this a palindrome? : ')


if __name__ == "__main__":
    main()
