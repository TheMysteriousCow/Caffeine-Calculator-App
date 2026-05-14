import os
import streamlit as st

from utils.profile_utils import load_profile
from functions.logo import set_logo
from utils.data_manager import DataManager
from functions.statistic_style import apply_statistic_style
from functions.statistic_history import render_drink_history
from functions.statistic_diary import render_diary


data_manager = DataManager(
    fs_protocol="webdav",
    fs_root_folder="caffeine_calculator_app"
)

username = st.session_state.get("username")

if username is None:
    st.error("No user logged in.")
    st.stop()

if st.session_state.get("history_username") != username:
    st.session_state.pop("data_df", None)
    st.session_state.pop("diary_df", None)
    st.session_state["history_username"] = username

profile = load_profile(username)
first_name = str(profile.get("first_name", "")).strip()
diary_title = f"{first_name}'s Diary" if first_name else "My Diary"

image_path = os.path.join(os.getcwd(), "images", "logo.png")

set_logo(
    image_path,
    top=-40,
    right=-20,
    width=140
)

apply_statistic_style()

st.markdown("<div class='main-title'>History</div>", unsafe_allow_html=True)

render_drink_history(data_manager)
render_diary(data_manager, diary_title)