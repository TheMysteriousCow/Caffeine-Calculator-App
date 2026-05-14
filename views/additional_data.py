import os
import streamlit as st

from functions.logo import set_logo
from functions.additional_data_style import apply_additional_data_style
from functions.additional_data_logic import (
    check_user_data,
    check_no_warning_medications,
    box_class
)


image_path = os.path.join(os.getcwd(), "images", "logo.png")

set_logo(
    image_path,
    top=-30,
    right=-20,
    width=140
)

apply_additional_data_style()

st.markdown(
    "<div class='main-title'>Additional Data</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div class='subtitle'>
Add relevant health information so the app can give more personalised caffeine guidance.
</div>
""", unsafe_allow_html=True)


st.markdown("<h3>Previous illness</h3>", unsafe_allow_html=True)

illness_list = st.text_area(
    "Enter previous illnesses or health conditions, one per line",
    placeholder="Example: high blood pressure, tachycardia, anxiety, reflux, insomnia..."
)

st.markdown("<h3>Allergies or sensitivities</h3>", unsafe_allow_html=True)

allergy_list = st.text_area(
    "Enter allergies or sensitivities, one per line",
    placeholder="Example: caffeine sensitivity, guarana allergy, cocoa allergy, green tea allergy..."
)

st.markdown("<h3>Medication</h3>", unsafe_allow_html=True)

medication_list = st.text_area(
    "Enter medications, one per line",
    placeholder="Example: bisoprolol, methylphenidate, ciprofloxacin, theophylline, Augmentin..."
)


st.markdown("""
<div class='info-box'>
<b>Important note:</b><br>
This app gives general caffeine-related information only. It does not diagnose, treat, prescribe or replace medical advice.
If you have symptoms, a medical condition, take regular medication, are pregnant, or feel unsure, please speak with a doctor,
pharmacist or another qualified healthcare professional.
</div>
""", unsafe_allow_html=True)


if st.button("Check caffeine recommendations"):

    recommendations = check_user_data(
        illness_list,
        allergy_list,
        medication_list
    )

    no_warning_meds = check_no_warning_medications(medication_list)

    st.markdown("<h3>Your caffeine guidance</h3>", unsafe_allow_html=True)

    if recommendations:
        for rec in recommendations:
            st.markdown(f"""
            <div class='{box_class(rec["level"])}'>
            <b>{rec["title"]}</b><br><br>
            {rec["message"]}<br><br>
            <b>{rec["advice"]}</b>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='info-box'>
        <b>Gentle next step:</b><br>
        You do not necessarily have to stop caffeine completely. A realistic first step can be choosing smaller servings,
        avoiding caffeine later in the day, switching to decaf, or checking the Alternatives page.
        </div>
        """, unsafe_allow_html=True)

    if no_warning_meds:
        for med in no_warning_meds:
            st.markdown(f"""
            <div class='neutral-box'>
            <b>{med["title"]}</b><br><br>
            {med["message"]}
            </div>
            """, unsafe_allow_html=True)

    if not recommendations and not no_warning_meds:
        st.markdown("""
        <div class='good-box'>
        <b>No specific caffeine-related warning found.</b><br><br>
        Based on the information entered, the app did not detect a clear caffeine-related condition, allergy or medication note.
        This does not mean caffeine is risk-free for everyone. It simply means that no specific rule in this app was triggered.
        </div>
        """, unsafe_allow_html=True)