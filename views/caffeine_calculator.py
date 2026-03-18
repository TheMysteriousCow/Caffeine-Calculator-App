import pandas as pd
import streamlit as st
import os
from datetime import datetime
from utils.data_manager import DataManager
from functions.caffeine_math import (
    get_default_values,
    calculate_caffeine_data
)

st.title("☕ Koffeinabbau-Rechner")
st.image(os.path.join(os.path.dirname(__file__), "titelbild.png"), use_container_width=True)

if "data_df" not in st.session_state:
    st.session_state["data_df"] = pd.DataFrame()

HALF_LIFE = 5.0

st.caption("Für alle Berechnungen wird eine feste Halbwertszeit von 5 Stunden verwendet.")

with st.form("caffeine_form"):
    drink = st.selectbox(
        "Getränk",
        [
            "Kaffee",
            "Espresso",
            "Energy Drink",
            "Red Bull",
            "NOCCO",
            "Mate",
            "Matcha",
            "Schwarzer Tee",
            "Eigener Wert"
        ]
    )

    default_values = get_default_values()

    col1, col2 = st.columns(2)

    with col1:
        caffeine_per_ml = st.number_input(
            "Koffein pro ml (mg/ml)",
            min_value=0.0,
            max_value=50.0,
            value=float(default_values[drink] / 250 if drink != "Eigener Wert" else 0.0),
            step=0.1
        )

    with col2:
        volume_ml = st.number_input(
            "Getränkemenge (ml)",
            min_value=1.0,
            max_value=1000.0,
            value=250.0,
            step=10.0
        )

    dose_mg = caffeine_per_ml * volume_ml

    intake_time = st.time_input(
        "Uhrzeit der Einnahme",
        value=datetime.now().time().replace(second=0, microsecond=0)
    )

    horizon = st.slider(
        "Berechnungszeitraum (Stunden)",
        min_value=6,
        max_value=48,
        value=24
    )

    submit = st.form_submit_button("Ausrechnen")


if submit:

    result = calculate_caffeine_data(
        drink=drink,
        dose_mg=dose_mg,
        intake_time=intake_time,
        horizon=horizon,
        half_life=HALF_LIFE
    )

    st.metric("Koffein aktuell im Körper (mg)", f"{result['current']:.1f}")
    st.info(f"Verwendete Halbwertszeit: {HALF_LIFE:.1f} Stunden")

    if result["caffeine_zero_time"] is not None:
        st.success(f"✅ Koffein ist nach ca. {result['caffeine_zero_time']} Stunde(n) aus dem Körper")
    else:
        st.warning(f"Innerhalb von {horizon} Stunden ist noch Restkoffein vorhanden")

    st.line_chart(result["df"])

    st.session_state["data_df"] = pd.concat(
        [st.session_state["data_df"], pd.DataFrame([result["new_row"]])],
        ignore_index=True
    )

    data_manager = DataManager()
    data_manager.save_user_data(st.session_state["data_df"], "data.csv")


st.subheader("Verlauf der Getränke")
st.dataframe(st.session_state["data_df"])