import streamlit as st
import altair as alt
import pandas as pd
from datetime import *
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from data.utils import *
from analytics.social_media import *
import numpy as np

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

# KDE plot for 'One_Day_Lag_Sales_Lift'
st.write("## Revenue Lift Percentage One Day After Post")
kde_sales_lift = alt.Chart(filtered_data).transform_density(
    'One_Day_Lag_Sales_Lift', as_=['One_Day_Lag_Sales_Lift', 'density']
).mark_area(
    opacity=0.5, 
    color='steelblue'
).encode(
    x=alt.X('One_Day_Lag_Sales_Lift:Q', title='One Day Lag Sales Lift'),
    y=alt.Y('density:Q', title='Density'),
).properties(
    width=600,
    height=400
)

st.altair_chart(kde_sales_lift, use_container_width=True)

selected_revenues_options = st.multiselect(
    'Filter Posts:', 
    options, 
    key="Revenue", 
)

# Filter the data for selected revenues options
filtered_data = df
for option in selected_revenues_options:
    filtered_data = filtered_data[filtered_data[options_map[option]] == True]

# KDE plot for 'One_Day_Lag_Revenues_Lift'
kde_revenues_lift = alt.Chart(filtered_data).transform_density(
    'One_Day_Lag_Revenues_Lift', as_=['One_Day_Lag_Revenues_Lift', 'density']
).mark_area(
    opacity=0.5, 
    color='orange'
).encode(
    x=alt.X('One_Day_Lag_Revenues_Lift:Q', title='One Day Lag Revenues Lift'),
    y=alt.Y('density:Q', title='Density'),
).properties(
    width=600,
    height=400
)

st.altair_chart(kde_revenues_lift, use_container_width=True)

# Scatter plot for Sales Lift vs. Likes
st.write("## Sales Lift Percentage vs. Post Likes")
sales_lift_scatter = alt.Chart(df).mark_circle().encode(
    x=alt.X('Likes:Q', title='Instagram Likes'),
    y=alt.Y('One_Day_Lag_Sales_Lift:Q', title='Sales Lift'),
    tooltip=['Likes', 'One_Day_Lag_Sales_Lift']
).properties(
    width=600,
    height=400
)

st.altair_chart(sales_lift_scatter, use_container_width=True)

# Scatter plot for Revenue Lift vs. Likes
st.write("## Revenue Lift Percentage vs. Post Likes")
revenues_lift_scatter = alt.Chart(df).mark_circle().encode(
    x=alt.X('Likes:Q', title='Instagram Likes'),
    y=alt.Y('One_Day_Lag_Revenues_Lift:Q', title='Revenue Lift'),
    tooltip=['Likes', 'One_Day_Lag_Revenues_Lift']
).properties(
    width=600,
    height=400
)

st.altair_chart(revenues_lift_scatter, use_container_width=True)


# xgboost model
st.write("## XGBoost Projection of Revenue Lift Percentage One Day After Post ")

cols = st.columns(6)

# Collect inputs with specified names and descriptions
with cols[0]:
    feature_1 = st.text_input("Give Away", help="Enter 1 if the post includes a giveaway, otherwise 0.")

with cols[1]:
    feature_2 = st.text_input("Discount", help="Enter 1 if the post includes a discount offer, otherwise 0.")

with cols[2]:
    feature_3 = st.text_input("Focused on Roni's Food", help="Enter 1 if the content mainly highlights Roni's food, otherwise 0.")

with cols[3]:
    feature_4 = st.text_input("Mentions an Event", help="Enter 1 if the post mentions any community event, otherwise 0.")

with cols[4]:
    feature_5 = st.text_input("Contains a Video", help="Enter 1 if the post contains a video, otherwise 0.")

with cols[5]:
    feature_6 = st.text_input("Number of Likes", help="Enter the number of likes the post has received.")


df['One_Day_Lag_Revenues_Lift'] = pd.to_numeric(df['One_Day_Lag_Revenues_Lift'], errors='coerce')
df.dropna(inplace=True)
X = df[['Give_Away', 'Discount', 'Food_Visual_Focus', 'Mentions_Event', 'Video', 'Likes']]
y = df[["One_Day_Lag_Revenues_Lift"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBRegressor(max_depth=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

if all([feature_1, feature_2, feature_3, feature_4, feature_5, feature_6]):
    try:
        # Aggregate inputs into a numpy array
        input_data = np.array([
            float(feature_1), 
            float(feature_2), 
            float(feature_3), 
            float(feature_4), 
            float(feature_5), 
            float(feature_6)
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data)

        # Display the prediction
        st.write(f"Predicted Revenue Lift: {round(prediction[0] * 100, 2)}%")
        st.write(f"Mean Squared Error of the model: {mse:.2f}")

    except ValueError:
        st.error("Please ensure all inputs are valid numbers.")
else:
    st.info("Please fill in all the fields to get a prediction.")
