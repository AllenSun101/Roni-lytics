import streamlit as st
from data.utils import load_data

st.title("Home Page")

data = load_data()
