import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_full.csv", parse_dates = ["Sent Date"])
    return df