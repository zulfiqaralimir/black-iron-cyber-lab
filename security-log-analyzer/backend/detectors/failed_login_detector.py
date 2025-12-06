import re

# Common patterns for failed logins
FAILED_LOGIN_PATTERNS = [
    r"Failed password for",
    r"authentication failure",
    r"invalid user",
    r"login failed",
    r"incorrect password"
]

def detect_failed_logins(log_lines):
    """
    Scans log lines for failed login attempts.

    Returns:
        A list of failed login entries.
    """
    failed_events = []

    for line in log_lines:
        for pattern in FAILED_LOGIN_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                failed_events.append(line.strip())
                break

    return failed_events
