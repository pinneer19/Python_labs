from utilities import amount_of_sentences, amount_of_non_declarative_sentences, \
    average_sentence_length, average_word_length, top_k_repeated_n_grams


def main():
    text = input('Enter your text: ')
    print('Amount of sentences in the text: ', amount_of_sentences(text))
    print('Amount of non-declarative sentences in the text: ', amount_of_non_declarative_sentences(text))
    print('Average length of the sentence in characters(words count only): ', average_sentence_length(text))
    print('Average length of the word in the text: ', average_word_length(text))

    try:
        values = input('\nEnter k and n separated by space(or type nothing to use default):\n')
        if values == '':
            k, n = 10, 4
        else:
            k, n = [int(i) for i in values.split(' ')]
    except ValueError:
        print("Error")
    else:
        print('Top k repeated n-grams: ', top_k_repeated_n_grams(text, k, n))


if __name__ == '__main__':
    main()
