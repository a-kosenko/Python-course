import unittest
from solution.ex4 import binary_to_decimal


class TestExtractValue(unittest.TestCase):

    def test_10(self):
        binary_input = "1010"

        expected_output = 10
        actual_result = binary_to_decimal(binary_input)
        self.assertEqual(actual_result, expected_output)

    def test_255(self):
        binary_input = "11111111"

        expected_output = 255
        actual_result = binary_to_decimal(binary_input)
        self.assertEqual(actual_result, expected_output)


if __name__ == '__main__':
    unittest.main()