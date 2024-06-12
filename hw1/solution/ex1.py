def extract_pid(log_line):
    start = log_line.find("[pid:") + 5
    end = log_line.find("]", start)
    pid = int(log_line[start:end])
    return pid