import streamlit as st

# Titel
st.markdown(
    "<h1 style='color:#5C4033;'>Your Profile</h1>",
    unsafe_allow_html=True
)

# Eingabefelder
name = st.text_input("Name")
first_name = st.text_input("First name")
gender = st.selectbox("Gender", ["Female", "Male", "Diverse"])
weight = st.text_input("Weight")
height = st.text_input("Height")