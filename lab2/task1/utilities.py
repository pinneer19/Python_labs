import re


def amount_of_sentences(text: str):
    return len(re.split(r"[.!?]+", text)) - 1


def amount_of_non_declarative_sentences(text: str):
    return len(re.split(r"[!?]+", text)) - 1
