import random


def build_markov(read, last, markov):
    """ sorts words in sentence, read, into dictionary, markov, based on
     preceding word, last """
    for w in read:
        if w not in markov:
            markov[w] = []
        if last != '':
            markov[last].append(w)
        last = w
    return last


def make_sentence(markov):
    """ takes in dictionary, markov, randomly selects a word and builds a
    sentence by randomly selecting the next word from corresponding list then
    finding that word in the dictionary. Stops either at 100 words or word with
    empty word list """
    word = random.choice(list(markov))
    sentence = [word]

    while len(sentence) < 100 or not markov[word]:
        word = random.choice(markov[word])
        sentence.append(word)

    final_sent = ''
    for w in sentence:
        final_sent = final_sent + " " + w
    print(final_sent)


def main():
    text = input('enter file name >>>')
    validInput = False

    while not validInput:
        try:
            with open(text, "r") as f:
                read = f.readline()
                markov = {}
                last = ''

                while read:
                    read.strip('_-()@#$%^&*";:?.,')
                    text = read.split(' ')
                    last = build_markov(text, last, markov)
                    read = f.readline()
                make_sentence(markov)
                # print(markov["when"])
                validInput = True
        except FileNotFoundError:
            print('file does not exist')
            filename = input('Try another file: ')


if __name__ == "__main__":
    main()
