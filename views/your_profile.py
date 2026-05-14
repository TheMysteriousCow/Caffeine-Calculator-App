import streamlit as st
from functions.logo import set_logo
import os

image_path = os.path.join(os.getcwd(), "images", "logo.png")

set_logo(
    image_path,
    top=0,
    right=-10,
    width=140
)

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Georgia', 'Times New Roman', serif;
    color: #5C4033;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: #5C4033 !important;
}

.main-title {
    text-align: center;
    font-size: 3.4rem;
    font-family: 'Georgia', 'Times New Roman', serif;
    font-weight: 600;
    color: #5C4033;
    margin-bottom: 2rem;
    letter-spacing: 1px;
}

.stTextInput label {
    color: #5C4033 !important;
    font-family: 'Georgia', 'Times New Roman', serif;
}

.stSelectbox label {
    color: #5C4033 !important;
    font-family: 'Georgia', 'Times New Roman', serif;
}

div.stButton > button {
    background-color: #CDECCF;
    color: #5C4033;
    border-radius: 14px;
    height: 45px;
    font-size: 15px;
    border: none;
    font-family: 'Georgia', 'Times New Roman', serif;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #BFE3C1;
    color: #5C4033;
}
</style>
""", unsafe_allow_html=True)

username = st.session_state.get("username")

if username is None:
    st.error("No user logged in.")
    st.stop()

data_manager = st.session_state["data_manager"]

DEFAULT_PROFILE = {
    "name": "",
    "first_name": "",
    "gender": "Female",
    "weight": 60,
    "height": 1.70
}

profile = data_manager.load_user_data(
    "profile.json",
    initial_value=DEFAULT_PROFILE.copy()
)

st.markdown(
    "<div class='main-title'>Your Profile</div>",
    unsafe_allow_html=True
)

name = st.text_input(
    "Name",
    value=profile.get("name", "")
)

first_name = st.text_input(
    "First name",
    value=profile.get("first_name", "")
)

gender_options = ["Female", "Male", "Other"]
saved_gender = profile.get("gender", "Female")

if saved_gender not in gender_options:
    saved_gender = "Female"

gender = st.selectbox(
    "Gender",
    gender_options,
    index=gender_options.index(saved_gender)
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
        weight_saved = float(str(weight).replace(",", "."))
    except:
        weight_saved = ""

    try:
        height_saved = float(str(height).replace(",", "."))
    except:
        height_saved = ""

    profile_data = {
        "name": name,
        "first_name": first_name,
        "gender": gender,
        "weight": weight_saved,
        "height": height_saved
    }

    data_manager.save_user_data(
        profile_data,
        "profile.json"
    )

    st.success("Profile saved")