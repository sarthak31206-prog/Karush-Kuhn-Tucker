import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import base64

st.set_page_config(page_title="KKT Solver", layout="centered")

st.title("📊 KKT Solver")

# ---------------- BACKGROUND  ----------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    css = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

set_bg("bg.png")





# ---------------- INPUT ----------------

# ---------------- PARSE ----------------


# ---------------- MAIN ----------------


        # ---------------- LAGRANGIAN ----------------

        # ---------------- STATIONARITY ----------------


        # ---------------- FULL SOLUTION ----------------


        # ---------------- RESULT ----------------


        # ---------------- QUICK MODE ----------------


        # ---------------- GRAPH ----------------
