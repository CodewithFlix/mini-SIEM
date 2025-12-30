import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "data/siem.db"

st.title("📊 Dashboard")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
events = pd.read_sql_query("SELECT * FROM events ORDER BY timestamp DESC", conn)
alerts = pd.read_sql_query("SELECT * FROM alerts ORDER BY timestamp DESC", conn)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Events", len(events))
c2.metric("Total Alerts", len(alerts))
c3.metric("Open Alerts", int((alerts["status"] == "open").sum()) if "status" in alerts else 0)
c4.metric("Unique IPs", int(events["ip"].nunique()) if "ip" in events else 0)

st.subheader("Recent Alerts")
st.dataframe(alerts.head(20), use_container_width=True)

st.subheader("Recent Events")
st.dataframe(events.head(30), use_container_width=True)

