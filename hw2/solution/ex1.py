def analyze_log_content(log_content: str) -> dict:
    log_counts = {'Error': 0, 'Warning': 0, 'Info': 0}
    lines = log_content.splitlines()
    for line in lines:
        match line.split():
            case level if "ERROR" in level:
                log_counts['Error'] += 1
            case level if "WARNING" in level:
                log_counts['Warning'] += 1
            case level if "INFO" in level:
                log_counts['Info'] += 1
            case _:
                continue
    return log_counts
