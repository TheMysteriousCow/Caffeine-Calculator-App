import streamlit as st

st.set_page_config(page_title="Caffeine Calculator", layout="wide")

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    text-align: center;
    font-size: 3.4rem;
    font-family: Georgia, serif;
    font-weight: 600;
    color: #5C4033;
    margin-bottom: 0.3rem;
}

.subtitle {
    text-align: center;
    font-size: 1.1rem;
    font-style: italic;
    color: #5C4033;
    margin-bottom: 2.5rem;
}

/* Wrapper volle Breite */
div[data-testid="stPageLink"] {
    width: 100% !important;
    margin-bottom: 24px;
}

/* Link selbst als große Karte */
div[data-testid="stPageLink"] a {
    width: 100% !important;
    height: 120px !important;
    border-radius: 18px !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.10);
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-decoration: none !important;
    font-size: 1.5rem !important;
    font-weight: 500 !important;
    color: #6b4a3b !important;
}

/* Text mittig */
div[data-testid="stPageLink"] a p {
    font-size: 1.5rem !important;
    color: #6b4a3b !important;
}

/* Farben */
div[data-testid="stPageLink"] a[href*="your_profile"] {
    background-color: #FFF4B8 !important;
}

div[data-testid="stPageLink"] a[href*="additional_data"] {
    background-color: #FFD8B1 !important;
}

div[data-testid="stPageLink"] a[href*="caffeine_calculator"] {
    background-color: #F7C6C7 !important;
}

div[data-testid="stPageLink"] a[href*="statistic"] {
    background-color: #E7A8C9 !important;
}

div[data-testid="stPageLink"] a[href*="recommendations"] {
    background-color: #F8D6E6 !important;
}

div[data-testid="stPageLink"] a[href*="alternatives"] {
    background-color: #CFE8FF !important;
}

div[data-testid="stPageLink"] a[href*="professional_help"] {
    background-color: #6FA3CC !important;
}

div[data-testid="stPageLink"] a:hover {
    filter: brightness(0.97);
    transform: scale(1.01);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Caffeine Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track it. Understand it. Control it.</div>", unsafe_allow_html=True)

left, center, right = st.columns([1.2, 1.6, 1.2])

with center:
    st.page_link("views/your_profile.py", label="Your Profile", use_container_width=True)
    st.page_link("views/additional_data.py", label="Additional Data", use_container_width=True)
    st.page_link("views/caffeine_calculator.py", label="Caffeine Calculator", use_container_width=True)
    st.page_link("views/statistic.py", label="History", use_container_width=True)
    st.page_link("views/recommendations.py", label="Recommendations", use_container_width=True)
    st.page_link("views/alternatives.py", label="Alternatives", use_container_width=True)
    st.page_link("views/professional_help.py", label="Professional Help", use_container_width=True)