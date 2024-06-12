import unittest
from solution.ex1 import analyze_log_content


class TestAnalyzeLogContent(unittest.TestCase):

    def test_analyze_log_content(self):
        log_content = """
        2024-04-29 15:45:00,089 INFO [name:starwars_engine][pid:2995] Message one
        2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
        2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
        2024-04-29 15:46:00,789 INFO [name:starwars_engine][pid:2998] All systems go
        """
        expected = {'Error': 1, 'Warning': 1, 'Info': 2}
        result = analyze_log_content(log_content)
        self.assertEqual(result, expected)

    def test_empty_log_content(self):
        log_content = ""
        expected = {'Error': 0, 'Warning': 0, 'Info': 0}
        result = analyze_log_content(log_content)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()