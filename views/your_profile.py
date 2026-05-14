import os
import streamlit as st

from functions.logo import set_logo

from functions.your_profile_functions import (
    apply_profile_style,
    check_user_logged_in,
    get_data_manager,
    load_profile,
    get_valid_gender,
    format_weight_value,
    format_height_value,
    save_profile
)


image_path = os.path.join(os.getcwd(), "images", "logo.png")

set_logo(
    image_path,
    top=0,
    right=-10,
    width=140
)

apply_profile_style()

check_user_logged_in()

data_manager = get_data_manager()

profile = load_profile(data_manager)

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

gender_options, saved_gender = get_valid_gender(profile)

gender = st.selectbox(
    "Gender",
    gender_options,
    index=gender_options.index(saved_gender)
)

weight = st.text_input(
    "Weight in kilograms",
    value=format_weight_value(
        profile.get("weight", "")
    )
)

height = st.text_input(
    "Height in meters",
    value=format_height_value(
        profile.get("height", "")
    )
)

if st.button("Save"):

    save_profile(
        data_manager,
        name,
        first_name,
        gender,
        weight,
        height
    )

    st.success("Profile saved")