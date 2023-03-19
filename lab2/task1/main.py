from utilities import amount_of_sentences, amount_of_non_declarative_sentences, \
    average_sentence_length, average_word_length
import re


def main():
    text = input('Enter your text: ')
    print('Amount of sentences in the text: ', amount_of_sentences(text))
    print('Amount of non-declarative sentences in the text: ', amount_of_non_declarative_sentences(text))
    print('Average length of the sentence in characters(words count only): ', average_sentence_length(text))
    print('Average length of the word in the text: ', average_word_length(text))


if __name__ == '__main__':
    main()
