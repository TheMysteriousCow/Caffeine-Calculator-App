import streamlit as st

DEFAULT_PROFILE = {
    "name": "",
    "first_name": "",
    "gender": "Female",
    "weight": 60,
    "height": 1.70
}


def load_profile(username):
    data_manager = st.session_state.get("data_manager")

    if data_manager is None:
        st.error("Profile error: DataManager not found in session_state.")
        return DEFAULT_PROFILE.copy()

    return data_manager.load_user_data(
        "profile.json",
        initial_value=DEFAULT_PROFILE.copy()
    )


def save_profile(username, profile_data):
    data_manager = st.session_state.get("data_manager")

    if data_manager is None:
        st.error("Profile error: DataManager not found in session_state.")
        return

    data_manager.save_user_data(
        profile_data,
        "profile.json"
    )