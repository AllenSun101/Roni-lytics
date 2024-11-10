import streamlit as st
import numpy as np

from data.utils import load_data
import analytics.summary_stats as stat
import datetime

st.title("Roni-lytics")

data = load_data()

for _ in range(2):  # Adjust the range for more or less space
    st.write("")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    best_data = stat.best_day(data)[0]
    date = datetime.datetime.strptime(str(best_data), "%Y-%m-%d")
    formatted_date = date.strftime("%B %d")

    st.write(f"## ${stat.best_day(data)[1]:,}")
    st.write(f"**Record Sales on {formatted_date}**")

with col2:
    st.write(f"## ${stat.total_revenue(data):,}")
    st.write("**Estimated Total Revenue**")

with col3:
    st.write(f"## ${stat.best_avg_day_of_week(data)[1]:,}")
    st.write(f"**Highest Revenue Day ({stat.best_avg_day_of_week(data)[0]})**")


for _ in range(3):  # Adjust the range for more or less space
    st.write("")

st.write("### Most Popular Choices")

category = st.selectbox(
    "Select Category",  # Prompt text
    ["Item", "Noodles", "Added Mac", "Cheeses", "Meats", "Toppings", "Drizzles", "Sides", "Drinks"],  # List of hardcoded options
    index = 5
)


counts = stat.aggregate_items_sold(data, category) 

st.bar_chart(counts, x = category, y = "count", horizontal = True, color = "colors", x_label = "Frequency")

