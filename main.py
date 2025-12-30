import argparse
from siem.collectors.file_collector import read_lines
from siem.parsers.auth_parser import parse_auth_line
from siem.detectors.rules import RuleEngine
from siem.storage.db import SIEMDB

def run_pipeline(log_path: str):
    db = SIEMDB()
    engine = RuleEngine()

    for line in read_lines(log_path):
        event = parse_auth_line(line)
        if not event:
            continue

        db.insert_event(event)
        alerts = engine.run(event)
        if alerts:
            db.insert_alerts(alerts)

def main():
    parser = argparse.ArgumentParser(description="Mini SIEM (Mac compatible)")
    parser.add_argument("--log", required=True, help="Path to log file (e.g., samples/auth.log)")
    args = parser.parse_args()

    run_pipeline(args.log)
    print("✅ Ingest complete. Run: streamlit run app.py")

if __name__ == "__main__":
    main()
