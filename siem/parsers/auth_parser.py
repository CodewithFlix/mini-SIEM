import re
from typing import Optional, Dict, Any
from siem.utils.time import parse_syslog_time

SSH_FAIL = re.compile(r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")
SSH_OK = re.compile(r"Accepted password for (?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")
SUDO_FAIL = re.compile(r"sudo: pam_unix\(sudo:auth\): authentication failure;.*user=(?P<user>\S+)")
SUDO_INCORRECT = re.compile(r"sudo: (?P<actor>\S+) : (?P<count>\d+) incorrect password attempts .* USER=(?P<user>\S+) ; COMMAND=(?P<cmd>.+)$")

def parse_auth_line(line: str) -> Optional[Dict[str, Any]]:
    ts = parse_syslog_time(line)

    event: Dict[str, Any] = {
        "timestamp": ts.isoformat(),
        "raw": line,
        "source": "auth.log",
        "event_type": "unknown",
        "user": None,
        "ip": None,
        "details": {},
        "severity": "info",
    }

    m = SSH_FAIL.search(line)
    if m:
        event["event_type"] = "ssh_failed_login"
        event["user"] = m.group("user")
        event["ip"] = m.group("ip")
        event["severity"] = "medium"
        return event

    m = SSH_OK.search(line)
    if m:
        event["event_type"] = "ssh_success_login"
        event["user"] = m.group("user")
        event["ip"] = m.group("ip")
        event["severity"] = "info"
        return event

    m = SUDO_FAIL.search(line)
    if m:
        event["event_type"] = "sudo_auth_failure"
        event["user"] = m.group("user")
        event["severity"] = "high"
        return event

    m = SUDO_INCORRECT.search(line)
    if m:
        event["event_type"] = "sudo_incorrect_password_attempts"
        event["user"] = m.group("user")
        event["details"] = {
            "actor": m.group("actor"),
            "count": int(m.group("count")),
            "command": m.group("cmd").strip(),
        }
        event["severity"] = "high"
        return event

    return None
