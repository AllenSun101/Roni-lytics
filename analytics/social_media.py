import pandas as pd
from datetime import *

def social_media_immediate_lift(df_data, df_insta):
    df_data["Time"] = df_data['time'].dt.strftime('%Y-%m-%d') + " 00:00:00"
    df_data["Time"] = pd.to_datetime(df_data["Time"])
    sales = df_data.groupby("Time")['orderID'].nunique()
    revenues = df_data.groupby("Time")['cost'].sum()

    df_insta["One_Day_Lag_Sales"] = pd.NA
    df_insta["One_Day_Lag_Revenues"] = pd.NA
    df_insta["Two_Day_Lag_Sales"] = pd.NA
    df_insta["Two_Day_Lag_Revenues"] = pd.NA
    df_insta["One_Day_Lag_Sales_Lift"] = pd.NA
    df_insta["One_Day_Lag_Revenues_Lift"] = pd.NA
    df_insta["Two_Day_Lag_Sales_Lift"] = pd.NA
    df_insta["Two_Day_Lag_Revenues_Lift"] = pd.NA

    for index, row in df_insta.iterrows():
        current_date = row["Date"]
        
        if current_date in sales:
            if current_date + pd.Timedelta(days=1) in sales:
                df_insta.loc[index, "One_Day_Lag_Sales"] = sales[current_date + pd.Timedelta(days=1)]
                df_insta.loc[index, "One_Day_Lag_Revenues"] = revenues[current_date + pd.Timedelta(days=1)]

                df_insta.loc[index, "One_Day_Lag_Sales_Lift"] = (df_insta["One_Day_Lag_Sales"].iloc[index] - sales[current_date]) / sales[current_date]
                df_insta.loc[index, "One_Day_Lag_Revenues_Lift"] = (df_insta["One_Day_Lag_Revenues"].iloc[index] - revenues[current_date]) / revenues[current_date]

            if current_date + pd.Timedelta(days=2) in sales:
                df_insta.loc[index, "Two_Day_Lag_Sales"] = sales[current_date + pd.Timedelta(days=2)]
                df_insta.loc[index, "Two_Day_Lag_Revenues"] = revenues[current_date + pd.Timedelta(days=2)]

                df_insta.loc[index, "Two_Day_Lag_Sales_Lift"] = (df_insta["Two_Day_Lag_Sales"].iloc[index] - sales[current_date]) / sales[current_date]
                df_insta.loc[index, "Two_Day_Lag_Revenues_Lift"] = (df_insta["Two_Day_Lag_Revenues"].iloc[index] - revenues[current_date]) / revenues[current_date]

    return df_insta


# xgboost model- projections in lift
