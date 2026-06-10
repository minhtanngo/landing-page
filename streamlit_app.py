from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mini Dramas Experience Studio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Hide Streamlit chrome and remove all padding so the kiosk fills the screen ---
st.markdown(
    """
    <style>
      #MainMenu, footer,
      [data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      [data-testid="stStatusWidget"] { display: none !important; }

      .stApp { background: #1C2632; }

      .block-container,
      [data-testid="stMainBlockContainer"],
      [data-testid="stAppViewBlockContainer"] {
          padding: 0 !important;
          margin: 0 !important;
          max-width: 100% !important;
      }

      /* stretch the embedded HTML iframe to the full viewport */
      .stApp iframe {
          height: 100svh !important;
          min-height: 100vh !important;
          width: 100% !important;
          border: none !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Load and embed the kiosk ---
html = Path(__file__).parent.joinpath("kiosk.html").read_text(encoding="utf-8")

# `height` is a fallback; the CSS above stretches the iframe to the full screen.
components.html(html, height=1200, scrolling=True)
