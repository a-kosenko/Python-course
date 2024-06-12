import re


def extract_value_by_key(log_line, key):
    pattern = fr"\[{key}:(.*?)\]"
    match = re.search(pattern, log_line)
    return match.group(1)
