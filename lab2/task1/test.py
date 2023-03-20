import unittest
from utilities import amount_of_sentences, amount_of_non_declarative_sentences, \
    average_sentence_length, average_word_length, top_k_repeated_n_grams


class TestCountSentences(unittest.TestCase):

    def test_empty_text(self):
        text = ""
        expected = 0
        actual = amount_of_sentences(text)
        self.assertEqual(expected, actual)

    def test_several_symbols(self):
        text = "This text has several symbols in the end?! Or this!!! And let's add some dots..."
        expected = 3
        actual = amount_of_sentences(text)
        self.assertEqual(expected, actual)

    def test_abbreviations(self):
        text = "This text has 5 different abbreviations. For example, U.S.A., U.K., Dr., Mrs., and etc. should not be " \
               "counted as sentence endings."
        expected = 2
        actual = amount_of_sentences(text)
        self.assertEqual(expected, actual)


class TestCountNonDeclarative(unittest.TestCase):
    def test_empty_text(self):
        text = ""
        expected = 0
        actual = amount_of_non_declarative_sentences(text)
        self.assertEqual(expected, actual)

    def test_several_symbols(self):
        text = "This text has several symbols in the end?! Or this!!! And let's add some dots..."
        expected = 2
        actual = amount_of_non_declarative_sentences(text)
        self.assertEqual(expected, actual)

    def test_declarative_sentence(self):
        text = "This sentence is declarative."
        expected = 0
        actual = amount_of_non_declarative_sentences(text)
        self.assertEqual(expected, actual)

    def test_abbreviations(self):
        text = "This text has 5 different abbreviations! For example, U.S.A., U.K., Dr., Mrs., and etc. should not be " \
               "counted as sentence endings."
        expected = 1
        actual = amount_of_non_declarative_sentences(text)
        self.assertEqual(expected, actual)


class TestAverageSentenceLength(unittest.TestCase):
    def test_empty_text(self):
        text = ""
        expected = 0
        actual = average_sentence_length(text)
        self.assertEqual(expected, actual)

    def test_abbreviations(self):
        text = "She works as assistant for a famous C.E.O. in NYC. They visited the U.S.A. and the U.K. last year."
        expected = 35
        actual = average_sentence_length(text)
        self.assertEqual(expected, actual)

    def test_number_sentence(self):
        text = "I have 6546971 likes."
        expected = 10
        actual = average_sentence_length(text)
        self.assertEqual(expected, actual)


class TestAverageWordLength(unittest.TestCase):
    def test_empty_text(self):
        text = ""
        expected = 0
        actual = average_sentence_length(text)
        self.assertEqual(expected, actual)

    def test_abbreviations(self):
        text = "She works as assistant for a famous C.E.O. in NYC. They visited the U.S.A. and the U.K. last year."
        expected = 2.92
        actual = round(average_word_length(text), 2)
        self.assertEqual(expected, actual)

    def test_number_sentence(self):
        text = "I have 6546971 likes."
        expected = 3.33
        actual = round(average_word_length(text), 2)
        self.assertEqual(expected, actual)


class TestCountNGrams(unittest.TestCase):

    def test_empty_text(self):
        n, k = 10, 10
        text = ""
        expected = "N can't be greater than words amount!!!"
        actual = top_k_repeated_n_grams(text, k, n)
        self.assertEqual(expected, actual)

    def test_one_sentence(self):
        n, k = 2, 1
        text = "Hello world!"
        expected = [('Hello world', 1)]
        actual = top_k_repeated_n_grams(text, k, n)
        self.assertEqual(expected, actual)

    def test_zero_grams(self):
        n, k = 0, 10
        text = "Hello world!"
        expected = []
        actual = top_k_repeated_n_grams(text, k, n)
        self.assertEqual(expected, actual)

    def test_sentence(self):
        n, k = 3, 10
        text = "Python has many built-in data structures, such as lists, tuples, sets, and dictionaries, that make it " \
               "easy to manipulate and store data."
        expected = [
            ('Python has many', 1), ('has many built', 1),
            ('many built in', 1), ('built in data', 1),
            ('in data structures', 1), ('data structures such', 1),
            ('structures such as', 1), ('such as lists', 1),
            ('as lists tuples', 1), ('lists tuples sets', 1)
        ]
        actual = top_k_repeated_n_grams(text, k, n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
