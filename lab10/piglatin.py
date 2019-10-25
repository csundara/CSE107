# import
def word_trans(word):
    """ takes in a word and returns piglatin translation """
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    if word[0] in vowel:
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'


def sent_trans(sentence):
    """ additional functions """
    # not_letters = [',', '.', '-', ';', '!', '?', '(', ')']
    sentence = sentence.strip(',.-;!?()')
    sent = sentence.split(' ')
    new_sentence = ''

    for w in sent:
        new_sentence = new_sentence + ' ' + word_trans(w)
    return new_sentence


def main():
    book = input('Enter English filename >>> ')
    textfile = input('Enter filename to write to >>> ')
    validInput = False

    while not validInput:
        try:
            with open(book, "r") as f:
                with open(textfile, "w+") as t:
                    sentence = f.readline()
                    while sentence:
                        t.write(sent_trans(sentence))
                        sentence = f.readline()
            print('Done')
            validInput = True
        except FileNotFoundError:
            print('file does not exist')
            filename = input('Try another file: ')


if __name__ == "__main__":
    main()
