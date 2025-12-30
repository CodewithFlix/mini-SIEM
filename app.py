import streamlit as st

st.set_page_config(page_title="Mini SIEM", page_icon="🛡️", layout="wide")

st.markdown(
    """
    <style>
      .block-container {padding-top: 2rem; padding-bottom: 2rem;}
      [data-testid="stSidebar"] {min-width: 290px; max-width: 290px;}
      .soc-title {font-size: 2.2rem; font-weight: 900; letter-spacing: -0.5px;}
      .soc-sub {opacity: 0.75; margin-top: -8px;}
      .card {border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 14px;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="soc-title">🛡️ Mini SIEM</div>', unsafe_allow_html=True)
st.markdown('<div class="soc-sub">Audit Log Management • Detection • Incident Response</div>', unsafe_allow_html=True)
st.divider()

st.info("Gunakan menu di sidebar untuk navigasi: Dashboard, Audit Logs, Incident Response.")
