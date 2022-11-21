import unittest
import solver
from preparation import lookup_table


class TestStringMethods(unittest.TestCase):
    def test(self):
        words_still_possible = {'round': 2.66, 'rownd': 2.66, 'sownd': 2.66, 'gourd': 2.56, 'sound': 2.41, 'hoagy': 1.91, 'coady': 1.7, 'vodka': 1.22}
        lt = lookup_table.load_lookup_table(False, True)
        wsp = solver.process_guess('round', 4, 0, 1, lt, words_still_possible)
        self.assertEqual(1.0, wsp['sound'])

if __name__ == '__main__':
    unittest.main()
