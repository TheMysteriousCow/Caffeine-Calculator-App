import streamlit as st
import base64
import os
import json


# =========================
# Profil speichern/laden
# =========================
PROFILE_FILE = "profile.json"


def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "name": "",
        "first_name": "",
        "gender": "Female",
        "weight": "",
        "height": ""
    }


def save_profile(profile):
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)


profile = load_profile()


# =========================
# Logo Funktion
# =========================
def set_logo_top_right(image_file: str):
    if not os.path.exists(image_file):
        st.warning(f"Bild konnte nicht geladen werden. Pfad: {image_file}")
        return

    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    css = f"""
    <style>

    .logo-container {{
        position: absolute;
        top: -45px;
        right: -10px;
        z-index: 100;
    }}

    .logo-img {{
        width: 140px;
        height: auto;
    }}

    </style>

    <div class="logo-container">
        <img src="data:image/png;base64,{encoded}" class="logo-img">
    </div>
    """

    st.markdown(css, unsafe_allow_html=True)


# =========================
# Logo einfügen
# =========================
image_path = os.path.join(os.getcwd(), "images", "logo.png")
set_logo_top_right(image_path)


# =========================
# Styling
# =========================
st.markdown("""
<style>

.stApp {
    background-color: white;
}

/* Textfarben */
h1, h2, h3, h4, h5, h6, p, label {
    color: #5C4033 !important;
}

/* Titel */
.main-title {
    text-align: center;
    font-size: 3.4rem;
    font-family: 'Georgia', 'Times New Roman', serif;
    font-weight: 600;
    color: #5C4033;
    margin-bottom: 0.3rem;
    letter-spacing: 1px;
}

/* Inputfelder */
input {
    color: #5C4033 !important;
}

/* Dropdown */
div[data-baseweb="select"] > div {
    color: #5C4033 !important;
}

/* Save Button */
.stButton > button {
    background-color: white;
    color: #5C4033;
    border: 2px solid #5C4033;
    border-radius: 12px;
    padding: 0.7rem 2rem;
    font-size: 1rem;
    font-weight: 600;
    width: 100%;
    transition: 0.3s;
}

/* Hover Effekt */
.stButton > button:hover {
    background-color: #f8f5f2;
    color: #5C4033;
    border: 2px solid #5C4033;
}

</style>
""", unsafe_allow_html=True)


# =========================
# Titel
# =========================
st.markdown(
    "<div class='main-title'>Your Profile</div>",
    unsafe_allow_html=True
)

st.write("")


# =========================
# Eingabefelder
# =========================
name = st.text_input(
    "Name",
    value=profile["name"]
)

first_name = st.text_input(
    "First name",
    value=profile["first_name"]
)

gender_options = ["Female", "Male", "Diverse"]

gender = st.selectbox(
    "Gender",
    gender_options,
    index=gender_options.index(profile["gender"])
)

weight = st.text_input(
    "Weight",
    value=profile["weight"]
)

height = st.text_input(
    "Height in meters",
    value=profile["height"]
)


# =========================
# Save Button
# =========================
if st.button("Save"):

    new_profile = {
        "name": name,
        "first_name": first_name,
        "gender": gender,
        "weight": weight,
        "height": height
    }

    save_profile(new_profile)