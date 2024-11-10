import streamlit as st
import pandas as pd
from datetime import timedelta

from data.utils import load_data
from analytics.orders import *

data = load_data()

st.title("Orders Hub")


container = st.container()

input = container.container()
left, right = input.columns(2)

start_date = left.date_input("Choose a start date:", data['Sent Date'].min(), 
                             min_value = data["Sent Date"].min(), 
                             max_value = data["Sent Date"].max(),
                             format = "MM/DD/YYYY",
                             key = "start_date"
                            )

start_time = right.time_input("Choose a start time:", step = timedelta(minutes = 10),
                              key = "start_time"
                              )


output = container.container()
left1, right1 = output.columns(2)

end_date = left1.date_input("Choose a start date:", start_date, 
                             min_value = start_date, 
                             max_value = data["Sent Date"].max(),
                             format = "MM/DD/YYYY",
                             key = "end_date"
                            )

end_time = right1.time_input("Choose a start time:", start_time ,
                              step = timedelta(minutes = 10),
                              key = "end_time"
                              )




    