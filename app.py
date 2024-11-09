import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

navigation = get_nav_from_toml()
pg = st.navigation(navigation)
pg.run()


