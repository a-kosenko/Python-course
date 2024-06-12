import unittest
from solution.ex5 import solve_quadratic


class TestExtractValue(unittest.TestCase):

    def test_solve1(self):
        a, b, c = 1, -5, 6

        expected_output = 3, 2
        actual_result = solve_quadratic(a, b, c)
        self.assertEqual(actual_result, expected_output)

    def test_solve2(self):
        a, b, c = 2, -10, 12

        expected_output = 3, 2
        actual_result = solve_quadratic(a, b, c)
        self.assertEqual(actual_result, expected_output)


if __name__ == '__main__':
    unittest.main()
