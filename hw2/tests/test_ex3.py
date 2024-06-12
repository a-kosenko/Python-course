import unittest
from solution.ex3 import *
from parameterized import parameterized


class TestGitCommandSimulator(unittest.TestCase):
    @parameterized.expand([
        ("git add file.txt", GIT_ADD.replace("<filename>", "file.txt")),
        ("git rm --cached file.txt", GIT_RM_CACHED.replace("<filename>", "file.txt")),
        ("git commit -m 'Initial'", GIT_COMMIT.replace("<commit message>", "'Initial'")),
        ("git push", GIT_PUSH),
        ("git stash", GIT_STASH),
        ("git stash push -m 'Working'", GIT_STASH_PUSH.replace("<stash message>", "'Working'")),
        ("git stash apply", GIT_STASH_APPLY),
        ("git stash apply 'stashname'", GIT_STASH_APPLY_NAMED.replace("<stash-name>", "'stashname'")),
        ("git foo bar", INVALID_COMMAND)
    ])
    def test_git_command_simulator(self, input_command, expected_output):
        self.assertEqual(git_command_simulator(input_command), expected_output)


if __name__ == '__main__':
    unittest.main()