import streamlit as st
import altair as alt
import pandas as pd
from datetime import *

from data.utils import load_data
from analytics.sales import *

data = load_data()

st.title("Revenue Hub")


# Getting inputs through a container
container = st.container()

input = container.container()
left, right = input.columns(2)

start_date = left.date_input("Choose a start date:", data['time'].min(), 
                             min_value = data["time"].min(), 
                             max_value = data["time"].max(),
                             format = "MM/DD/YYYY",
                             key = "start_date"
                            )

start_time = right.time_input("Choose an end time:", time(11, 0),
                              step = timedelta(minutes = 30),
                              key = "start_time"
                              )

start_datetime = datetime.combine(start_date, start_time)


output = container.container()
left1, right1 = output.columns(2)

end_date = left1.date_input("Choose a start date:", start_date, 
                             min_value = start_date, 
                             max_value = data["time"].max(),
                             format = "MM/DD/YYYY",
                             key = "end_date"
                            )

end_time = right1.time_input("Choose an end time:", time(22, 59) ,
                              step = timedelta(minutes = 30),
                              key = "end_time"
                              )

end_datetime = datetime.combine(end_date, end_time)


if (start_datetime > end_datetime):
    st.write(":red[Error: Start time must be before end time]")
else:
    test = get_revenues(data, start_datetime, end_datetime)

    if (end_datetime - start_datetime > timedelta(days = 69)):
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('Time:T', title='Date', axis = alt.Axis(format='%B', tickCount = 4)),  
            y=alt.Y('Total Revenue:Q', title='Revenue')  
        )
    elif (end_datetime - start_datetime > timedelta(days = 6)):
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('Time:T', title='Date', axis = alt.Axis(format='%b %d')),  
            y=alt.Y('Total Revenue:Q', title='Revenue')  
        )
    elif (end_datetime - start_datetime > timedelta(days = 3)):
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('Time:T', title='Date', axis = alt.Axis(format='%b %d', tickCount = 3)),  
            y=alt.Y('Total Revenue:Q', title='Revenue')  
        )
    else:
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('time:T', title = 'Date', axis = alt.Axis(format='%b-%d-%I-%p', tickCount = 14)),  
            y=alt.Y('Total Revenue:Q', title='Revenue')  
        )


    container.write("")
    container.write("")
    container.altair_chart(chart, use_container_width=True)


    






# container = st.container()
# container.write("Choose period over which you want to see order count")

# month = st.selectbox(
#     "Please select month to look at stats for", 
#     data["Sent Date"].dropna().dt.month_name().unique(),
#     key = "month_input",
#     index = 1
# )

# st.write("")
# st.write("")
# monthOrders = orders_in_month(data, month)
# st.line_chart(monthOrders, x_label = month, y_label = "Orders")


# dayOrders = orders_in_day(data, month, 23)
# # print(dayOrders)
# st.line_chart(dayOrders, x_label = f'Hour', y_label = "Orders")


    