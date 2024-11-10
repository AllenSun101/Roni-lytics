import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
from data.utils import load_data

# st.logo("logo.png", size="large")

navigation = get_nav_from_toml()

pg = st.navigation(navigation)
pg.run()


data = load_data()

