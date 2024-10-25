import pandas as pd
import numpy as np

df = pd.read_excel("first_hour_sales.xlsx")

df = df. set_index("Transaction ID")

# df = df.drop("Till ID", axis=1)
# OR
df = df.drop(columns=["Till ID"])

df = df.dropna(how="any" )
# The .drop_na() method allows us to drop NULL values like NaN. 
# It can be used to get rid of many rows quickly.
# The how argument specifies how strict is should be. 
# Do all the values in the row need to be NaN, or just any value?

# print(df[df.duplicated()])

df = df.drop_duplicates()

# df = df.drop([15.0])
# removes row with 600

df.at[15.0, "Cost"] = 6.00
# changed outlier of 600 to 6 from menu prices

def float_to_time(time_record):
    time_record= str(time_record)
    hours, minutes = time_record.split(".")
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp

df["Time"] = df["Time"].apply(float_to_time)

df["Time"] = pd.to_datetime(df["Time"])

def split_basket(basket_item):
    items = basket_item.split(",")
    stripped_items = [item.strip() for item in items]

    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)

exploded_data = df.explode("Basket", ignore_index=False)

# print(exploded_data["Basket"] )

print(df)
# print(df["Basket"])
# print(df.describe)
# print(df.info())

# Activity 1
# • The average price of an item 
products = {
    'Tea' : 1.00,
    'Americano' : 1.70,
    'Latte' : 1.90,
    'Cappuccino' : 1.90,
    'Mocha' : 2.00,
    'Hot Chocolate' : 2.20,
    'Croissant' : 1.50,
    'Muffin' : 2.10,
    'Toast' : 1.00,
    'Panini' : 2.90,
    'Buttered Roll' : 0.70,
    'Stroopwafel': 0.50,
    }

average_price = sum(products.values()) / len(products)
# print(f"The average price of an item is: {average_price:.2f}")
# print(average_price)

# # • The average basket price
# print(df["Cost"].mean())
# # • The maximum spend in one transaction
# print(df["Cost"].max())
# # • The minimum spend in one transaction
# print(df["Cost"].min())
# # • The most common spend amount
# print(df["Cost"].mode())
# # • The most common payment type
# print(df["Payment Method"].mode())


# Activity 2
# Download cleaning_activity.xlsxfrom Teams.
# Ensure this data is clean and accurate.

df1 = pd.read_excel("cleaning_activity.xlsx")

# print(df1)
# print(df1.describe())
# print(df1.info())

df1 = df1. set_index("Transaction ID")

df1 = df1.drop(columns=["Till ID","Transaction Type","Unnamed: 0"])

df1 = df1.dropna(how="any")

df1 = df1.drop_duplicates()

df1.at[56.0, "Cost"] = 6.00

df1 = df1.drop(index=60)

df1['Basket'] = df1['Basket'].str.replace("'", "")
df1['Basket'] = df1['Basket'].str.replace("[", "")
df1['Basket'] = df1['Basket'].str.replace("]", "")

df1["Basket"] = df1["Basket"].apply(split_basket)

exploded_data1 = df1.explode("Basket", ignore_index=False)

# print(exploded_data1["Basket"] )

print(df1)
#print(df1["Basket"])

#print(df1.info("Basket"))