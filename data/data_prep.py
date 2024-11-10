import numpy as np
import pandas as pd
import csv

sides = {
    "No Side": 0.00,
    "Garlic Bread": 1.99,
    "Cheesy Garlic Bread": 1.99,
    "Cheesecake": 4.99,
    "Large Chocolate Chunk Cookie": 4.99,
    "Doritos": 1.99,
    "Cheetos": 1.99,
    "Lays Barbecue": 1.99,
    "Lays Classic": 1.99,
    "Cheesy Broccoli": 2.99,
    "Any Bag Of Chips": 1.99,
    "Side Mac": 8.99
}


drinks = {
    "No Drink": 0.00,
    "Water Bottle": 1.49,
    "Apple Juice": 2.49,
    "Coke": 1.99,
    "Dr. Pepper": 1.99,
    "Sprite": 1.99,
    "Diet Coke": 1.99,
    "Powerade - Blue Mountain Berry Blast": 1.99,
    "Minute Maid Lemonade": 1.99,
    "Water": 0.00,
    "Unlimited Fountain Drinks": 1.99,
    "Barq's Root Beer": 1.99,
    "Fanta Orange": 1.99,
    "": 0.00
}

menu = {
    "Buffalo Chicken": ["Cheddar", "Chicken", "Onions", "Buffalo"],
    "Texas BBQ": ["Pepper Jack", "Brisket", "Jalapenos", "BBQ"],
    "Garden Mac": ["Cheddar", "Broccoli", "Tomatoes", "Ranch"],
    "Chicken Alfredo": ["Alfredo", "Chicken", "Broccoli", "Pesto"],
    "Chicken Bacon Ranch": ["Cheddar", "Chicken", "Bacon", "Ranch"],
    "Classic Mac": ["Cheddar", "Breadcrumbs", "Garlic Parmesan"]
}

meats = {
    "No Meat": 0.00,
    "Grilled Chicken": 1.99,
    "Pulled Pork": 1.99,
    "Brisket": 1.99,
    "Bacon": 1.99,
    "Ham": 1.99
}

cheeses = ['Cheddar', 'Alfredo', 'Pepper Jack']
meat = ['Brisket', 'Chicken', 'Bacon']
sauce = ['Ranch', 'Garlic Parmesan', 'Buffalo']


FIELDS = ['orderID', 'time', 'item', 'noodles', 'added_mac', 'cheese', 'meats', 'toppings', 'drizzles', 'sides', 'drinks', 'utensils', 'cost']

with open ("data_full.csv", 'r') as file:
    header = file.readline()
    data_array = list(csv.reader(file, quotechar='"'))

data = data_array

print(data[1])

proccess = []

newOrder = False
index = 0
previous_meal = ""

data_len = len(data) -1
while index < data_len:
    previous_meal = data[index][3]
    storage = {key: np.nan for key in FIELDS}
    storage['orderID'] = data[index][4].strip()
    storage['time'] = data[index][0]
    storage['item'] = data[index][3]
    storage['cheese'] = []
    storage['meats'] = []
    storage['toppings'] = []
    storage['drizzles'] = []
    storage['sides'] = []
    storage['drinks'] = []
    storage['added_mac'] = []
    question = data[index][2]
    result = data[index][1]
    party = False
    if (data[index][3] == "Mac and Cheese" or data[index][3] == "Grilled Cheese Sandwich"):
        storage['cost'] = 8.99
    elif (data[index][3] == "Mac and Cheese Party Tray (Plus FREE Garlic Bread)"):
        party = True
        storage['cost'] = 39.99
        # info = data[index][1].split('(')
        # item_name = info[0].strip() + " Party Tray + FREE Garlic Bread"
        # print(info[0])
        # items = info[1][:-1].split(',')

        # for item in items:
        #     if (item in cheeses):
        #         storage['cheese'].append(item)
        #     elif item in meat:
        #         storage['meats'].append(item)
        #     elif item in sauce:
        #         storage['drizzles'].append(item)
        #     else:
        #         storage['toppings'].append(item)
        


        # print(info)

    elif (data[index][3] == "Garlic Bread (Party Size)"):
        storage['cost'] = 13.99
    # print(question)
    # print(result)
    if question == "Noods":
        # print("Noods set")
        storage['noodles'] = result
        # print(storage['noodles'])
    
    elif question == "Choose Your Cheese":
        storage['cheese'].append(result)

    elif question == "Choose Your Meats":
        storage['meats'].append(result)
        storage['cost'] += meats[result]

    elif question == "Choose Your Toppings":
        storage['toppings'].append(result)

    elif question == "Choose Your Drizzles":
        storage['drizzles'].append(result)
    
    elif question == "Choose Your Side":
        storage['sides'].append(result)
        storage['cost'] += sides[result]
    
    elif question == "Choose Your Drink":
        storage['drinks'].append(result)
        storage['cost'] += drinks[result]
    
    elif question == "Choose Your Melted Cheese":
        storage['cheese'].append(result)
    
    elif question == "Do you want Mac and Cheese added inside?":
        storage['added_mac'].append(result)
        storage['cost'] += 1.99
    else:
        # storage['note'] = result
        truei = True

    newOrder = False
    index += 1
    # print(len(data[index]))
    if (index == data_len):
        break
    while (not newOrder):
        # print(index, " are here")
        question = data[index][2]
        result = data[index][1]
        if question == "Choose Your Cheese":
            if (result != "MIX"):
                storage['cheese'].append(result)

        elif question == "Choose Your Meats":
            if (result != 'No Meat'):
                storage['meats'].append(result)
                storage['cost'] += meats[result]

        elif question == "Choose Your Toppings":
            if (result != 'No Toppings'):
                storage['toppings'].append(result)

        elif question == "Choose Your Drizzles":
            storage['drizzles'].append(result)
        
        elif question == "Choose Your Side":
            storage['sides'].append(result)
            storage['cost'] += sides[result]
        
        elif question == "Choose Your Drink":
            storage['drinks'].append(result)
            storage['cost'] += drinks[result]
        
        elif question == "Choose Your Melted Cheese":
            storage['cheese'].append(result)
        
        elif question == "Do you want Mac and Cheese added inside?":
            if (result != "No Mac"):
                storage['added_mac'].append(result)
                storage['cost'] += 1.99
        elif question == '':
            storage['note'] = result
        elif question == 'Mix Bases':
            storage['cheese'].append(result)


        if (index == data_len):
            break
        if data[index][2] == "Noods" or data[index][3] == "Choose Melted Cheese":
            newOrder = True
        elif data[index][3] != previous_meal:
            if (data[index][3] == 'MIX'):
                index += 1
                continue
            newOrder = True
        else:
            index += 1
    if (len(storage['added_mac']) == 0):
        if (storage['item'] == 'Grilled Cheese Sandwich'):
            storage['added_mac'].append('No Mac')
        else:
            storage['added_mac'].append('N/A')
    proccess.append(storage)

daf = pd.DataFrame(proccess)
print(len(daf))
print(daf.head())
daf.dropna(subset=['time'], inplace=True)
print(len(daf))
daf.to_csv('data_processed.csv', index = False)

