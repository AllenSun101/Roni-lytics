from datetime import timedelta
import pandas as pd

def get_aggie_meal(df, storage):
    # dataframe and a storage dictionary that has other things
    if (storage['item']):
        newdf = df[df['item'] == storage['item']]
        cheeseitem = newdf['cheese'].value_counts().reset_index()
        size = len(newdf)

        result = [cheeseitem['cheese'][0], cheeseitem['cheese'][1], cheeseitem['cheese'][2]]

        meatitem = newdf['meats'].value_counts().reset_index()
        
        result.append(meatitem['meats'][0])
        result.append(meatitem['meats'][1])
        result.append(meatitem['meats'][2])


        toppingitems = newdf['toppings'].value_counts().reset_index()

        result.append(toppingitems['toppings'][0])
        result.append(toppingitems['toppings'][1])
        result.append(toppingitems['toppings'][2])

        percents = []

        for elem in result:
            percents.append(elem/size)
        
        val = [result, percents]

        # # newnewdf = newdf[newdf['meats'].apply(lambda meats: storage['meat'] in meats)]
        # print(newnewdf['meats'].value_counts().reset_index())

    return val
