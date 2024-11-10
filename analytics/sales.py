import pandas as pd

def sales(start_date, start_time, end_date, end_time):
    df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_processed.csv", parse_dates = ["time"])

    #dfMonth = df.loc[df['Sent Date'].dt.month_name().isin(months)]

    #dfMonth['day'] = dfMonth['Sent Date'].dt.day
    #days = dfMonth.groupby(dfMonth["day"])['Order ID'].nunique()

    start_year, start_month, start_day = start_date.split("-")
    end_year, end_month, end_day = end_date.split("-")

    print(start_month)

    # if monthly, use all data
    if start_year != end_year or start_month != end_month:
        pass
    # if daily
    elif start_day != end_day:
        df = df[df['time'].dt.month == start_month]
    # if hourly
    else:
        pass
    
    timestamps = []
    revenue = []
    current_timestamp = 0
    current_revenue_count = 0

    for row in df:

        # if move to next, reset
        pass

    return timestamps, revenue

print(sales("2024-04-13", "20:00", "2024-09-30", "19:00"))