from datetime import timedelta
import pandas as pd

def get_revenues(df, start_time, end_time):
    data = df.loc[(df['time'] >= start_time) & (df['time'] <= end_time)]
    data = data.copy()

    if (end_time - start_time > timedelta(days = 69)):
        data["Time"] = data['time'].dt.strftime('%m')  
        out = data.groupby("Time")['cost'].sum()
        out = out.to_frame(name = "Total Revenue").reset_index()
        out = out.rename(columns={"revenue": "Total Revenue"})
    elif ((start_time.month != end_time.month) or (end_time - start_time > timedelta(days = 3))):
        data["Time"] = data['time'].dt.strftime('%m-%d')  
        out = data.groupby("Time")['cost'].sum()
        out = out.to_frame(name = "Total Revenue").reset_index()
        out = out.rename(columns={"revenue": "Total Revenue"})
    else:
        out = data.groupby(pd.Grouper(key='time', freq='1h'))['cost'].sum()
        out = out.to_frame(name="Total Revenue").reset_index()
        out = out.rename(columns={"revenue": "Total Revenue"})
        
    pd.set_option('display.max_rows', None)  # Show all rows
    pd.set_option('display.max_columns', None)  # Show all columns

                
    # print(data[["time", "cost"]])

    return out

