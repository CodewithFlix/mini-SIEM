import sqlite3
from pathlib import Path
from typing import Dict, Any, Iterable

DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp TEXT,
  source TEXT,
  event_type TEXT,
  user TEXT,
  ip TEXT,
  severity TEXT,
  raw TEXT
);

CREATE TABLE IF NOT EXISTS alerts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp TEXT,
  rule TEXT,
  severity TEXT,
  ip TEXT,
  user TEXT,
  message TEXT,
  event_raw TEXT,
  status TEXT DEFAULT 'open',
  notes TEXT DEFAULT ''
);
"""

class SIEMDB:
    def __init__(self, db_path: str = "data/siem.db"):
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.executescript(DB_SCHEMA)
        self.conn.commit()

    def insert_event(self, e: Dict[str, Any]) -> None:
        self.conn.execute(
            "INSERT INTO events(timestamp, source, event_type, user, ip, severity, raw) VALUES(?,?,?,?,?,?,?)",
            (e["timestamp"], e["source"], e["event_type"], e.get("user"), e.get("ip"), e.get("severity"), e["raw"])
        )
        self.conn.commit()

    def insert_alerts(self, alerts: Iterable[Dict[str, Any]]) -> None:
        self.conn.executemany(
            "INSERT INTO alerts(timestamp, rule, severity, ip, user, message, event_raw, status, notes) VALUES(?,?,?,?,?,?,?,?,?)",
            [(a["timestamp"], a["rule"], a["severity"], a.get("ip"), a.get("user"), a["message"], a["event_raw"], "open", "") for a in alerts]
        )
        self.conn.commit()
