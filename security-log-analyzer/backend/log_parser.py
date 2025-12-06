import os
from backend.detectors.failed_login_detector import detect_failed_logins


def load_log_file(file_path):
    """Reads log file and returns a list of lines."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", errors="ignore") as f:
        return f.readlines()


def analyze_log(file_path):
    """
    Main analysis function.
    Loads log lines and runs all detectors.
    Returns a dictionary with results.
    """

    log_lines = load_log_file(file_path)

    results = {
        "failed_logins": detect_failed_logins(log_lines),
    }

    return results
