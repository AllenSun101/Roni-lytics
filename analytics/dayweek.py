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
    data['month'] = data['time'].dt.month
    data['month_day'] = data['time'].dt.strftime('%B %d')


    count = data['month_day'].nunique()

    # count = data['day'].nunique()
    
    count = len(data['month'].drop_duplicates().reset_index(drop=True))
    print(count)
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


def get_aggie_meal(df, storage):
    # dataframe and a storage dictionary that has other things
    if (True):
        newdf = df[df['item'] == storage]
        cheeseitem = newdf['cheese'].value_counts().reset_index()
        size = len(newdf)

        print(cheeseitem)

        result = [cheeseitem['cheese'][0], cheeseitem['cheese'][1], cheeseitem['cheese'][2]]
        predict = [cheeseitem['count'][0], cheeseitem['count'][1], cheeseitem['count'][2]]

        meatitem = newdf['meats'].value_counts().reset_index()
        
        result.append(meatitem['meats'][0])
        result.append(meatitem['meats'][1])
        result.append(meatitem['meats'][2])

        predict.append(meatitem['count'][0])
        predict.append(meatitem['count'][1])
        predict.append(meatitem['count'][2])


        toppingitems = newdf['toppings'].value_counts().reset_index()

        result.append(toppingitems['toppings'][0])
        result.append(toppingitems['toppings'][1])
        result.append(toppingitems['toppings'][2])

        predict.append(toppingitems['count'][0])
        predict.append(toppingitems['count'][1])
        predict.append(toppingitems['count'][2])

        percents = []

        for elem in predict:
            percents.append((elem * 1.0)/size)
        
        val = [result, percents]

        # # newnewdf = newdf[newdf['meats'].apply(lambda meats: storage['meat'] in meats)]
        # print(newnewdf['meats'].value_counts().reset_index())

    return val