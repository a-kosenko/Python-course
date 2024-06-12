import unittest
from solution.ex3 import extract_value_by_key


class TestExtractValue(unittest.TestCase):

    def test_extract_value(self):
        log_line = "2024-04-29 15:45:00,089 INFO [name:game_loader][user:test_user][error:specialchars!@#$%^&*()]"
        key = "user"

        expected_output = "test_user"
        actual_result = extract_value_by_key(log_line, key)
        self.assertEqual(actual_result, expected_output)

    def test_extract_value_with_special_char(self):
        log_line = "2024-04-29 15:45:00,089 INFO [name:game_loader][user:test_user][error:specialchars!@#$%^&*()]"
        key = "error"

        expected_output = "specialchars!@#$%^&*()"
        actual_result = extract_value_by_key(log_line, key)
        self.assertEqual(actual_result, expected_output)


if __name__ == '__main__':
    unittest.main()
