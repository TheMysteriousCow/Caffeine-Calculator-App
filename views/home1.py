import streamlit as st

# Titel
st.markdown(
    "<h1 style='color:#5C4033;'>Caffeine</h1>",
    unsafe_allow_html=True
)

st.write("")

# Optional: Buttons etwas größer machen
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 70px;
        font-size: 24px;
        border-radius: 10px;
        border: 2px solid #5C4033;
        color: black;
        background-color: white;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Kästchen / Buttons
if st.button("Calculator"):
    st.switch_page("views/caffeine_calculator.py")

if st.button("Statistics"):
    st.switch_page("views/statistics.py")

if st.button("Recommendations"):
    st.switch_page("views/recommendations.py")

if st.button("Alternatives"):
    st.switch_page("views/alternatives.py")