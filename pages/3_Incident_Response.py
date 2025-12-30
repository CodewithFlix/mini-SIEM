import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

DB_PATH = "data/siem.db"
st.title("🚨 Incident Response")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)

with st.sidebar:
    st.caption("User: pentester")
    st.header("Incident Response")
    status = st.selectbox("Status", ["open", "resolved"], index=0)
    sev = st.multiselect("Severity", ["high", "medium", "info"], default=["high", "medium", "info"])
    max_alerts = st.slider("Max alerts", 20, 500, 100)
    correlate_minutes = st.slider("Correlation window (minutes)", 1, 240, 30)

alerts = pd.read_sql_query(
    f"""
    SELECT * FROM alerts
    WHERE status = ?
      AND severity IN ({','.join(['?']*len(sev))})
    ORDER BY timestamp DESC
    LIMIT ?
    """,
    conn,
    params=[status, *sev, max_alerts]
)

st.subheader("Alerts Queue")
st.dataframe(alerts, use_container_width=True)

if len(alerts) == 0:
    st.stop()

pick = st.selectbox("Select alert id", alerts["id"].tolist())
a = alerts[alerts["id"] == pick].iloc[0].to_dict()

st.subheader("Incident Detail")
c1, c2 = st.columns([2, 1])

with c1:
    st.json(a)

with c2:
    st.markdown("### Actions")
    new_status = st.selectbox("Update status", ["open", "resolved"], index=0 if a["status"] == "open" else 1)
    notes = st.text_area("Notes", value=a.get("notes", ""), height=140)
    if st.button("Save", type="primary"):
        conn.execute("UPDATE alerts SET status=?, notes=? WHERE id=?", (new_status, notes, pick))
        conn.commit()
        st.success("Saved. Refresh page to see updates.")

st.subheader("Correlated Events")
ts = datetime.fromisoformat(a["timestamp"])
t1 = (ts - timedelta(minutes=correlate_minutes)).isoformat()
t2 = (ts + timedelta(minutes=correlate_minutes)).isoformat()

ip = a.get("ip")
user = a.get("user")

sql = "SELECT * FROM events WHERE timestamp BETWEEN ? AND ?"
params = [t1, t2]

if ip:
    sql += " AND ip = ?"
    params.append(ip)
elif user:
    sql += " AND user = ?"
    params.append(user)

sql += " ORDER BY timestamp DESC LIMIT 500"

corr = pd.read_sql_query(sql, conn, params=params)
st.dataframe(corr, use_container_width=True)
