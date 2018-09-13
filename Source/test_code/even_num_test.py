import unittest
import even_num

class TestEvenNum(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_odd(self):
        odds = [1, 3, 5, 7, 9]
        result = even_num.even_number(odds)
        self.assertEqual(result, [])

    def test_evens(self):
        evens = [4, 129586, 68974, 12034, 3256, 129302]
        result = even_num.even_number(evens)
        self.assertEqual(result, evens)

if __name__ == '__main__':
    unittest.main()
