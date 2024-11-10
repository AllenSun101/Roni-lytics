import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_processed.csv", parse_dates = ["time"])
    return df