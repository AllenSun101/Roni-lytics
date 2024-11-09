import streamlit as st
from data.utils import load_data
from analytics.orders import *


st.title("Data Hub")

data = load_data()

st.write(data['Sent Date'].dt.month_name().value_counts())

months = st.multiselect(
    "Please select months", 
    data["Sent Date"].dt.month_name().unique(),
    key = "month_input"
)


monthOrders = orders_in_month(data, months)
st.line_chart(monthOrders)


    