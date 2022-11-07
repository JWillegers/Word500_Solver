import unittest
import prepare_game

word1 = 'going'
word1tuple = ['going', 4]
word2 = 'hates'
word2tuple = ['hates', 5]
word3 = 'quote'
word3tuple = ['quote', 5]

class TestStringMethods(unittest.TestCase):
    def test_easy(self):
        possible_words, word_guesses = prepare_game.get_words('easy', testmode=True)
        self.assertIn(word1, possible_words)
        self.assertIn(word2, possible_words)
        self.assertIn(word3, possible_words)
        self.assertNotIn(word1tuple, word_guesses)
        self.assertIn(word2tuple, word_guesses)
        self.assertNotIn(word3tuple, word_guesses)

    def test_medium(self):
        possible_words, word_guesses = prepare_game.get_words('medium', testmode=True)
        self.assertIn(word1, possible_words)
        self.assertIn(word2, possible_words)
        self.assertIn(word3, possible_words)
        self.assertNotIn(word1tuple, word_guesses)
        self.assertIn(word2tuple, word_guesses)
        self.assertIn(word3tuple, word_guesses)

    def test_hard(self):
        possible_words, word_guesses = prepare_game.get_words('hard', testmode=True)
        self.assertIn(word1, possible_words)
        self.assertIn(word2, possible_words)
        self.assertIn(word3, possible_words)
        self.assertIn(word1tuple, word_guesses)
        self.assertIn(word2tuple, word_guesses)
        self.assertIn(word3tuple, word_guesses)

if __name__ == '__main__':
    unittest.main()