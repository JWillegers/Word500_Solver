import unittest
import lookup_table

class TestStringMethods(unittest.TestCase):
    def test_charlist_from_word(self):
        expected = ('house', [('h', 0), ('o', 1), ('u', 2), ('s', 3), ('e', 4)])
        actual = lookup_table.get_charlist_from_word(['pilot', 'house'], 1)
        self.assertEqual(expected, actual)

    def test_calculate_value_005(self):
        word1 = [('h', 0), ('o', 1), ('u', 2), ('s', 3), ('e', 4)]
        word2 = [('t', 0), ('a', 1), ('l', 2), ('k', 3), ('y', 4)]
        self.assertEqual('005', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_104(self):
        word1 = [('s', 0), ('t', 1), ('e', 2), ('e', 3), ('l', 4)]
        word2 = [('s', 0), ('o', 1), ('n', 2), ('g', 3), ('s', 4)]
        self.assertEqual('104', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_203(self):
        word1 = [('s', 0), ('t', 1), ('e', 2), ('e', 3), ('l', 4)]
        word2 = [('s', 0), ('t', 1), ('o', 2), ('r', 3), ('k', 4)]
        self.assertEqual('203', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_302(self):
        word1 = [('s', 0), ('t', 1), ('e', 2), ('e', 3), ('l', 4)]
        word2 = [('s', 0), ('t', 1), ('e', 2), ('a', 3), ('m', 4)]
        self.assertEqual('302', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_401(self):
        word1 = [('s', 0), ('t', 1), ('e', 2), ('e', 3), ('l', 4)]
        word2 = [('s', 0), ('t', 1), ('e', 2), ('e', 3), ('r', 4)]
        self.assertEqual('401', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_014_no_doubles(self):
        word1 = [('t', 0), ('a', 1), ('k', 2), ('e', 3), ('s', 4)]
        word2 = [('b', 0), ('e', 1), ('e', 2), ('c', 3), ('h', 4)]
        self.assertEqual('014', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_023_no_doubles(self):
        word1 = [('t', 0), ('a', 1), ('k', 2), ('e', 3), ('s', 4)]
        word2 = [('s', 0), ('k', 1), ('i', 2), ('l', 3), ('l', 4)]
        self.assertEqual('023', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_032_no_doubles(self):
        word1 = [('t', 0), ('a', 1), ('k', 2), ('e', 3), ('s', 4)]
        word2 = [('g', 0), ('u', 1), ('e', 2), ('s', 3), ('t', 4)]
        self.assertEqual('032', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_041_no_doubles(self):
        word1 = [('t', 0), ('a', 1), ('k', 2), ('e', 3), ('s', 4)]
        word2 = [('s', 0), ('t', 1), ('a', 2), ('r', 3), ('e', 4)]
        self.assertEqual('041', lookup_table.calculate_value(word1, word2))

    def test_calculate_value_050_no_doubles(self):
        word1 = [('t', 0), ('a', 1), ('k', 2), ('e', 3), ('s', 4)]
        word2 = [('s', 0), ('t', 1), ('a', 2), ('k', 3), ('e', 4)]
        self.assertEqual('050', lookup_table.calculate_value(word1, word2))

    def test_green_doubles(self):
        word1 = [('s', 0), ('o', 1), ('n', 2), ('g', 3), ('s', 4)]
        word2 = [('s', 0), ('t', 1), ('a', 2), ('k', 3), ('e', 4)]
        self.assertEqual('104', lookup_table.calculate_value(word1, word2))

        word3 = [('s', 0), ('t', 1), ('o', 2), ('r', 3), ('m', 4)]
        word4 = [('s', 0), ('a', 1), ('c', 2), ('k', 3), ('s', 4)]
        self.assertEqual('104', lookup_table.calculate_value(word3, word4))

    def test_double_yellows(self):
        word1 = [('p', 0), ('e', 1), ('r', 2), ('e', 3), ('z', 4)]
        word2 = [('s', 0), ('k', 1), ('e', 2), ('l', 3), ('e', 4)]
        self.assertEqual('023', lookup_table.calculate_value(word1, word2))

        word3 = [('p', 0), ('e', 1), ('r', 2), ('e', 3), ('z', 4)]
        word4 = [('s', 0), ('n', 1), ('a', 2), ('k', 3), ('e', 4)]
        self.assertEqual('014', lookup_table.calculate_value(word3, word4))

    def test_1_green_1_yellow(self):
        word1 = [('s', 0), ('n', 1), ('a', 2), ('k', 3), ('e', 4)]
        word2 = [('h', 0), ('o', 1), ('u', 2), ('s', 3), ('e', 4)]
        self.assertEqual('113', lookup_table.calculate_value(word1, word2))

        word3 = [('s', 0), ('n', 1), ('a', 2), ('k', 3), ('e', 4)]
        word4 = [('b', 0), ('r', 1), ('a', 2), ('s', 3), ('s', 4)]
        self.assertEqual('113', lookup_table.calculate_value(word3, word4))

if __name__ == '__main__':
    unittest.main()