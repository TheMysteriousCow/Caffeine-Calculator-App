import streamlit as st
import os

st.set_page_config(page_title="Caffeine Calculator", layout="wide")

# -----------------------------
# STYLE
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: white;
}

.main-title {
    text-align: center;
    font-size: 3.4rem;
    font-family: 'Georgia', 'Times New Roman', serif;
    font-weight: 600;
    color: #5C4033;
    margin-bottom: 0.3rem;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    font-size: 1.1rem;
    font-family: Arial, sans-serif;
    color: #6b7280;
    margin-bottom: 2rem;
}

.section-title {
    text-align: center;
    font-size: 1.8rem;
    font-family: 'Georgia', serif;
    font-weight: 600;
    color: #5C4033;
    margin-bottom: 2rem;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    height: 55px;
    background-color: #CDECCF;
    color: #5C4033;
    border: none;
    border-radius: 16px;
    font-size: 1.1rem;
    font-family: Arial, sans-serif;
    font-weight: 600;
    white-space: nowrap;
}

div.stButton > button:hover {
    background-color: #BEE6C2;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown("<div class='main-title'>Caffeine Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Choose your drink and calculate your caffeine intake.</div>", unsafe_allow_html=True)

# -----------------------------
# DRINK DATA (Monster direkt nach Red Bull)
# -----------------------------
drinks = {
    "Red Bull": {"image": "Redbull.png", "caffeine_mg": 114, "volume_ml": 355},
    "Monster": {"image": "Monster.png", "caffeine_mg": 160, "volume_ml": 500},  # 👈 hier verschoben
    "El Tony Mate Zero": {"image": "ElTonyMateZero.png", "caffeine_mg": 85.8, "volume_ml": 330},
    "El Tony Mate": {"image": "ElTonyMate.png", "caffeine_mg": 76, "volume_ml": 330},
    "Mate Bio Puro": {"image": "MateBioPuro.png", "caffeine_mg": 80, "volume_ml": 500},
    "Nocco": {"image": "Nocco.png", "caffeine_mg": 180, "volume_ml": 330},
    "Matcha": {"image": "Matcha.png", "caffeine_mg": 79, "volume_ml": None},
    "Espresso": {"image": "Espresso.png", "caffeine_mg": 60, "volume_ml": 30},
    "Doppio": {"image": "Doppio.png", "caffeine_mg": 120, "volume_ml": 60},
    "Cappuccino": {"image": "Cappuccino.png", "caffeine_mg": 60, "volume_ml": 180},
    "Latte Macchiato": {"image": "LatteMacchiato.png", "caffeine_mg": 60, "volume_ml": 250},
    "Flat White": {"image": "FlatWhite.png", "caffeine_mg": 120, "volume_ml": 160},
    "Café Crème": {"image": "CaféCrème.png", "caffeine_mg": 90, "volume_ml": 180},
    "Filterkaffee": {"image": "Filterkaffee.png", "caffeine_mg": 100, "volume_ml": 200},
    "Cold Brew": {"image": "ColdBrew.png", "caffeine_mg": 140, "volume_ml": 250}
}

# -----------------------------
# SESSION STATE
# -----------------------------
if "selected_drink" not in st.session_state:
    st.session_state.selected_drink = None

if "selected_caffeine_mg" not in st.session_state:
    st.session_state.selected_caffeine_mg = 0

if "selected_volume_ml" not in st.session_state:
    st.session_state.selected_volume_ml = 0

# -----------------------------
# CHOOSE DRINK
# -----------------------------
st.markdown("<div class='section-title'>Choose your Drink</div>", unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1])

with center:
    for drink_name, info in drinks.items():
        image_path = os.path.join("images", info["image"])

        col_img, col_btn = st.columns([2, 5])

        with col_img:
            if os.path.exists(image_path):
                st.image(image_path, use_container_width=True)
            else:
                st.write("🥤")

        with col_btn:
            if st.button(drink_name, key=f"drink_{drink_name}", use_container_width=True):
                st.session_state.selected_drink = drink_name
                st.session_state.selected_caffeine_mg = info["caffeine_mg"]
                st.session_state.selected_volume_ml = info["volume_ml"]

# -----------------------------
# RESULT
# -----------------------------
if st.session_state.selected_drink:
    st.success(f"You selected: **{st.session_state.selected_drink}**")