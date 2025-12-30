import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "data/siem.db"
st.title("🗂️ Audit Log Management")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)

with st.sidebar:
    st.caption("User: pentester")
    st.header("Audit Logs")
    q = st.text_input("Search logs…", placeholder="ssh_failed_login / 185.12.44.10 / felix / sudo")
    severity = st.multiselect("Severity", ["info", "medium", "high"], default=["info", "medium", "high"])
    event_type = st.text_input("Event Type (optional)", placeholder="ssh_failed_login")
    user = st.text_input("User (optional)", placeholder="felix")
    ip = st.text_input("IP (optional)", placeholder="185.12.44.10")
    limit = st.slider("Max rows", 50, 2000, 200)

st.subheader("System Search")

run = st.button("Run Query", type="primary")

def build_query():
    base = "SELECT * FROM events WHERE 1=1"
    params = []

    if severity:
        base += f" AND severity IN ({','.join(['?'] * len(severity))})"
        params += severity

    if event_type.strip():
        base += " AND event_type = ?"
        params.append(event_type.strip())

    if user.strip():
        base += " AND user = ?"
        params.append(user.strip())

    if ip.strip():
        base += " AND ip = ?"
        params.append(ip.strip())

    if q.strip():
        base += " AND (raw LIKE ? OR event_type LIKE ? OR user LIKE ? OR ip LIKE ?)"
        like = f"%{q.strip()}%"
        params += [like, like, like, like]

    base += " ORDER BY timestamp DESC LIMIT ?"
    params.append(limit)

    return base, params

if run:
    sql, params = build_query()
    df = pd.read_sql_query(sql, conn, params=params)
    st.caption(f"Results: {len(df)} rows")
    st.dataframe(df, use_container_width=True)

    st.subheader("Event Detail")
    if len(df) > 0:
        pick = st.selectbox("Select event id", df["id"].tolist())
        row = df[df["id"] == pick].iloc[0].to_dict()
        st.json(row)
