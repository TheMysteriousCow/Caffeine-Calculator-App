import os
import json
import time
import base64
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from functions.logo import set_logo

st.set_page_config(page_title="Recommendations", layout="wide")

username = st.session_state.get("username", "default_user")
DATA_FILE = f"data_{username}.csv"
CURRENT_FILE = f"current_caffeine_{username}.json"

PEAK_HOURS = 0.75
CRASH_HOURS = 4
RECOVERY_HOURS = 8
TOTAL_HOURS = 10
HALF_LIFE = 5.0


def empty_current_data():
    return {
        "entries": [],
        "countdown_end_time": None,
        "countdown_total_seconds": 0,
        "last_drink": None
    }


def load_current_data():
    if os.path.exists(CURRENT_FILE):
        try:
            with open(CURRENT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                return empty_current_data()

            data.setdefault("entries", [])
            data.setdefault("countdown_end_time", None)
            data.setdefault("countdown_total_seconds", 0)
            data.setdefault("last_drink", None)

            return data
        except:
            return empty_current_data()

    return empty_current_data()


def load_history_data():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.dropna(subset=["timestamp"])
            return df
        except:
            pass

    return pd.DataFrame(columns=[
        "timestamp",
        "Drink",
        "Caffeine (mg)",
        "Volume (ml)"
    ])


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
    color: #5C4033 !important;
}

html, body, p, div, span, label,
h1, h2, h3, h4, h5, h6,
.stMarkdown, .stText, .stCaption,
[data-testid="stMarkdownContainer"],
[data-testid="stText"],
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stWidgetLabel"] {
    color: #5C4033 !important;
}

.main-title {
    text-align: center;
    font-size: 3.4rem;
    font-family: 'Georgia', 'Times New Roman', serif;
    font-weight: 600;
    color: #5C4033 !important;
    margin-bottom: 0.3rem;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    font-size: 1.1rem;
    font-family: Arial, sans-serif;
    color: #5C4033 !important;
    margin-bottom: 2rem;
}

h2, h3 {
    font-family: 'Georgia', serif;
    color: #5C4033 !important;
}

div.stButton > button {
    width: 100%;
    height: 50px;
    background-color: #CDECCF;
    color: #5C4033 !important;
    border: none;
    border-radius: 16px;
    font-size: 1rem;
    font-family: Arial, sans-serif;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #BEE6C2;
    color: #5C4033 !important;
}

.streamlit-expanderHeader {
    font-family: 'Georgia', serif;
    color: #5C4033 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Recommendations</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Understand your caffeine state and get direct help.</div>", unsafe_allow_html=True)

if "recommendation_detail" not in st.session_state:
    st.session_state["recommendation_detail"] = None

if "data_df" not in st.session_state:
    st.session_state["data_df"] = load_history_data()


def caffeine_remaining(initial_mg: float, hours_passed: float, half_life: float = 5.0) -> float:
    if initial_mg <= 0:
        return 0.0

    hours_passed = max(hours_passed, 0.0)
    return initial_mg * (0.5 ** (hours_passed / half_life))


def get_phase_info(hours_passed: float):
    if hours_passed < PEAK_HOURS:
        return "Increase", "The caffeine effect is building up and has not reached the peak yet."
    elif hours_passed < CRASH_HOURS:
        return "Peak", "The caffeine effect is strong now."
    elif hours_passed < RECOVERY_HOURS:
        return "Crash", "The caffeine effect is going down again."
    else:
        return "Recovery", "Your body is slowly calming down again."


def get_latest_entry(df: pd.DataFrame):
    if df.empty:
        return None

    df_copy = df.copy()
    df_copy["timestamp"] = pd.to_datetime(df_copy["timestamp"], errors="coerce")
    df_copy = df_copy.dropna(subset=["timestamp"]).sort_values("timestamp")

    if df_copy.empty:
        return None

    return df_copy.iloc[-1]


def get_hours_since_timestamp(timestamp) -> float:
    ts = pd.to_datetime(timestamp, errors="coerce")

    if pd.isna(ts):
        return 0.0

    return max(0.0, (pd.Timestamp.now() - ts).total_seconds() / 3600)


def get_initial_caffeine(entry) -> float:
    try:
        return float(entry.get("Caffeine (mg)", 0))
    except:
        return 0.0


def build_curve(total_hours: int = 10):
    x = np.linspace(0, total_hours, 1000)
    y = np.zeros_like(x)

    for i, hour in enumerate(x):
        if hour <= PEAK_HOURS:
            y[i] = hour / PEAK_HOURS
        else:
            y[i] = np.exp(-0.32 * (hour - PEAK_HOURS))

    return x, y


def add_vertical_gradient(ax, x0, x1, y0, y1, color_rgb, alpha_top=0.35, alpha_bottom=0.15, zorder=0):
    n = 256
    gradient = np.ones((n, 2, 4))
    gradient[..., 0] = color_rgb[0]
    gradient[..., 1] = color_rgb[1]
    gradient[..., 2] = color_rgb[2]
    gradient[..., 3] = np.linspace(alpha_top, alpha_bottom, n).reshape(n, 1)

    ax.imshow(
        gradient,
        aspect="auto",
        extent=[x0, x1, y0, y1],
        origin="lower",
        zorder=zorder
    )


def draw_phase_bar(ax):
    bar_y = -0.10
    bar_height = 0.08

    phase_specs = [
        ("Increase", 0, PEAK_HOURS, "#76bb2d"),
        ("Peak", PEAK_HOURS, CRASH_HOURS, "#ff4338"),
        ("Crash", CRASH_HOURS, RECOVERY_HOURS, "#ff9d35"),
        ("Recovery", RECOVERY_HOURS, TOTAL_HOURS, "#7aa8cf"),
    ]

    for label, x0, x1, color in phase_specs:
        rect = patches.Rectangle(
            (x0, bar_y),
            x1 - x0,
            bar_height,
            facecolor=color,
            edgecolor="none",
            alpha=0.95,
            zorder=3
        )

        ax.add_patch(rect)

        ax.text(
            (x0 + x1) / 2,
            bar_y + bar_height / 2,
            label,
            ha="center",
            va="center",
            fontsize=11,
            color="white",
            zorder=4
        )


def plot_colored_segments(ax, x, y):
    phase_segments = [
        (0, PEAK_HOURS, "#76bb2d"),
        (PEAK_HOURS, CRASH_HOURS, "#ff4338"),
        (CRASH_HOURS, RECOVERY_HOURS, "#ff9d35"),
        (RECOVERY_HOURS, TOTAL_HOURS, "#2f6fb0"),
    ]

    for x0, x1, color in phase_segments:
        mask = (x >= x0) & (x <= x1)
        ax.plot(x[mask], y[mask], color=color, linewidth=3, zorder=5)


def draw_recommendation_chart(hours_passed: float):
    x, y = build_curve(TOTAL_HOURS)

    fig, ax = plt.subplots(figsize=(11, 6), dpi=150)
    y_max = 1.1

    add_vertical_gradient(ax, 0, PEAK_HOURS, 0, y_max, (118/255, 187/255, 45/255))
    add_vertical_gradient(ax, PEAK_HOURS, CRASH_HOURS, 0, y_max, (1.0, 67/255, 56/255))
    add_vertical_gradient(ax, CRASH_HOURS, RECOVERY_HOURS, 0, y_max, (1.0, 157/255, 53/255))
    add_vertical_gradient(ax, RECOVERY_HOURS, TOTAL_HOURS, 0, y_max, (122/255, 168/255, 207/255))

    for border_x in [PEAK_HOURS, CRASH_HOURS, RECOVERY_HOURS]:
        ax.axvline(border_x, color=(0, 0, 0, 0.15), linewidth=1)

    plot_colored_segments(ax, x, y)

    current_x = min(max(hours_passed, 0), TOTAL_HOURS)
    current_y = np.interp(current_x, x, y)

    ax.scatter(current_x, current_y, s=120, color="#0d4f8b", zorder=6)

    if current_x < 8.7:
        text_x = current_x + 0.15
        text_ha = "left"
    else:
        text_x = current_x - 0.25
        text_ha = "right"

    ax.text(
        text_x,
        min(current_y + 0.06, 1.05),
        "You are here",
        fontsize=14,
        color="#1f1f1f",
        ha=text_ha,
        va="bottom",
        zorder=7
    )

    draw_phase_bar(ax)

    ax.set_title("Caffeine state over time", fontsize=20, pad=12, color="#5C4033")
    ax.set_xlabel("Hours after caffeine intake", fontsize=14, color="#5C4033")
    ax.set_ylabel("Effect strength", fontsize=14, color="#5C4033")

    ax.set_xlim(0, TOTAL_HOURS)
    ax.set_ylim(-0.12, y_max)
    ax.set_xticks([0, PEAK_HOURS, 2, CRASH_HOURS, 6, RECOVERY_HOURS, 10])
    ax.set_xticklabels(["0", "0.75", "2", "4", "6", "8", "10"])

    ax.tick_params(axis="both", labelsize=11, colors="#5C4033")
    ax.grid(True, alpha=0.12)

    st.pyplot(fig, clear_figure=True)


def show_detail_page(title: str, intro: str, tips: list[str], warning: str):
    st.subheader(title)
    st.write(intro)

    st.markdown("### What can help?")

    for tip in tips:
        st.write(f"• {tip}")

    st.markdown("### Important")
    st.warning(warning)

    if st.button("Back"):
        st.session_state["recommendation_detail"] = None
        st.rerun()


def show_phase_help():
    st.markdown("### Help: What do the phases mean?")

    with st.expander("Increase"):
        st.write("Caffeine is entering your body. The effect is rising and usually reaches its peak after about 45 minutes.")

    with st.expander("Peak"):
        st.write("This is the strongest phase. In this app, the peak starts after about 45 minutes and lasts until around 4 hours.")

    with st.expander("Crash"):
        st.write("The caffeine effect is going down. Some people feel tired, unfocused or low in energy here.")

    with st.expander("Recovery"):
        st.write("Your body is slowly calming down again. The caffeine effect is weaker now.")


selected_detail = st.session_state["recommendation_detail"]

if selected_detail == "Peak":
    show_detail_page(
        title="Peak",
        intro="Your caffeine effect is currently high. This is the phase in which alertness and stimulation are strongest.",
        tips=[
            "Avoid additional caffeine right now.",
            "Drink water to stay hydrated.",
            "Use this phase for focused work, but do not overdo it.",
            "If you feel shaky, take a short break and eat something light."
        ],
        warning="Too much caffeine during the peak phase can increase nervousness, inner restlessness and heartbeat."
    )
    st.stop()

elif selected_detail == "Increase":
    show_detail_page(
        title="Increase",
        intro="Your caffeine effect is currently building up. The peak is usually reached after about 45 minutes.",
        tips=[
            "Do not take more caffeine too quickly.",
            "Wait until the full effect arrives.",
            "Drink water alongside caffeine.",
            "Notice whether your body feels calm, energized or overstimulated."
        ],
        warning="Taking more caffeine during the increase phase can make the later peak stronger than expected."
    )
    st.stop()

elif selected_detail == "Crash":
    show_detail_page(
        title="Crash",
        intro="The caffeine effect is going down. Some people feel tired, unfocused, low in energy or slightly irritable during this phase.",
        tips=[
            "Drink water first and give your body a short pause.",
            "Eat something balanced instead of immediately reaching for more caffeine.",
            "Go outside or move gently for a few minutes.",
            "Avoid a second large caffeine dose if it is already late in the day."
        ],
        warning="Using caffeine repeatedly to escape a crash can create a cycle of stimulation followed by stronger tiredness later."
    )
    st.stop()

elif selected_detail == "I can't fall asleep":
    show_detail_page(
        title="I can't fall asleep",
        intro="There may still be caffeine in your body, especially if you consumed it late in the day.",
        tips=[
            "Do not take more caffeine today.",
            "Avoid screens and bright light before sleep.",
            "Drink water, but not too much right before bed.",
            "Try a calm environment and slow breathing."
        ],
        warning="If sleep problems happen often, reduce caffeine in the afternoon and evening."
    )
    st.stop()

elif selected_detail == "I feel tired":
    show_detail_page(
        title="I feel tired",
        intro="Your caffeine effect may already be dropping. This can happen after the stimulating phase wears off.",
        tips=[
            "Drink water first.",
            "Eat a balanced snack.",
            "Get fresh air or move for a few minutes.",
            "Avoid automatically taking more caffeine immediately."
        ],
        warning="Repeated caffeine use against tiredness can lead to a cycle of short-term stimulation and later tiredness."
    )
    st.stop()

elif selected_detail == "I feel anxious":
    show_detail_page(
        title="I feel anxious",
        intro="High caffeine levels can increase nervousness, restlessness or tension.",
        tips=[
            "Stop caffeine for the rest of the day.",
            "Drink water slowly.",
            "Sit down and breathe slowly and deeply.",
            "Reduce other stimulants if possible."
        ],
        warning="If symptoms are strong or unusual, professional medical advice may be necessary."
    )
    st.stop()

elif selected_detail == "I can't concentrate":
    show_detail_page(
        title="I can't concentrate",
        intro="Too little or too much caffeine can both affect concentration.",
        tips=[
            "Check whether you are in a crash phase or overstimulated.",
            "Drink water and take a short movement break.",
            "Work in short blocks instead of forcing long focus periods.",
            "Avoid taking more caffeine too quickly."
        ],
        warning="Poor concentration is not always caused by caffeine. Sleep, stress and food intake also matter."
    )
    st.stop()

elif selected_detail == "Recovery":
    show_detail_page(
        title="Recovery",
        intro="Your body is slowly returning to a calmer state. The caffeine effect is lower now.",
        tips=[
            "Drink water and listen to your natural energy level.",
            "Fresh air, food or rest may help more than another coffee.",
            "Use this phase to return to a more balanced rhythm.",
            "Avoid taking caffeine automatically just because the effect is fading."
        ],
        warning="If you often rely on caffeine again during recovery, it can become a repeating cycle."
    )
    st.stop()

elif selected_detail == "Stomach discomfort or acidity":
    show_detail_page(
        title="Stomach discomfort or acidity",
        intro="Caffeine can irritate the stomach in some people and may feel worse if you drink it on an empty stomach.",
        tips=[
            "Avoid more caffeine for now, especially coffee or energy drinks.",
            "Drink water slowly.",
            "Eat something mild, for example bread, rice, banana or oatmeal.",
            "Avoid very spicy, acidic or fatty foods for the moment.",
            "Notice whether certain caffeine sources cause more discomfort than others."
        ],
        warning="If stomach pain is strong, keeps coming back, or is combined with vomiting, blood, chest pain or severe burning, seek medical advice."
    )
    st.stop()

elif selected_detail == "I have a headache":
    show_detail_page(
        title="I have a headache",
        intro="Headaches can have many causes. With caffeine, they may be linked to dehydration, too much caffeine, caffeine withdrawal, stress or lack of sleep.",
        tips=[
            "Drink water slowly and rest your eyes for a few minutes.",
            "Eat something if you have not eaten enough.",
            "Avoid taking more caffeine immediately unless you know caffeine withdrawal is likely.",
            "Move gently or get fresh air if it feels helpful.",
            "Track whether headaches happen after high caffeine intake or when you skip caffeine."
        ],
        warning="Seek medical help if the headache is sudden and severe, unusual for you, follows an injury, or comes with fever, confusion, weakness, vision problems or chest pain."
    )
    st.stop()

elif selected_detail == "I am training soon or doing sports":
    show_detail_page(
        title="I am training soon or doing sports",
        intro="Caffeine can support alertness and performance for some people, but too much can also increase nervousness, stomach discomfort or a racing heartbeat during exercise.",
        tips=[
            "Avoid taking extra caffeine if you already feel shaky, anxious or overstimulated.",
            "Drink water before and during training.",
            "Do not train after a large caffeine dose if your stomach feels sensitive.",
            "Keep caffeine moderate and avoid experimenting with high doses.",
            "After training, focus on hydration, food and recovery."
        ],
        warning="Stop exercising and seek help if you feel chest pain, faintness, severe shortness of breath, irregular heartbeat or unusual strong symptoms."
    )
    st.stop()


current_data = load_current_data()
current_entries = current_data.get("entries", [])
end_time = current_data.get("countdown_end_time")
now_unix = int(time.time())

has_active_countdown = bool(current_entries) and end_time and end_time > now_unix

if has_active_countdown:
    current_df = pd.DataFrame(current_entries)

    current_df["timestamp"] = pd.to_datetime(
        current_df["timestamp"],
        errors="coerce"
    )

    current_df = current_df.dropna(subset=["timestamp"])

    if current_df.empty:
        st.info("No valid active caffeine data found. Please use the Caffeine Calculator first.")
        st.stop()

    current_df = current_df.sort_values("timestamp")

    first_timestamp = current_df.iloc[0]["timestamp"]
    latest_entry = current_df.iloc[-1]

    initial_mg = current_df["Caffeine (mg)"].sum()
    hours_passed = get_hours_since_timestamp(first_timestamp)
    current_mg = caffeine_remaining(initial_mg, hours_passed, HALF_LIFE)

    remaining_seconds = max(end_time - now_unix, 0)
    remaining_hours = remaining_seconds / 3600

    st.success("Active caffeine countdown found from your Caffeine Calculator.")

else:
    data_df = load_history_data()
    st.session_state["data_df"] = data_df

    latest_entry = get_latest_entry(data_df)

    if latest_entry is None:
        st.info("No active caffeine countdown found. Please use the Caffeine Calculator first.")
        st.stop()

    initial_mg = get_initial_caffeine(latest_entry)
    hours_passed = get_hours_since_timestamp(latest_entry["timestamp"])
    current_mg = caffeine_remaining(initial_mg, hours_passed, HALF_LIFE)
    remaining_hours = 0


phase_name, phase_text = get_phase_info(hours_passed)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Initial caffeine", f"{initial_mg:.1f} mg")

with col2:
    st.metric("Estimated current caffeine", f"{current_mg:.1f} mg")

with col3:
    st.metric("Current phase", phase_name)

with col4:
    if has_active_countdown:
        st.metric("Countdown remaining", f"{int(remaining_hours)} h {int((remaining_hours % 1) * 60)} min")
    else:
        st.metric("Countdown remaining", "No active countdown")

draw_recommendation_chart(hours_passed)

show_phase_help()

st.success(f"Current interpretation: **{phase_name}** — {phase_text}")

if has_active_countdown:
    last_drink = current_data.get("last_drink", {})
    drink_name = last_drink.get("Drink", "Selected drink")

    st.info(
        f"Last selected drink: **{drink_name}**. "
        "This recommendation page is using the saved active countdown from your Caffeine Calculator."
    )

st.markdown("### Choose how you feel")

col_a, col_b = st.columns(2)

with col_a:
    if st.button("Increase", use_container_width=True):
        st.session_state["recommendation_detail"] = "Increase"
        st.rerun()

    if st.button("Peak", use_container_width=True):
        st.session_state["recommendation_detail"] = "Peak"
        st.rerun()

    if st.button("Crash", use_container_width=True):
        st.session_state["recommendation_detail"] = "Crash"
        st.rerun()

    if st.button("I feel tired", use_container_width=True):
        st.session_state["recommendation_detail"] = "I feel tired"
        st.rerun()

    if st.button("I feel anxious", use_container_width=True):
        st.session_state["recommendation_detail"] = "I feel anxious"
        st.rerun()

    if st.button("Stomach discomfort or acidity", use_container_width=True):
        st.session_state["recommendation_detail"] = "Stomach discomfort or acidity"
        st.rerun()

with col_b:
    if st.button("I can't fall asleep", use_container_width=True):
        st.session_state["recommendation_detail"] = "I can't fall asleep"
        st.rerun()

    if st.button("I can't concentrate", use_container_width=True):
        st.session_state["recommendation_detail"] = "I can't concentrate"
        st.rerun()

    if st.button("I have a headache", use_container_width=True):
        st.session_state["recommendation_detail"] = "I have a headache"
        st.rerun()

    if st.button("I am training soon or doing sports", use_container_width=True):
        st.session_state["recommendation_detail"] = "I am training soon or doing sports"
        st.rerun()

    if st.button("Recovery", use_container_width=True):
        st.session_state["recommendation_detail"] = "Recovery"
        st.rerun()