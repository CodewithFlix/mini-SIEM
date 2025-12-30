from datetime import datetime
from dateutil import parser as dtparser

def parse_syslog_time(line: str, year: int | None = None) -> datetime:
    """
    Syslog biasanya format: 'Dec 30 10:01:12 ...'
    Kita lengkapi year agar jadi timestamp valid.
    """
    year = year or datetime.now().year
    prefix = " ".join(line.split()[:3])  # "Dec 30 10:01:12"
    return dtparser.parse(f"{prefix} {year}")
