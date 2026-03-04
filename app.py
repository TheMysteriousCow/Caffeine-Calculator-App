import streamlit as st

home = st.Page("views/home.py", title="Home", icon="🏠")
calculator = st.Page("views/caffeine_calculator.py", title="Koffein Rechner", icon="☕")

pg = st.navigation([home, calculator])

pg.run()