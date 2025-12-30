from collections import defaultdict, deque
from datetime import datetime, timedelta
from typing import Dict, Any, List

class RuleEngine:
    def __init__(self):
        # rolling window failed login per IP (deque timestamps)
        self.failed_by_ip = defaultdict(lambda: deque())

    def run(self, event: Dict[str, Any]) -> List[Dict[str, Any]]:
        alerts: List[Dict[str, Any]] = []

        et = event.get("event_type")
        ts = datetime.fromisoformat(event["timestamp"])
        ip = event.get("ip")

        # RULE 1: SSH brute force >= 3 fails in 60s from same IP
        if et == "ssh_failed_login" and ip:
            window = self.failed_by_ip[ip]
            window.append(ts)

            cutoff = ts - timedelta(seconds=60)
            while window and window[0] < cutoff:
                window.popleft()

            if len(window) >= 3:
                alerts.append({
                    "timestamp": event["timestamp"],
                    "rule": "SSH_BRUTEFORCE",
                    "severity": "high",
                    "ip": ip,
                    "user": event.get("user"),
                    "message": f"Possible SSH brute force from {ip} ({len(window)} fails/60s)",
                    "event_raw": event.get("raw", ""),
                })

        # RULE 2: Sudo failures are high severity
        if et in ("sudo_auth_failure", "sudo_incorrect_password_attempts"):
            alerts.append({
                "timestamp": event["timestamp"],
                "rule": "SUDO_AUTH_FAILURE",
                "severity": "high",
                "ip": event.get("ip"),
                "user": event.get("user"),
                "message": "Sudo authentication failure detected",
                "event_raw": event.get("raw", ""),
            })

        return alerts
