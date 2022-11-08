import unittest

import reduce_words


class TestStringMethods(unittest.TestCase):
    def test_5_green(self):
        word_found, possible_words = reduce_words.process_guess('house 5 0 0', ['pilot', 'house', 'quote'])
        self.assertTrue(word_found)
        self.assertEqual('house', possible_words)

    def test_5_red(self):
        word_found, possible_words = reduce_words.process_guess('award 0 0 5', ['award', 'pilot', 'house', 'quote'])
        self.assertFalse(word_found)
        self.assertEqual(['pilot', 'house', 'quote'], possible_words)

    def test_1_green(self):
        word_found, possible_words = reduce_words.process_guess('steel 1 0 4', ['songs', 'stork', 'steam', 'steer'])
        self.assertFalse(word_found)
        self.assertEqual(['songs'], possible_words)

    def test_2_green(self):
        word_found, possible_words = reduce_words.process_guess('steel 2 0 3', ['songs', 'stork', 'steam', 'steer'])
        self.assertFalse(word_found)
        self.assertEqual(['stork'], possible_words)

    def test_3_green(self):
        word_found, possible_words = reduce_words.process_guess('steel 3 0 2', ['songs', 'stork', 'steam', 'steer'])
        self.assertFalse(word_found)
        self.assertEqual(['steam'], possible_words)

    def test_4_green(self):
        word_found, possible_words = reduce_words.process_guess('steel 4 0 1', ['songs', 'stork', 'steam', 'steer'])
        self.assertFalse(word_found)
        self.assertEqual(['steer'], possible_words)

    def test_1_yellow_no_doubles(self):
        word_found, possible_words = reduce_words.process_guess('takes 0 1 4', ['pilot', 'skill', 'guest', 'stare', 'steak', 'token', 'beech'])
        self.assertFalse(word_found)
        self.assertEqual(['pilot', 'beech'], possible_words)

    def test_2_yellow_no_doubles(self):
        word_found, possible_words = reduce_words.process_guess('takes 0 2 3', ['pilot', 'skill', 'guest', 'stare', 'steak', 'token'])
        self.assertFalse(word_found)
        self.assertEqual(['skill'], possible_words)

    def test_3_yellow_no_doubles(self):
        word_found, possible_words = reduce_words.process_guess('takes 0 3 2', ['pilot', 'skill', 'guest', 'stare', 'steak', 'token'])
        self.assertFalse(word_found)
        self.assertEqual(['guest'], possible_words)

    def test_4_yellow_no_doubles(self):
        word_found, possible_words = reduce_words.process_guess('takes 0 4 1', ['pilot', 'skill', 'guest', 'stare', 'steak', 'token'])
        self.assertFalse(word_found)
        self.assertEqual(['stare'], possible_words)

    def test_5_yellow_no_doubles(self):
        word_found, possible_words = reduce_words.process_guess('takes 0 5 0', ['pilot', 'skill', 'guest', 'stare', 'steak', 'token'])
        self.assertFalse(word_found)
        self.assertEqual(['steak'], possible_words)

    def test_green_doubles(self):
        word_found, possible_words = reduce_words.process_guess('songs 1 0 4', ['steel', 'stork', 'steam', 'steer', 'spins'])
        self.assertFalse(word_found)
        self.assertEqual(['steel', 'steam', 'steer'], possible_words)

        word_found, possible_words = reduce_words.process_guess('songs 1 0 4', ['bears', 'silly',   'storm', 'sacks'])
        self.assertFalse(word_found)
        self.assertEqual(['bears', 'silly'], possible_words)

    def test_yellow_doubles(self):
        word_found, possible_words = reduce_words.process_guess('perez 0 2 3', ['skele', 'sekle', 'sklee', 'sacks', 'snake'])
        self.assertFalse(word_found)
        self.assertEqual(['skele'], possible_words)

    def test_1_green_1_yellow(self):
        word_found, possible_words = reduce_words.process_guess('snake 1 1 3', ['house', 'rains', 'wrong', 'brass', 'skill'])
        self.assertFalse(word_found)
        self.assertEqual(['house', 'brass', 'skill'], possible_words)


if __name__ == '__main__':
    unittest.main()
