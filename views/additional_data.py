import streamlit as st

# Titel
st.markdown(
    "<h1 style='color:#5C4033;'>Additional Data</h1>",
    unsafe_allow_html=True
)

st.write("")

# Previous illness
st.markdown("<h3 style='color:black;'>Previous illness</h3>", unsafe_allow_html=True)
illness_list = st.text_area("Enter previous illnesses (one per line)")

# Medication
st.markdown("<h3 style='color:black;'>Medication</h3>", unsafe_allow_html=True)
medication_list = st.text_area("Enter medications (one per line)")