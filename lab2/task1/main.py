from utilities import amount_of_sentences, amount_of_non_declarative_sentences


def main():
    text = input('Enter your text: ')
    print('Amount of sentences in the text: ', amount_of_sentences(text))
    print('Amount of non-declarative sentences in the text: ', amount_of_non_declarative_sentences(text))


if __name__ == '__main__':
    main()
