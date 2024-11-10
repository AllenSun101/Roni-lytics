import pandas as pd

def sales(start_date, start_time, end_date, end_time):
    df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_processed.csv", parse_dates = ["time"])

    #dfMonth = df.loc[df['Sent Date'].dt.month_name().isin(months)]
    
    #dfMonth['day'] = dfMonth['Sent Date'].dt.day
    #days = dfMonth.groupby(dfMonth["day"])['Order ID'].nunique()

    return df.iloc[0]

print(sales("2024-04-13", "20:00", "2024-09-30", "19:00"))