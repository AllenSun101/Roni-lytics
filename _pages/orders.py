import streamlit as st
import altair as alt
from datetime import *

from data.utils import *
from analytics.orders import *

data = load_data()
special_events = load_special_events_data()

st.title("Orders Hub")


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

end_date = left1.date_input("Choose a end date:", start_date, 
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
    test = get_num_orders(data, start_datetime, end_datetime)
    events = special_events.loc[(special_events["Start_Time"] > start_datetime) & (special_events['Start_Time'] < end_datetime)]
    

    if (end_datetime - start_datetime > timedelta(days = 69)):
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('Time:T', title='Date', axis = alt.Axis(format='%B', tickCount = 4)),  
            y=alt.Y('Order Count:Q', title='Order Count')  
        )

        events = pd.DataFrame({
            'time': ['None'] * len(events) ,
            'event_name': ['None'] * len(events)})
        

    elif (end_datetime - start_datetime > timedelta(days = 7)):
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('Time:T', title='Date', axis = alt.Axis(format='%b %d')),  
            y=alt.Y('Order Count:Q', title='Order Count')  
        )

        events = pd.DataFrame({
            'time': events['Start_Time'].dt.strftime('%m-%d') ,
            'event_name': events['Event_Name']  
        })

    elif (end_datetime - start_datetime > timedelta(days = 3)):
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('Time:T', title='Date', axis = alt.Axis(format='%b %d', tickCount = 3)),  
            y=alt.Y('Order Count:Q', title='Order Count')  
        )

        events = pd.DataFrame({
            'time': events['Start_Time'].dt.strftime('%m-%d') ,
            'event_name': events['Event_Name']  
        })
    else:
        chart = alt.Chart(test).mark_line().encode(
            x=alt.X('time:T', title = 'Date', axis = alt.Axis(format='%b-%d-%I-%p', tickCount = 14, labelAngle = -30)),  
            y=alt.Y('Order Count:Q', title='Order Count')  
        )

        


    annotations = alt.Chart(events).mark_rule(color='red', strokeDash=[6, 3]).encode(
        x='time:T',
        size=alt.value(2),
        tooltip=[
        alt.Tooltip('time:T', title='Date', format='%b %d'),  
        alt.Tooltip('event_name:N', title='Event')      
    ]
    )


    final_chart = chart + annotations
    container.write("")
    container.write("")
    container.altair_chart(final_chart, use_container_width=True)


