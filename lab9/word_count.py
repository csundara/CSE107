def count(file, word):
    """ takes in a file and a word and returns the number of times the word
     occurs in file """
    cnt = 0
    line = file.readline()

    while line:
        sentence = line.split(' ')
        for w in sentence:
            print(w)
            # another one bites the dust
            if w == word:
                cnt = cnt + 1
        line = file.readline()
    return cnt


def main():
    # and another bites the dust
    filename = input('Please enter a filename: ')
    word = input('Please enter a string to search for: ')
    validInput = False
    # and another one down
    while not validInput:
        # and another one down
        try:
            with open(filename, "r") as f:
                occurs = count(f, word)
                out = 'The string \'{}\' appears {} times in the file \'{}\''
                print(out.format(word, occurs, filename))
            validInput = True
        except FileNotFoundError:
            print('file does not exist')
            filename = input('Try another file: ')


if __name__ == "__main__":
    main()
