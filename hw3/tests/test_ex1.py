import unittest
from solution.ex1 import format_data


class TestTypeCheckDecorator(unittest.TestCase):
    def test_correct_types(self):
        self.assertEqual(
            format_data("Alice", 30, {"key": "value"}, other_info=1234),
            "Name: Alice, Age: 30, Data: value, Other Info : 1234"
        )

    def test_incorrect_type_for_age(self):
        with self.assertRaises(TypeError) as context:
            format_data("Alice", "thirty", {"key": "value"})
        self.assertIn("Argument 'age' must be of type <class 'int'>, got <class 'str'> instead.", str(context.exception))


# Running the tests
if __name__ == '__main__':
    unittest.main()