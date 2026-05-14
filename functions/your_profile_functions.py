import streamlit as st


DEFAULT_PROFILE = {
    "name": "",
    "first_name": "",
    "gender": "Female",
    "weight": 60,
    "height": 1.70
}


def apply_profile_style():

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

    .stTextInput label,
    .stSelectbox label,
    .stTextArea label {
        color: #5C4033 !important;
        font-family: 'Georgia', 'Times New Roman', serif;
    }

    /* Textfelder */
    .stTextInput input {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
        border: none !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    .stTextInput input:focus {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* Textarea */
    .stTextArea textarea {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
        border: none !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    .stTextArea textarea:focus {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #8B8B8B !important;
    }

    /* Selectbox */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #EDEFF2 !important;
        border: none !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    .stSelectbox div[data-baseweb="select"] * {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
    }

    /* Dropdown Menü */
    div[role="listbox"] {
        background-color: #EDEFF2 !important;
        border: none !important;
    }

    div[role="option"] {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
    }

    div[role="option"]:hover {
        background-color: #DCDCDC !important;
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


def check_user_logged_in():

    username = st.session_state.get("username")

    if username is None:
        st.error("No user logged in.")
        st.stop()


def get_data_manager():

    return st.session_state["data_manager"]


def load_profile(data_manager):

    return data_manager.load_user_data(
        "profile.json",
        initial_value=DEFAULT_PROFILE.copy()
    )


def get_valid_gender(profile):

    gender_options = ["Female", "Male", "Other"]

    saved_gender = profile.get("gender", "Female")

    if saved_gender not in gender_options:
        saved_gender = "Female"

    return gender_options, saved_gender


def format_weight_value(weight_value):

    if weight_value in ["", None, 60]:
        return ""

    return str(weight_value)


def format_height_value(height_value):

    if height_value in ["", None, 1.70]:
        return ""

    return str(height_value)


def convert_to_float(value):

    try:
        return float(str(value).replace(",", "."))

    except:
        return ""


def save_profile(
    data_manager,
    name,
    first_name,
    gender,
    weight,
    height
):

    weight_saved = convert_to_float(weight)
    height_saved = convert_to_float(height)

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