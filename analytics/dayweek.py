import pandas as pd
from datetime import datetime

def rev_orders_by_day_of_week(df, day_name):
    df = df.dropna(subset=['time'])
    df['time'] = pd.to_datetime(df['time']) 

    if isinstance(day_name, str):
        day_name = [day_name]

    data = df.loc[df['time'].dt.day_name().isin(day_name)]
    data = data.copy()

    data['day'] = data['time'].dt.day
    data['hour'] = data['time'].dt.hour
    data['month_day'] = data['time'].dt.strftime('%B %d')


    count = data['month_day'].nunique()

    out = data.groupby('hour')['orderID'].nunique().reset_index()
    out = out.rename(columns={"orderID": "Orders"})

    out = out[out['hour'] > 8]
    out['Orders'] = out['Orders']/count
    return out

def rev_by_day_of_week(df, day_name):
    df = df.dropna(subset=['time'])
    df['time'] = pd.to_datetime(df['time']) 

    if isinstance(day_name, str):
        day_name = [day_name]

    data = df.loc[df['time'].dt.day_name().isin(day_name)]
    data = data.copy()

    data['day'] = data['time'].dt.day
    data['hour'] = data['time'].dt.hour
    data['month_day'] = data['time'].dt.strftime('%B %d')


    count = data['month_day'].nunique()

    out = data.groupby('hour')['cost'].sum().reset_index()
    out = out.rename(columns={"cost": "revenue"})

    out = out[out['hour'] > 8]
    out['revenue'] = out['revenue']/count
    return out



