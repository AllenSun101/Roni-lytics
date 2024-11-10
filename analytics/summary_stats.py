import pandas as pd
import ast

def aggregate_items_sold(df):
    """Returns total orders and items sold"""

    item_counts = {}
    noodles_counts = {}
    added_mac_counts = {}
    cheese_counts = {}
    meats_counts = {}
    toppings_counts = {}
    drizzles_counts = {}
    sides_counts = {}
    drinks_counts = {}

    for i in range(len(df)):
        item = df.iloc[i]

        if item["item"] not in item_counts:
            item_counts[item["item"]] = 1
        else:
            item_counts[item["item"]] += 1

        if item["noodles"] not in noodles_counts:
            noodles_counts[item["noodles"]] = 1
        else:
            noodles_counts[item["noodles"]] += 1

        macs = ast.literal_eval(item["added_mac"])
        macs = list(set(macs))
        for mac in macs:
            if mac not in added_mac_counts:
                added_mac_counts[mac] = 1
            else:
                added_mac_counts[mac] += 1

        cheeses = ast.literal_eval(item["cheese"])
        cheeses = list(set(cheeses))
        for cheese in cheeses:
            if cheese not in cheese_counts:
                cheese_counts[cheese] = 1
            else:
                cheese_counts[cheese] += 1

        meats = ast.literal_eval(item["meats"])
        meats = list(set(meats))
        for meat in meats:
            if meat not in meats_counts:
                meats_counts[meat] = 1
            else:
                meats_counts[meat] += 1

        toppings = ast.literal_eval(item["toppings"])
        toppings = list(set(toppings))
        for topping in toppings:
            if topping not in toppings_counts:
                toppings_counts[topping] = 1
            else:
                toppings_counts[topping] += 1

        drizzles = ast.literal_eval(item["drizzles"])
        drizzles = list(set(drizzles))
        for drizzle in drizzles:
            if drizzle not in drizzles_counts:
                drizzles_counts[drizzle] = 1
            else:
                drizzles_counts[drizzle] += 1

        sides = ast.literal_eval(item["sides"])
        sides = list(set(sides))
        for side in sides:
            if side not in sides_counts:
                sides_counts[side] = 1
            else:
                sides_counts[side] += 1

        drinks = ast.literal_eval(item["drinks"])
        drinks = list(set(drinks))
        for drink in drinks:
            if drink not in drinks_counts:
                drinks_counts[drink] = 1
            else:
                drinks_counts[drink] += 1

    return item_counts, noodles_counts, added_mac_counts, cheese_counts, meats_counts, toppings_counts, drizzles_counts, sides_counts, drinks_counts


def total_revenue(df):
    """Returns total estimated revenue so far"""
    return df['cost'].sum()


def best_day(df):
    """Returns total estimated revenue so far"""
    day = df.groupby(df['time'].dt.date)['cost'].sum().idxmax()
    value = df.groupby(df['time'].dt.date)['cost'].sum().max()
    return day, value


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

def best_avg_day_of_week(df):
    revenues = average_revenue_day_of_week(df)
    return revenues.idxmax(), revenues.max()

# df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_processed.csv", parse_dates = ["time"])
# print(best_day(df))