import unittest
from solution.ex2 import extract_title
# Provide the missing imports


class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        html = "<html><head><title>My Title</title></head><body></body></html>"

        expected_output = "My Title"
        actual_result = extract_title(html)
        self.assertEqual(actual_result, expected_output)

    def test_extract_tittle_with_special_char(self):
        html = "<html><head><title>Title with special characters &amp; symbols!</title></head></html>"

        expected_output = "Title with special characters &amp; symbols!"
        actual_result = extract_title(html)
        self.assertEqual(actual_result, expected_output)

    def test_extract_empty_tittle(self):
        html = "<html><head><title></title></head><body>Empty title here</body></html>"

        expected_output = ""
        actual_result = extract_title(html)
        self.assertEqual(actual_result, expected_output)


if __name__ == '__main__':
    unittest.main()
