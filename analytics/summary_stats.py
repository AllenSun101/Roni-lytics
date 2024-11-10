import pandas as pd

def aggregate_items_sold():
    """Returns total orders and items sold"""

    item = {}
    noodles = {}


    df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_processed.csv", parse_dates = ["time"])
    
    df = df.drop_duplicates(subset='orderID', keep='first')

    df['month'] = df['time'].dt.month

    # Get the value counts for each month
    month_counts = df['month'].value_counts()
    print(month_counts)


def most_popular_order_combinations():
    """Returns most popular customizations"""

def total_revenue():
    """Returns total revenue so far"""

def average_revenue_day_of_week():
    """Returns average revenue by day of week"""

aggregate_items_sold()