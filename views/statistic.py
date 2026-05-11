import pandas as pd
import streamlit as st
from datetime import datetime
import base64
import os
import json

DIARY_FILE = "diary.csv"
PROFILE_FILE = "profile.json"


# =========================
# PROFILE LOAD
# =========================
def load_profile():
    if os.path.exists(PROFILE_FILE):
        try:
            with open(PROFILE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass

    return {
        "name": "",
        "first_name": "",
        "gender": "Female",
        "weight": "",
        "height": ""
    }


profile = load_profile()
first_name = str(profile.get("first_name", "")).strip()

if first_name:
    diary_title = f"{first_name}'s Diary"
else:
    diary_title = "My Diary"


# =========================
# FILES
# =========================
DATA_FILE = "data.csv"


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


def empty_history_df():
    return pd.DataFrame(columns=[
        "timestamp",
        "Drink",
        "Caffeine (mg)",
        "Volume (ml)"
    ])


def empty_diary_df():
    return pd.DataFrame(columns=["timestamp", "Diary Entry"])


def load_history_data():
    if "data_manager" in st.session_state:
        try:
            data_manager = st.session_state["data_manager"]
            df = data_manager.load_user_data(DATA_FILE)

            if df is not None:
                return df
        except:
            pass

    if os.path.exists(DATA_FILE):
        try:
            return pd.read_csv(DATA_FILE)
        except:
            return empty_history_df()

    return empty_history_df()


def save_history_data(df):
    if "data_manager" in st.session_state:
        try:
            data_manager = st.session_state["data_manager"]
            data_manager.save_user_data(df, DATA_FILE)
            return
        except:
            pass

    df.to_csv(DATA_FILE, index=False)


def load_diary_data():
    if "data_manager" in st.session_state:
        try:
            data_manager = st.session_state["data_manager"]
            df = data_manager.load_user_data(DIARY_FILE)

            if df is not None and not df.empty:
                return df
        except:
            pass

    if os.path.exists(DIARY_FILE):
        try:
            return pd.read_csv(DIARY_FILE)
        except:
            return empty_diary_df()

    return empty_diary_df()


def save_diary_data(df):
    if "data_manager" in st.session_state:
        try:
            data_manager = st.session_state["data_manager"]
            data_manager.save_user_data(df, DIARY_FILE)
            return
        except:
            pass

    df.to_csv(DIARY_FILE, index=False)


# =========================
# LOGO
# =========================
image_path = os.path.join(os.getcwd(), "images", "logo.png")
set_logo_top_right(image_path)


# =========================
# CSS
# =========================
st.markdown("""
<style>
.stApp {
    background-color: white;
}

h1, h2, h3, h4, h5, h6, p, label, span {
    color: #5C4033 !important;
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

.section-title {
    font-size: 1.8rem;
    font-family: 'Georgia', serif;
    font-weight: 600;
    color: #5C4033;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

div.stButton > button {
    background-color: #CDECCF;
    color: #5C4033;
    border: none;
    border-radius: 12px;
    font-weight: 600;
}

[data-testid="stSidebar"] button {
    background-color: white !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================
st.markdown("<div class='main-title'>History</div>", unsafe_allow_html=True)


# =========================
# HISTORY DATA
# =========================
if "data_df" not in st.session_state:
    st.session_state["data_df"] = load_history_data()

if st.session_state["data_df"] is None:
    st.session_state["data_df"] = empty_history_df()

data_df = st.session_state["data_df"]

if not data_df.empty and "timestamp" in data_df.columns:
    data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors="coerce")
    data_df = data_df.dropna(subset=["timestamp"])
    data_df = data_df.sort_values("timestamp", ascending=False)
    st.session_state["data_df"] = data_df

st.markdown("<div class='section-title'>Drink History</div>", unsafe_allow_html=True)

if data_df.empty:
    st.info("No data available yet. Please choose a drink in the Caffeine Calculator first.")
else:
    display_df = data_df.copy()

    if "timestamp" in display_df.columns:
        display_df["Date"] = display_df["timestamp"].dt.strftime("%d.%m.%Y")
        display_df["Time"] = display_df["timestamp"].dt.strftime("%H:%M")

    columns_to_show = ["Date", "Time", "Drink", "Caffeine (mg)", "Volume (ml)"]
    existing_columns = [col for col in columns_to_show if col in display_df.columns]

    st.dataframe(
        display_df[existing_columns],
        use_container_width=True,
        hide_index=True
    )


# =========================
# DELETE HISTORY
# =========================
if st.button("🗑️ Clear History"):
    empty_df = empty_history_df()

    st.session_state["data_df"] = empty_df
    save_history_data(empty_df)

    st.success("History has been cleared!")
    st.rerun()


# =========================
# DIARY
# =========================
st.markdown(f"<div class='section-title'>{diary_title}</div>", unsafe_allow_html=True)


# =========================
# LOAD DIARY DATA
# =========================
if "diary_df" not in st.session_state:
    st.session_state["diary_df"] = load_diary_data()

if "diary_df" not in st.session_state or st.session_state["diary_df"] is None:
    st.session_state["diary_df"] = empty_diary_df()


# =========================
# DATE + TIME INPUT
# =========================
col_date, col_time = st.columns(2)

with col_date:
    diary_date = st.date_input(
        "Choose a date:",
        value=datetime.now().date()
    )

with col_time:
    diary_time = st.time_input(
        "Choose a time:",
        value=datetime.now().time().replace(second=0, microsecond=0)
    )

diary_timestamp = datetime.combine(diary_date, diary_time)


# =========================
# DIARY TEXT INPUT
# =========================
diary_text = st.text_area(
    "Write your diary entry here:",
    height=180,
    placeholder="How do you feel today? Did caffeine affect your energy, sleep, mood or concentration?"
)


# =========================
# SAVE DIARY ENTRY
# =========================
if st.button("💾 Save Diary Entry"):
    if diary_text.strip() == "":
        st.warning("Please write something before saving.")
    else:
        new_entry = pd.DataFrame([{
            "timestamp": diary_timestamp,
            "Diary Entry": diary_text.strip()
        }])

        st.session_state["diary_df"] = pd.concat(
            [st.session_state["diary_df"], new_entry],
            ignore_index=True
        )

        save_diary_data(st.session_state["diary_df"])

        st.success("Diary entry saved!")
        st.rerun()


# =========================
# SHOW + DELETE DIARY ENTRIES
# =========================
diary_df = st.session_state["diary_df"]

if not diary_df.empty:
    diary_df["timestamp"] = pd.to_datetime(diary_df["timestamp"], errors="coerce")
    diary_df = diary_df.dropna(subset=["timestamp"])
    diary_df = diary_df.sort_values("timestamp", ascending=False).reset_index(drop=True)
    st.session_state["diary_df"] = diary_df

    st.markdown("<div class='section-title'>Saved Diary Entries</div>", unsafe_allow_html=True)

    for index, row in diary_df.iterrows():
        date_time = row["timestamp"].strftime("%d.%m.%Y %H:%M")
        entry = row["Diary Entry"]

        st.markdown(f"""
        <div style="
            border: 2px solid #CDECCF;
            border-radius: 14px;
            padding: 16px;
            margin-bottom: 10px;
            background-color: #FAFFFA;
        ">
            <strong>{date_time}</strong><br><br>
            {entry}
        </div>
        """, unsafe_allow_html=True)

        if st.button("🗑️ Delete Entry", key=f"delete_diary_{index}"):
            st.session_state["diary_df"] = diary_df.drop(index).reset_index(drop=True)
            save_diary_data(st.session_state["diary_df"])

            st.success("Diary entry deleted!")
            st.rerun()

else:
    st.info("No diary entries yet.")