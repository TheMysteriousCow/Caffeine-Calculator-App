import os
import base64
import streamlit as st


def set_logo(
    image_file: str,
    top: int = -40,
    right: int = -20,
    width: int = 140,
    position: str = "absolute",
):
    """
    Zeigt ein Logo mit frei definierbarer Position an.

    Parameters:
    ----------
    image_file : str
        Pfad zum Bild
    top : int
        Abstand von oben in px
    right : int
        Abstand von rechts in px
    width : int
        Breite des Bildes in px
    position : str
        CSS-Positionierung (absolute, fixed, relative)
    """

    if not os.path.exists(image_file):
        st.warning(f"Bild konnte nicht geladen werden. Pfad: {image_file}")
        return

    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    css = f"""
    <style>
    .logo-container {{
        position: {position};
        top: {top}px;
        right: {right}px;
        z-index: 100;
    }}

    .logo-img {{
        width: {width}px;
        height: auto;
    }}
    </style>

    <div class="logo-container">
        <img src="data:image/png;base64,{encoded}" class="logo-img">
    </div>
    """

    st.markdown(css, unsafe_allow_html=True)
