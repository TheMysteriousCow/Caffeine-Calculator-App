import streamlit as st


def apply_additional_data_style():
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Georgia', 'Times New Roman', serif;
        color: #5C4033;
    }

    h1, h2, h3, h4, h5, h6, p, label {
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

    .subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #5C4033;
        margin-bottom: 2rem;
    }

    .stTextArea label {
        color: #5C4033 !important;
        font-family: 'Georgia', 'Times New Roman', serif;
    }

    .stTextArea textarea {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
        border: 1.5px solid #B8B8B8 !important;
        border-radius: 10px !important;
        box-shadow: none !important;
        font-family: Arial, sans-serif !important;
    }

    .stTextArea textarea:focus {
        background-color: #EDEFF2 !important;
        color: #5C4033 !important;
        border: 1.5px solid #5C4033 !important;
        box-shadow: none !important;
        outline: none !important;
    }

    .stTextArea textarea::placeholder {
        color: #8B8B8B !important;
    }

    .info-box, .warning-box, .good-box, .avoid-box, .neutral-box {
        padding: 1rem 1.2rem;
        border-radius: 14px;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #5C4033;
        line-height: 1.55;
    }

    .info-box {
        background-color: #F8F1EB;
        border-left: 6px solid #B98B73;
    }

    .warning-box {
        background-color: #FFF3E8;
        border-left: 6px solid #D08A45;
    }

    .avoid-box {
        background-color: #FBEAEA;
        border-left: 6px solid #B95C5C;
    }

    .good-box {
        background-color: #EEF7EE;
        border-left: 6px solid #7FA87F;
    }

    .neutral-box {
        background-color: #F4F1EF;
        border-left: 6px solid #A89B93;
    }

    .small-note {
        font-size: 0.9rem;
        color: #6B4E3D;
    }

    div.stButton > button {
        background-color: #CDECCF;
        color: #5C4033;
        border-radius: 14px;
        height: 45px;
        font-size: 15px;
        border: none;
        font-family: 'Georgia', 'Times New Roman', serif;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #BFE3C1;
        color: #5C4033;
    }
    </style>
    """, unsafe_allow_html=True)