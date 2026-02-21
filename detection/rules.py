from datetime import timedelta

RULES = [
    {
        "rule_name": "Brute Force Login",
        "event_type": "login_attempt",
        "condition": {
            "status": "failed"
        },
        "threshold": 5,
        "time_window": 120,  # seconds
        "severity": "high"
    },
    {
        "rule_name": "Blacklisted IP Access",
        "event_type": "*",
        "condition": {},
        "threshold": 1,
        "time_window": 1,
        "severity": "critical"
    },
    {
        "rule_name": "Privilege Escalation Attempt",
        "event_type": "sudo_attempt",
        "condition": {},
        "threshold": 3,
        "time_window": 300,
        "severity": "medium"
    }
]