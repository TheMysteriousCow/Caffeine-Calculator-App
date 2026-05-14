import pandas as pd
import streamlit as st
from datetime import datetime
import os
from utils.profile_utils import load_profile
from functions.logo import set_logo
from utils.data_manager import DataManager

data_manager = DataManager(fs_protocol="webdav", fs_root_folder="caffeine_calculator_app")


username = st.session_state.get("username", "default_user")

if st.session_state.get("history_username") != username:
    st.session_state.pop("data_df", None)
    st.session_state.pop("diary_df", None)
    st.session_state["history_username"] = username

DATA_FILE = f"data_{username}.csv"
DIARY_FILE = f"diary_{username}.csv"

profile = load_profile(username)
first_name = str(profile.get("first_name", "")).strip()
diary_title = f"{first_name}'s Diary" if first_name else "My Diary"

def empty_history_df():
    return pd.DataFrame(columns=[
        "timestamp",
        "Drink",
        "Caffeine (mg)",
        "Volume (ml)"
    ])

def empty_diary_df():
    return pd.DataFrame(columns=[
        "timestamp",
        "Diary Entry"
    ])



    return empty_history_df()



image_path = os.path.join(os.getcwd(), "images", "logo.png")

# Logo anzeigen
set_logo(
    image_path,
    top=-40,
    right=-20,
    width=140
)

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
    color: #5C4033 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>History</div>", unsafe_allow_html=True)

if "data_df" not in st.session_state:
    st.session_state["data_df"] = data_manager.load_user_data(
        DATA_FILE, 
        initial_value=empty_history_df()
    )

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

if st.button("🗑️ Clear History"):
    empty_df = empty_history_df()
    st.session_state["data_df"] = empty_df
    data_manager.save_user_data(empty_df, DATA_FILE)
    st.success("History has been cleared!")
    st.rerun()

st.markdown(f"<div class='section-title'>{diary_title}</div>", unsafe_allow_html=True)

if "diary_df" not in st.session_state:
    st.session_state["diary_df"] = data_manager.load_user_data(
        DIARY_FILE,
        initial_value=empty_diary_df()
    )

if st.session_state["diary_df"] is None:
    st.session_state["diary_df"] = empty_diary_df()

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

diary_text = st.text_area(
    "Write your diary entry here:",
    height=180,
    placeholder="How do you feel today? Did caffeine affect your energy, sleep, mood or concentration?"
)

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

        data_manager.save_user_data(st.session_state["diary_df"], DIARY_FILE)


        st.success("Diary entry saved!")
        st.rerun()

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