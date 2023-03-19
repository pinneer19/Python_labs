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
