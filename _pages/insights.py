import streamlit as st
import altair as alt
from datetime import *
import ast

from data.utils import *
from analytics.dayweek import *

def lc(lis):
    lis = ast.literal_eval(lis)
    # print(lis)
    # print(len(lis))
    if len(lis) == 0:
        return "None"
    if len(lis) == 1:
        # print(lis[0])
        return lis[0]
    else:
        return (lis[0] + " and " + lis[1])

st.title("Predictions")

data = load_data()

container = st.container()
input = container.container()
left, right = input.columns(2)

option = input.selectbox('Select an item', ('Mac and Cheese', 'Grilled Cheese Sandwich'))
output = container.container()


test = get_aggie_meal(data, option)

st.write("## Top Cheeses with this item")
st.write("### 1. ", lc(test[0][0]), " (", round(test[1][0]* 100, 2), "%)")
st.write("### 2. ", lc(test[0][1]), " (", round(test[1][1]* 100, 2), "%)")
st.write("### 3. ", lc(test[0][2]), " (", round(test[1][2]* 100, 2), "%)")

st.write("## Top Meat Combos with this item")
st.write("### 1. ", lc(test[0][3]), " (", round(test[1][3]* 100,2), "%)")
st.write("### 2. ", lc(test[0][4]), " (", round(test[1][4]* 100,2), "%)")
st.write("### 3. ", lc(test[0][5]), " (", round(test[1][5]* 100,2), "%)")

st.write("## Top Topping Combos with this item")
st.write("### 1. ", lc(test[0][6]), " (", round(test[1][6]* 100, 2), "%)")
st.write("### 2. ", lc(test[0][7]), " (", round(test[1][7]* 100, 2), "%)")
st.write("### 3. ", lc(test[0][8]), " (", round(test[1][8]* 100, 2), "%)")


