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
