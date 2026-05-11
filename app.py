import streamlit as st
import pandas as pd
from pandas.errors import EmptyDataError

from utils.data_manager import DataManager
from utils.login_manager import LoginManager

st.set_page_config(page_title="Caffeine Calculator", layout="wide")

data_manager = DataManager(
    fs_protocol="webdav",
    fs_root_folder="diagnosticdetective"
)

st.session_state["data_manager"] = data_manager

login_manager = LoginManager(data_manager)
login_manager.login_register()

if "data_df" not in st.session_state:
    try:
        df = data_manager.load_user_data(
            "data.csv",
            initial_value=pd.DataFrame()
        )
    except EmptyDataError:
        df = pd.DataFrame()

    if not df.empty and "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    st.session_state["data_df"] = df

st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background-color: #f3f4f6;
}

section[data-testid="stSidebar"] a {
    border-radius: 10px;
    padding: 8px 12px !important;
    margin-bottom: 6px;
    display: block;
    color: black !important;
    text-decoration: none !important;
}

section[data-testid="stSidebar"] a[href*="home"] {
    background-color: #FFE5B4 !important;
}

section[data-testid="stSidebar"] a[href*="your_profile"] {
    background-color: #FFF4B8 !important;
}

section[data-testid="stSidebar"] a[href*="additional_data"] {
    background-color: #FFD8B1 !important;
}

section[data-testid="stSidebar"] a[href*="caffeine_calculator"] {
    background-color: #F7C6C7 !important;
}

section[data-testid="stSidebar"] a[href*="statistic"] {
    background-color: #E7A8C9 !important;
}

section[data-testid="stSidebar"] a[href*="recommendations"] {
    background-color: #F8D6E6 !important;
}

section[data-testid="stSidebar"] a[href*="alternatives"] {
    background-color: #CFE8FF !important;
}

section[data-testid="stSidebar"] a[href*="professional_help"] {
    background-color: #6FA3CC !important;
}

section[data-testid="stSidebar"] a:hover {
    opacity: 0.85;
}

/* NUR Logout Button in der Sidebar */
section[data-testid="stSidebar"] div[data-testid="stButton"] button {
    background-color: #CDECCF !important;
    color: black !important;

    border-radius: 14px !important;
    border: none !important;

    font-size: 15px !important;
    font-family: Arial, sans-serif !important;

    box-shadow: none !important;
}

/* Hover nur für Logout */
section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
    background-color: #BFE3C1 !important;
    color: black !important;
    border: none !important;
}

/* Fokus nur für Logout */
section[data-testid="stSidebar"] div[data-testid="stButton"] button:focus {
    background-color: #CDECCF !important;
    color: black !important;
    border: none !important;
    box-shadow: none !important;
}

/* Klick nur für Logout */
section[data-testid="stSidebar"] div[data-testid="stButton"] button:active {
    background-color: #BFE3C1 !important;
    color: black !important;
    border: none !important;
}

</style>
""", unsafe_allow_html=True)

home = st.Page("views/home1.py", title="Home", url_path="home", default=True)
your_profile = st.Page("views/your_profile.py", title="Your Profile", url_path="your_profile")
additional_data = st.Page("views/additional_data.py", title="Additional Data", url_path="additional_data")
calculator = st.Page("views/caffeine_calculator.py", title="Caffeine Calculator", url_path="caffeine_calculator")
statistics = st.Page("views/statistic.py", title="History", url_path="statistic")
recommendations = st.Page("views/recommendations.py", title="Recommendations", url_path="recommendations")
alternatives = st.Page("views/alternatives.py", title="Alternatives", url_path="alternatives")
professional_help = st.Page("views/professional_help.py", title="Professional Help", url_path="professional_help")

pg = st.navigation([
    home,
    your_profile,
    additional_data,
    calculator,
    statistics,
    recommendations,
    alternatives,
    professional_help
])

pg.run()