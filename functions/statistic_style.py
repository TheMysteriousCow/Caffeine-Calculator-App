import streamlit as st


def apply_statistic_style():
    st.markdown("""
<style>
.stApp {
    background-color: white;
    color: #5C4033 !important;
}

html, body, p, div, span, label, input, textarea,
h1, h2, h3, h4, h5, h6,
.stMarkdown, .stText, .stCaption,
[data-testid="stMarkdownContainer"],
[data-testid="stText"],
[data-testid="stWidgetLabel"],
[data-testid="stCaptionContainer"],
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    color: #5C4033 !important;
}

[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p {
    color: #5C4033 !important;
    font-family: Arial, sans-serif !important;
    font-weight: 400 !important;
}

div[data-baseweb="input"],
div[data-baseweb="base-input"],
div[data-baseweb="textarea"],
div[data-baseweb="select"] {
    background-color: #EDEFF2 !important;
    border-radius: 14px !important;
    color: #5C4033 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="base-input"] > div,
div[data-baseweb="textarea"] > div,
div[data-baseweb="select"] > div {
    background-color: #EDEFF2 !important;
    border-radius: 14px !important;
    color: #5C4033 !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="base-input"] input,
div[data-baseweb="textarea"] textarea,
textarea,
input {
    background-color: #EDEFF2 !important;
    color: #5C4033 !important;
    font-family: Arial, sans-serif !important;
    font-weight: 400 !important;
}

input::placeholder,
textarea::placeholder {
    color: #8B6F63 !important;
}

[data-testid="stDateInput"],
[data-testid="stTimeInput"] {
    background-color: transparent !important;
}

[data-testid="stDateInput"] div[data-baseweb="input"],
[data-testid="stTimeInput"] div[data-baseweb="input"] {
    background-color: #EDEFF2 !important;
    border-radius: 14px !important;
}

[data-testid="stDateInput"] div[data-baseweb="input"] > div,
[data-testid="stTimeInput"] div[data-baseweb="input"] > div {
    background-color: #EDEFF2 !important;
    border-radius: 14px !important;
}

[data-testid="stDateInput"] input,
[data-testid="stTimeInput"] input {
    background-color: #EDEFF2 !important;
    color: #5C4033 !important;
}

[data-testid="stTextArea"] textarea {
    background-color: #EDEFF2 !important;
    color: #5C4033 !important;
    border-radius: 14px !important;
}

div[data-baseweb="input"] svg,
div[data-baseweb="select"] svg {
    color: #5C4033 !important;
    fill: #5C4033 !important;
}

div[data-baseweb="popover"],
div[data-baseweb="menu"],
div[data-baseweb="calendar"] {
    background-color: #EDEFF2 !important;
    color: #5C4033 !important;
}

div[data-baseweb="popover"] *,
div[data-baseweb="menu"] *,
div[data-baseweb="calendar"] * {
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

.section-title {
    font-size: 1.8rem;
    font-family: 'Georgia', serif;
    font-weight: 600;
    color: #5C4033 !important;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

div.stButton > button {
    background-color: #CDECCF !important;
    color: #5C4033 !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
}

div.stButton > button:hover {
    background-color: #BEE6C2 !important;
    color: #5C4033 !important;
}

[data-testid="stSidebar"] button {
    background-color: white !important;
    color: #5C4033 !important;
}

[data-testid="stAlert"] {
    background-color: #EDEFF2 !important;
    color: #5C4033 !important;
    border-radius: 14px !important;
    border: none !important;
}

[data-testid="stAlert"] * {
    color: #5C4033 !important;
}

[data-testid="stDataFrame"] {
    background-color: #EDEFF2 !important;
    border-radius: 14px !important;
    padding: 10px !important;
    color: #5C4033 !important;
}

[data-testid="stDataFrame"] * {
    color: #5C4033 !important;
}

[data-testid="stDataFrame"] div,
[data-testid="stDataFrame"] span,
[data-testid="stDataFrame"] button {
    color: #5C4033 !important;
}

table {
    background-color: #EDEFF2 !important;
    color: #5C4033 !important;
    border-radius: 14px !important;
}

thead, tbody, tr, th, td {
    background-color: #EDEFF2 !important;
    color: #5C4033 !important;
}

.diary-card {
    border: 2px solid #D7D9DD;
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 10px;
    background-color: #EDEFF2;
    color: #5C4033 !important;
}

.diary-card * {
    color: #5C4033 !important;
}
</style>
""", unsafe_allow_html=True)