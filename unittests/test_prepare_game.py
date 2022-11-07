import unittest
import prepare_game

word1 = 'going'
word2 = 'hates'
word3 = 'quote'

class TestStringMethods(unittest.TestCase):
    def test_easy(self):
        possible_words, word_guesses = prepare_game.get_words('easy', testmode=True)
        self.assertIn(word1, possible_words)
        self.assertIn(word2, possible_words)
        self.assertIn(word3, possible_words)
        self.assertNotIn(word1, word_guesses)
        self.assertIn(word2, word_guesses)
        self.assertNotIn(word3, word_guesses)

    def test_medium(self):
        possible_words, word_guesses = prepare_game.get_words('medium', testmode=True)
        self.assertIn(word1, possible_words)
        self.assertIn(word2, possible_words)
        self.assertIn(word3, possible_words)
        self.assertNotIn(word1, word_guesses)
        self.assertIn(word2, word_guesses)
        self.assertIn(word3, word_guesses)

    def test_hard(self):
        possible_words, word_guesses = prepare_game.get_words('hard', testmode=True)
        self.assertIn(word1, possible_words)
        self.assertIn(word2, possible_words)
        self.assertIn(word3, possible_words)
        self.assertIn(word1, word_guesses)
        self.assertIn(word2, word_guesses)
        self.assertIn(word3, word_guesses)

if __name__ == '__main__':
    unittest.main()