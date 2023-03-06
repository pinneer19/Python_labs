from utilities import amount_of_sentences


def main():
    text = input('Enter your text: ')
    print('Amount of sentences in the text: ', amount_of_sentences(text))


if __name__ == '__main__':
    main()
