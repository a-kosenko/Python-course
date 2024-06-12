import re

GIT_ADD = "Stage all changes or specific file <filename> for the next commit."
GIT_RM_CACHED = "Unstage file <filename> while retaining the changes in the working directory."
GIT_COMMIT = "Commit changes to the repository with a descriptive message <commit message>."
GIT_PUSH = "Upload your commits to the remote repository."
GIT_STASH = "Temporarily shelves changes in your working directory so you can work on a different task."
GIT_STASH_PUSH = "Stashes changes with a custom message <stash message> for easy identification."
GIT_STASH_APPLY = "Applies the most recently stashed changes."
GIT_STASH_APPLY_NAMED = "Applies the stashed changes with the specified name <stash-name>."
INVALID_COMMAND = "Invalid Command"


def git_command_simulator(command: str) -> str:
    command_parts = command.split()
    match command_parts:
        case ["git", "add", filename]:
            return GIT_ADD.replace("<filename>", filename)
        case ["git", "rm", "--cached", filename]:
            return GIT_RM_CACHED.replace("<filename>", filename)
        case ["git", "commit", "-m", message]:
            return GIT_COMMIT.replace("<commit message>", message)
        case ["git", "push"]:
            return GIT_PUSH
        case ["git", "stash"] if len(command_parts) == 2:
            return GIT_STASH
        case ["git", "stash", "push", "-m", message]:
            return GIT_STASH_PUSH.replace("<stash message>", message)
        case ["git", "stash", "apply"] if len(command_parts) == 3:
            return GIT_STASH_APPLY
        case ["git", "stash", "apply", stash_name]:
            return GIT_STASH_APPLY_NAMED.replace("<stash-name>", stash_name)
        case _:
            return INVALID_COMMAND


# Example usage
print(git_command_simulator("git stash apply 'stashname'"))
