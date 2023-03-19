import re
from constants import ABBREVIATIONS


def amount_of_sentences(text: str):
    sentences = re.findall(r"[.!?]+", text)
    amount = len(sentences)

    for abbreviation in ABBREVIATIONS:
        amount -= text.count(abbreviation) * abbreviation.count('.')

    return amount


def amount_of_non_declarative_sentences(text: str):
    return len(re.split(r"[!?]+", text)) - 1


def average_sentence_length(text: str):
    sentences_amount = amount_of_sentences(text)
    return len(text.split()) / sentences_amount
