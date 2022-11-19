import unittest
import pandas as pd
import solver


def create_test_table():
    d = {'house': ['500', '014', '014'], 'pilot': ['014', '500', '005'], 'bread': ['014', '005', '500'], 'entropy': [10, 10, 10]}
    test_table = pd.DataFrame(data=d, index=['house', 'pilot', 'bread'])
    return test_table

class TestStringMethods(unittest.TestCase):
    def test_014(self):
        tt = create_test_table()
        tt = solver.process_guess('house', 0, 1, 4, tt)
        self.assertFalse('house' in tt)
        self.assertTrue('pilot' in tt)
        self.assertTrue('bread' in tt)
        self.assertTrue('entropy' in tt)
        self.assertFalse('house' in tt.index)
        self.assertTrue('pilot' in tt.index)
        self.assertTrue('bread' in tt.index)
        self.assertEqual(1, tt.at['pilot', 'entropy'])
        self.assertEqual(1, tt.at['bread', 'entropy'])

    def test_500(self):
        tt = create_test_table()
        tt = solver.process_guess('house', 5, 0, 0, tt)
        self.assertTrue('house' in tt)
        self.assertFalse('pilot' in tt)
        self.assertFalse('bread' in tt)
        self.assertTrue('entropy' in tt)
        self.assertTrue('house' in tt.index)
        self.assertFalse('pilot' in tt.index)
        self.assertFalse('bread' in tt.index)
        self.assertEqual(0, tt.at['house', 'entropy'])


if __name__ == '__main__':
    unittest.main()
