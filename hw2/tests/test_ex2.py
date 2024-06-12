import unittest
from solution.ex2 import calculate


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate('add', [1, 2]), 3)

    def test_subtract(self):
        self.assertEqual(calculate('subtract', [5, 2]), 3)

    def test_multiply(self):
        self.assertEqual(calculate('multiply', [3, 2]), 6)

    def test_divide(self):
        self.assertEqual(calculate('divide', [8, 2]), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(Exception):
            calculate('divide', [5, 0])


if __name__ == '__main__':
    unittest.main()
