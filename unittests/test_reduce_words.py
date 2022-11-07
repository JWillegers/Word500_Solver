import unittest

import reduce_words


class TestStringMethods(unittest.TestCase):
    def test_5_green(self):
        word_found, possible_words = reduce_words.process_guess('house 5 0 0', ['pilot, house, quote'])
        self.assertTrue(word_found)
        self.assertEqual(possible_words, 'house')

    def test_5_red(self):
        word_found, possible_words = reduce_words.process_guess('award 0 0 5', ['award', 'pilot, house, quote'])
        self.assertFalse(word_found)
        self.assertEqual(possible_words, ['pilot, house, quote'])

    def test_1_green(self):
        word_found, possible_words = reduce_words.process_guess('award 1 0 4', ['award', 'pilot, house, quote'])


if __name__ == '__main__':
    unittest.main()