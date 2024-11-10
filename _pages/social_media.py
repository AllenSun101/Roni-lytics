import streamlit as st
import altair as alt
import pandas as pd
from datetime import *
import seaborn as sns
import matplotlib.pyplot as plt

from data.utils import *
from analytics.social_media import *

data = load_data()
social_media = load_instagram_data()

st.title("Social Media Analytics")

for _ in range(3):  # Adjust the range for more or less space
    st.write("")

st.write("## Sales Lift Percentage One Day After Post ")

df = social_media_immediate_lift(data, social_media)

options = ['Mentions Giveaways', 'Mentions Discounts', 'Focuses on Food', 'Mentions Event', 'Includes Video']
options_map = {'Mentions Giveaways' : 'Give_Away', 'Mentions Discounts': 'Discount', 'Focuses on Food': 'Food_Visual_Focus', 'Mentions Event': 'Mentions_Event', 'Includes Video': 'Video'}

selected_sales_options = st.multiselect(
    'Filter Posts:', 
    options, 
    key="Sales", 
)

filtered_data = df
for option in selected_sales_options:
    filtered_data = filtered_data[filtered_data[options_map[option]] == True]

print(filtered_data["One_Day_Lag_Sales_Lift"].median())

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
sns.kdeplot(filtered_data["One_Day_Lag_Sales_Lift"], shade=True, ax=ax)

# Display plot in Streamlit
st.pyplot(fig)

st.write("## Revenue Lift Percentage One Day After Post ")

selected_revenues_options = st.multiselect(
    'Filter Posts:', 
    options, 
    key="Revenue", 
)

filtered_data = df
for option in selected_revenues_options:
    filtered_data = filtered_data[filtered_data[options_map[option]] == True]

print(filtered_data["One_Day_Lag_Revenues_Lift"].median())

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
sns.kdeplot(filtered_data["One_Day_Lag_Revenues_Lift"], shade=True, ax=ax)

# Display plot in Streamlit
st.pyplot(fig)

st.write("## Sales Lift Percentage vs. Post Likes ")
st.scatter_chart(data=df, x="Likes", y="One_Day_Lag_Sales_Lift", x_label="Instagram Likes", y_label="Sales Lift", use_container_width=True)

st.write("## Revenue Lift Percentage vs. Post Likes ")
st.scatter_chart(data=df, x="Likes", y="One_Day_Lag_Revenues_Lift", x_label="Instagram Likes", y_label="Revenue Lift", use_container_width=True)
