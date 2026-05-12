import streamlit as st
from utils.profile_utils import load_profile, save_profile

username = st.session_state.get("username", "default_user")
profile = load_profile(username)

st.title("Your Profile")

name = st.text_input(
    "Name",
    value=profile.get("name", "")
)

first_name = st.text_input(
    "First name",
    value=profile.get("first_name", "")
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Other"],
    index=["Female", "Male", "Other"].index(
        profile.get("gender", "Female")
    )
)

weight_value = profile.get("weight", "")
height_value = profile.get("height", "")

weight = st.text_input(
    "Weight in kilograms",
    value="" if weight_value in ["", None, 60] else str(weight_value)
)

height = st.text_input(
    "Height in meters",
    value="" if height_value in ["", None, 1.70] else str(height_value)
)

if st.button("Save"):

    try:
        weight = float(str(weight).replace(",", "."))
    except:
        weight = ""

    try:
        height = float(str(height).replace(",", "."))
    except:
        height = ""

    save_profile(username, {
        "name": name,
        "first_name": first_name,
        "gender": gender,
        "weight": weight,
        "height": height
    })

    st.success("Profile saved")