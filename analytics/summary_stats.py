import pandas as pd

# All time Stats

# most popular toppings

# most order day
# most items ordered per day
# most sales revenue day
# most popular hours by average revenue

# Last month Stats

# Comparison to previous month


def aggregate_items_sold():
    """Returns total orders and items sold"""

    item_counts = {}
    noodles_counts = {}
    added_mac_counts = {}
    cheese_counts = {}
    meats_counts = {}
    tops_counts = {}
    drizzle_counts = {}
    sides_counts = {}

    df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_processed.csv", parse_dates = ["time"])
    for i in range(len(df)):
        item = df.iloc[i]
        for col in df.columns:
            if col in ["orderID", "time", "note", "cost", "utensils"]:
                continue
            if col in ["added_mac", "cheese", "meats", "tops", "drizzle", "sides", "drinks", ""]:
                continue
            if item[col] not in item_counts:
                item_counts[item[col]] = 1
            else:
                item_counts[item[col]] += 1

    print(item)


def total_revenue(df):
    """Returns total estimated revenue so far"""
    return df['cost'].sum()


def average_revenue_day_of_week(df):
    """Returns average revenue by day of week"""
    daily_revenue = df.groupby(df['time'].dt.date)['cost'].sum()
    daily_revenue = daily_revenue.reset_index()
    daily_revenue['date'] = pd.to_datetime(daily_revenue['time'])


    daily_revenue['day_of_week'] = daily_revenue['date'].dt.dayofweek
    average_revenue = daily_revenue.groupby('day_of_week')['cost'].mean().round(2)
    average_revenue.index = average_revenue.index.map({
            0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 
            4: 'Friday', 5: 'Saturday', 6: 'Sunday'
        })
    return average_revenue

df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_processed.csv", parse_dates = ["time"])
print(average_revenue_day_of_week(df))