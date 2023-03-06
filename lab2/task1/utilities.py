import re


def amount_of_sentences(text: str):
    return len(re.split(r"[.!?]+", text)) - 1
