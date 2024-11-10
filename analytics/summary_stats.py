import pandas as pd
import ast
import random

def aggregate_items_sold(df, category):
    """Returns total orders and items sold"""

    type1 = {"Item", "Noodles"} 
    type2 = {"Added Mac", "Cheeses", "Meats", "Toppings", "Drizzles", "Sides", "Drinks"}

    MAP = {"Item": "item",
           "Noodles": "noodles",
           "Added Mac": "added_mac",
           "Cheeses" : "cheese",
           "Meats": "meats",
           "Toppings": "toppings",
           "Drizzles": "drizzles",
           "Sides" : "sides",
           "Drinks": "drinks"
           }
    
    COLOR_BANK = [
        "#FF5733", "#33FF57", "#5733FF", "#FF33A1", "#FF8C00", "#00FFFF", 
        "#8A2BE2", "#DC143C", "#FF1493", "#00FF7F", "#FFD700", "#ADFF2F", 
        "#FF6347", "#1E90FF", "#F0E68C", "#FF00FF", "#800080", "#008000", 
        "#FF4500", "#2E8B57"
    ]   

    if category in type1:
        key = MAP[category]
        output = df[key].value_counts().reset_index()
        colors = random.sample(COLOR_BANK, len(output))
        output["colors"] = colors
        output = output.rename(columns = {MAP[category] : category})
        return output
    else:
        output = {}
        for row in range(len(df)):
            item = df.iloc[row]

            fields = ast.literal_eval(item[MAP[category]])
            fields = list(set(fields))

            for item in fields:
                if item not in output:
                    output[item] = 1
                else:
                    output[item] += 1

        output = [[key, output[key]] for key in output]
        output = pd.DataFrame(output)
        output = output.rename(columns = {0: category, 1: "count"})
        output = output.sort_values(by = "count", ascending = False)
        colors = random.sample(COLOR_BANK, len(output))
        output["colors"] = colors

        return output


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