import pandas as pd

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

df = df.drop_duplicates()

df = df.drop([15.0])
# removes row with 600

print(df)
# print(df.describe)
# print(df.info())

# print(df[df.duplicated()])

