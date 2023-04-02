import re
from constants import ABBREVIATIONS


def amount_of_sentences(text: str):
    sentences = re.findall(r"[.!?]+", text)
    amount = len(sentences)

    for abbreviation in ABBREVIATIONS:
        amount -= text.count(abbreviation) * abbreviation.count('.')

    return amount


def amount_of_non_declarative_sentences(text: str):
    return len(re.findall(r"[!?]+", text))


def average_sentence_length(text: str):
    words = [word for word in re.findall(r"\b\w+\b", text) if not (str(word).isdigit() or '_' in str(word))]
    words_length = sum(len(word) for word in words)
    sentences = amount_of_sentences(text)

    return words_length / sentences if sentences != 0 else 0


def average_word_length(text: str):
    words = [word for word in re.findall(r"\b\w+\b", text) if not (str(word).isdigit() or '_' in str(word))]
    words_length = sum(len(word) for word in words)

    return words_length / len(words) if len(words) != 0 else 0


def top_k_repeated_n_grams(text: str, k=10, n=4):
    words = re.findall(r"\b\w+\b", text)
    gram_dict = dict()

    if len(words) < n:
        return "N can't be greater than words amount!!!"
    if k == 0 or n == 0:
        return []

    for i in range(len(words) - n + 1):
        current_gram = " ".join(words[i:i + n])
        if current_gram not in gram_dict:
            gram_dict[current_gram] = 1
        else:
            gram_dict[current_gram] += 1

    gram_dict = sorted(gram_dict.items(), reverse=True, key=lambda x: x[1])

    return gram_dict if len(gram_dict) <= k else gram_dict[0:k]


def print_text_statistics():
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
