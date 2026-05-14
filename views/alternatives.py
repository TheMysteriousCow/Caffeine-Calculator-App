import os
import streamlit as st
import streamlit.components.v1 as components

from functions.logo import set_logo
from functions.alternatives_texts_buttons import (
    ALTERNATIVE_TEXTS,
    init_alternative_state,
    image_button
)

st.set_page_config(page_title="Alternatives", layout="wide")

image_path = os.path.join(os.getcwd(), "images", "logo.png")

set_logo(
    image_path,
    top=-30,
    right=-20,
    width=140
)

init_alternative_state()

st.markdown("""
<style>
.stApp {
    background-color: white;
}

h1, h2, h3, h4, h5, h6, label {
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

.description-text {
    color: #5C4033;
    font-size: 16px;
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin-bottom: 2rem;
}

div.stButton > button {
    width: 100%;
    background-color: #CDECCF;
    color: #5C4033;
    border-radius: 14px;
    height: 45px;
    font-size: 15px;
    margin-bottom: 18px;
    border: none;
    font-family: Arial, sans-serif;
}

.info-box {
    border: 3px solid #CDECCF;
    border-radius: 12px;
    padding: 18px;
    margin-top: 20px;
    background-color: white;
    color: #5C4033;
    font-family: Arial, sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='main-title'>Alternatives</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class='description-text'>
    Here you can explore alternative options to your usual caffeine intake.
    Choosing the right alternative can help you better manage your energy levels,
    reduce side effects such as nervousness or crashes, and support a more balanced and sustainable routine.
    Whether you want a smoother caffeine source or avoid caffeine completely, these options can support your well-being.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='color:#5C4033; font-family: Georgia, serif;'>With Caffeine</h3>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    image_button("Guarana", "images/Guarana.png")

with col2:
    image_button("Green tea", "images/Greentea.png")

with col3:
    image_button("Black tea", "images/Blacktea.png")

st.markdown(
    "<h3 style='color:#5C4033; font-family: Georgia, serif;'>Without Caffeine</h3>",
    unsafe_allow_html=True
)

col4, col5, col6 = st.columns(3)

with col4:
    image_button("Ginger", "images/Ginger.png")

with col5:
    image_button("Herbal tea", "images/Herbaltea.png")

with col6:
    image_button("Kokoa", "images/Cocoa.png")

if st.session_state.selected_alternative:
    selected = st.session_state.selected_alternative

    st.markdown('<div id="result-box"></div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="info-box">
            <h4 style="color:#5C4033;">{selected}</h4>
            <div>{ALTERNATIVE_TEXTS[selected]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    components.html(
        f"""
        <script>
            setTimeout(function() {{
                const element = window.parent.document.getElementById("result-box");
                if (element) {{
                    element.scrollIntoView({{
                        behavior: "smooth",
                        block: "start"
                    }});
                }}
            }}, 150);
        </script>

        <div style="display:none;">
            {st.session_state.scroll_counter}
        </div>
        """,
        height=0
    )