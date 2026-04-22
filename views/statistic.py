import pandas as pd
import streamlit as st

# -------------------------------------------------
# CSS (einheitliche Farbe + Titelstil)
# -------------------------------------------------
st.markdown("""
<style>

/* Hintergrund */
.stApp {
    background-color: white;
}

/* Einheitliche Schriftfarbe */
h1, h2, h3, h4, h5, h6, p, label, span {
    color: #5C4033 !important;
}

/* TITEL wie auf Hauptscreen */
.main-title {
    text-align: center;
    font-size: 3.4rem;
    font-family: 'Georgia', 'Times New Roman', serif;
    font-weight: 600;
    color: #5C4033;
    margin-bottom: 0.3rem;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)

# Titel
st.markdown("<div class='main-title'>History</div>", unsafe_allow_html=True)

# -------------------------------------------------
# HISTORY
# -------------------------------------------------

if "data_df" not in st.session_state:
    st.session_state["data_df"] = pd.DataFrame()

data_df = st.session_state["data_df"]

if not data_df.empty and "timestamp" in data_df.columns:
    data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors="coerce")
    data_df = data_df.sort_values("timestamp")
    st.session_state["data_df"] = data_df

st.subheader("Verlauf der Getränke")

if data_df.empty:
    st.info("Noch keine Daten vorhanden. Führen Sie zuerst eine Berechnung im Koffein Rechner durch.")
else:
    st.dataframe(data_df, use_container_width=True)

if st.button("🗑️ Verlauf löschen"):
    st.session_state["data_df"] = pd.DataFrame()
    data_manager = st.session_state["data_manager"]
    data_manager.save_user_data(st.session_state["data_df"], "data.csv")
    st.success("Verlauf wurde gelöscht!")