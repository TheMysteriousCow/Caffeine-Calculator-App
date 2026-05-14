import os
import streamlit as st

from functions.logo import set_logo
from functions.professional_help_websites import (
    apply_professional_help_style,
    show_professional_help_header,
    show_professional_help_intro,
    show_professional_help_websites,
    show_professional_help_footer
)

st.set_page_config(page_title="Professional Help", layout="wide")

image_path = os.path.join(os.getcwd(), "images", "logo.png")

set_logo(
    image_path,
    top=15,
    right=-22,
    width=140
)

apply_professional_help_style()
show_professional_help_header()
show_professional_help_intro()
show_professional_help_websites()
show_professional_help_footer()