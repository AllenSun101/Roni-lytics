import streamlit as st
from data.utils import load_data
import analytics.summary_stats as stat

st.title("Roni-lytics")

data = load_data()

for _ in range(3):  # Adjust the range for more or less space
    st.write("")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write(f"## ${stat.best_day(data)[1]:,}")
    st.write(f"**Record Sales on {stat.best_day(data)[0]}**")

with col2:
    st.write(f"## ${stat.total_revenue(data):,}")
    st.write("**Estimated Total Revenue**")

with col3:
    st.write(f"## ${stat.best_avg_day_of_week(data)[1]:,}")
    st.write(f"**Highest Revenue Day ({stat.best_avg_day_of_week(data)[0]})**")


for _ in range(3):  # Adjust the range for more or less space
    st.write("")

st.write("## Most Popular Items")

category = st.selectbox(
    "Select Category",  # Prompt text
    ["Item", "Noodles", "Added Mac", "Cheeses", "Meats", "Toppings", "Drizzles", "Sides", "Drinks"]  # List of hardcoded options
)


counts = stat.aggregate_items_sold(data)
category_map = {"Item": 0, "Noodles": 1, "Added Mac": 2, "Cheeses": 3, "Meats": 4, "Toppings": 5, "Drizzles": 6, "Sides": 7, "Drinks": 8}
category_data = counts[category_map[category]]

print(category_data)
st.bar_chart(category_data, horizontal=True)
