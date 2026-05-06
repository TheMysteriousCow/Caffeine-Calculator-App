import streamlit as st
import pandas as pd
import os
import time
import streamlit.components.v1 as components
import base64
import re
import unicodedata
from difflib import SequenceMatcher

st.set_page_config(page_title="Caffeine Calculator", layout="wide")


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
        top: -40px;
        right: -20px;
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
# Logo anzeigen
# =========================
image_path = os.path.join(os.getcwd(), "images", "logo.png")
set_logo_top_right(image_path)


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
    color: #5C4033;
}

input {
    color: #5C4033 !important;
}

label {
    color: #5C4033 !important;
}

.drink-card {
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# TITLE
# -----------------------------
st.markdown("<div class='main-title'>Caffeine Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Choose your drink and calculate your caffeine intake.</div>", unsafe_allow_html=True)


# -----------------------------
# DRINK DATA
# -----------------------------
drinks = {
    "Red Bull": {"image": "Redbull.png", "caffeine_mg": 114, "volume_ml": 355},
    "Monster": {"image": "Monster.png", "caffeine_mg": 160, "volume_ml": 500},
    "El Tony Mate Zero": {"image": "ElTonyMateZero.png", "caffeine_mg": 85.8, "volume_ml": 330},
    "El Tony Mate": {"image": "ElTonyMate.png", "caffeine_mg": 76, "volume_ml": 330},
    "Mate Bio Puro": {"image": "MateBioPuro.png", "caffeine_mg": 80, "volume_ml": 500},
    "Nocco": {"image": "Nocco.png", "caffeine_mg": 180, "volume_ml": 330},
    "Matcha": {"image": "Matcha.png", "caffeine_mg": 79, "volume_ml": 250},
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
# SEARCH FUNCTION
# -----------------------------
def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9]", "", text)
    return text


def search_matches(search_text, drink_name):
    if search_text.strip() == "":
        return True

    search_clean = normalize_text(search_text)
    drink_clean = normalize_text(drink_name)

    if search_clean in drink_clean:
        return True

    similarity = SequenceMatcher(None, search_clean, drink_clean).ratio()

    return similarity >= 0.45


# -----------------------------
# CALCULATION SETTINGS
# -----------------------------
PEAK_MINUTES = 45
CRASH_HOURS = 4
RECOVERY_HOURS = 8

BASE_EFFECT_HOURS = 3.0
REFERENCE_CAFFEINE_MG = 80
MAX_EFFECT_HOURS = 6.0


def caffeine_effect_duration_hours(caffeine_mg):
    if caffeine_mg <= 0:
        return 0

    effect_hours = BASE_EFFECT_HOURS + (caffeine_mg / REFERENCE_CAFFEINE_MG) * 1.2
    return min(effect_hours, MAX_EFFECT_HOURS)


def format_hours(hours):
    total_minutes = int(round(hours * 60))
    h = total_minutes // 60
    m = total_minutes % 60
    return f"{h} h {m} min"


# -----------------------------
# SESSION STATE
# -----------------------------
if "selected_drink" not in st.session_state:
    st.session_state.selected_drink = None

if "selected_caffeine_mg" not in st.session_state:
    st.session_state.selected_caffeine_mg = 0

if "selected_volume_ml" not in st.session_state:
    st.session_state.selected_volume_ml = 0

if "drink_start_time" not in st.session_state:
    st.session_state.drink_start_time = None

if "scroll_to_timeline" not in st.session_state:
    st.session_state.scroll_to_timeline = False

if "data_df" not in st.session_state:
    st.session_state["data_df"] = pd.DataFrame(columns=[
        "timestamp",
        "Drink",
        "Caffeine (mg)"
    ])


# -----------------------------
# CHOOSE DRINK
# -----------------------------
st.markdown("<div class='section-title'>Choose your Drink</div>", unsafe_allow_html=True)

left, center, right = st.columns([1, 4, 1])

with center:
    search_text = st.text_input(
        "Search drink",
        placeholder="Example: redbull, latte machiato, coffe..."
    )

    filtered_drinks = {
        name: info
        for name, info in drinks.items()
        if search_matches(search_text, name)
    }

    if len(filtered_drinks) == 0:
        st.info("No drink found. Try another spelling.")

    drink_items = list(filtered_drinks.items())

    for i in range(0, len(drink_items), 3):
        cols = st.columns(3)

        for col, item in zip(cols, drink_items[i:i + 3]):
            drink_name, info = item

            with col:
                st.markdown("<div class='drink-card'>", unsafe_allow_html=True)

                image_path = os.path.join("images", info["image"])

                if os.path.exists(image_path):
                    st.image(image_path, use_container_width=True)
                else:
                    st.write("🥤")

                if st.button(drink_name, key=f"drink_{drink_name}", use_container_width=True):
                    st.session_state.selected_drink = drink_name
                    st.session_state.selected_caffeine_mg = info["caffeine_mg"]
                    st.session_state.selected_volume_ml = info["volume_ml"]
                    st.session_state.drink_start_time = int(time.time())
                    st.session_state.scroll_to_timeline = True

                    new_entry = pd.DataFrame([{
                        "timestamp": pd.Timestamp.now(),
                        "Drink": drink_name,
                        "Caffeine (mg)": info["caffeine_mg"]
                    }])

                    st.session_state["data_df"] = pd.concat(
                        [st.session_state["data_df"], new_entry],
                        ignore_index=True
                    )

                    if "data_manager" in st.session_state:
                        data_manager = st.session_state["data_manager"]
                        data_manager.save_user_data(st.session_state["data_df"], "data.csv")

                    st.rerun()

                st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# RESULT + COUNTDOWN
# -----------------------------
if st.session_state.selected_drink:

    st.markdown("<div id='caffeine-timeline'></div>", unsafe_allow_html=True)

    if st.session_state.scroll_to_timeline:
        components.html("""
        <script>
            const timeline = window.parent.document.querySelector('#caffeine-timeline');
            if (timeline) {
                timeline.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        </script>
        """, height=0)

        st.session_state.scroll_to_timeline = False

    selected_drink = st.session_state.selected_drink
    caffeine_mg = st.session_state.selected_caffeine_mg
    volume_ml = st.session_state.selected_volume_ml
    start_time = st.session_state.drink_start_time

    effect_hours = caffeine_effect_duration_hours(caffeine_mg)
    effect_seconds = int(effect_hours * 3600)

    st.success(f"You selected: **{selected_drink}**")

    st.markdown("### Caffeine Timeline")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Peak", f"{PEAK_MINUTES} min", "about 0 h 45 min")

    with col2:
        st.metric("Crash", f"{CRASH_HOURS} h", f"{CRASH_HOURS * 60} min")

    with col3:
        st.metric("Recovery", f"{RECOVERY_HOURS} h", f"{RECOVERY_HOURS * 60} min")

    with col4:
        st.metric("Effect duration", format_hours(effect_hours))

    end_time = start_time + effect_seconds

    html = f"""
    <div style="
        display:flex;
        align-items:center;
        justify-content:center;
        gap:50px;
        margin-top:35px;
        margin-bottom:25px;
        font-family:Arial, sans-serif;
    ">
        <div style="
            background:#f7f4f1;
            border-radius:24px;
            padding:28px 36px;
            min-width:300px;
            text-align:center;
            box-shadow:0 8px 20px rgba(0,0,0,0.08);
        ">
            <div style="
                color:#5C4033;
                font-size:1.1rem;
                margin-bottom:10px;
            ">
                Countdown while caffeine is still working
            </div>

            <div id="countdown" style="
                color:#5C4033;
                font-size:2.4rem;
                font-weight:700;
                letter-spacing:1px;
            ">
                Loading...
            </div>

            <div id="status" style="
                color:#6b7280;
                font-size:0.95rem;
                margin-top:10px;
            ">
                Caffeine effect is decreasing over time.
            </div>
        </div>

        <div style="
            width:120px;
            height:220px;
            border:5px solid #5C4033;
            border-radius:0 0 35px 35px;
            position:relative;
            overflow:hidden;
            background:rgba(255,255,255,0.85);
            box-shadow:0 8px 20px rgba(0,0,0,0.12);
        ">
            <div id="liquid" style="
                position:absolute;
                bottom:0;
                left:0;
                width:100%;
                height:100%;
                background:linear-gradient(180deg, #6b3f22 0%, #3b1f12 100%);
                transition:height 1s linear;
            "></div>

            <div style="
                position:absolute;
                top:20px;
                left:25px;
                width:22px;
                height:150px;
                background:rgba(255,255,255,0.22);
                border-radius:20px;
            "></div>
        </div>
    </div>

    <script>
        const startTime = {start_time * 1000};
        const endTime = {end_time * 1000};
        const totalDuration = endTime - startTime;

        function updateCountdown() {{
            const now = new Date().getTime();
            let remaining = endTime - now;

            if (remaining <= 0) {{
                remaining = 0;
                document.getElementById("countdown").innerHTML = "0 h 0 min 0 s";
                document.getElementById("status").innerHTML = "The main caffeine effect is now likely over.";
                document.getElementById("liquid").style.height = "0%";
                return;
            }}

            const hours = Math.floor(remaining / (1000 * 60 * 60));
            const minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((remaining % (1000 * 60)) / 1000);

            document.getElementById("countdown").innerHTML =
                hours + " h " + minutes + " min " + seconds + " s";

            const elapsed = now - startTime;
            const progress = Math.min(Math.max(elapsed / totalDuration, 0), 1);
            const liquidHeight = 100 - (progress * 100);

            document.getElementById("liquid").style.height = liquidHeight + "%";
        }}

        updateCountdown();
        setInterval(updateCountdown, 1000);
    </script>
    """

    components.html(html, height=330)

    st.info(
        f"{selected_drink} contains **{caffeine_mg} mg caffeine** in **{volume_ml} ml**. "
        f"The noticeable caffeine effect is estimated to last about **{format_hours(effect_hours)}**."
    )