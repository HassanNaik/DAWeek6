import pandas as pd
import numpy as np
from  ydata_profiling import ProfileReport

df = pd.read_excel("results2024-10-24-1512.xlsx")
# reads excel file

df = df. set_index("Unnamed: 0")
# Sets index
df = df.drop(columns=["Date-time"])
# Removes column 

# print(df)
# prints data frame with index and column removed

# print(df.describe())
# returns 5 figure summary

# print(df.info())
# The number of entries (rows) and Each column's name and data type

# print(f"{df['Download (Mb/s)'].mean():.2f} mean downlad")
# prints mean download speed


# print(f"{df['Download (Mb/s)'].median():.2f} median download")
# prints median download speed

# print(f"{df['Upload (Mb/s)'].mean():.2f} mean upload")
# prints mean upload speed

# print(f"{df['Upload (Mb/s)'].median():.2f} median upload")
# prints median upload speed

 
# Mean of the download speeds
# avg = df["Download (Mb/s)"].mean()
# print(f"The mean of download speed {avg}")
 
# # Median of the download speeds
# med = df["Download (Mb/s)"].median()
# print(f"The median of download speed {med}")
 
# # Sort by fastest upload
# print(df.sort_values(by=["Upload (Mb/s)"], ascending =False))
 
# # Sort by slowest upload
# print(df.sort_values(by=["Upload (Mb/s)"], ascending =True))
 
# Return download speeds which are faster than the mean
# def fast():
#     if "Download (Mb/s)" <= avg:

# df = df.sort_values(by='Upload (Mb/s)', ascending=True)
# print(df)
# df = df.sort_values(by='Upload (Mb/s)', ascending=False)
# print(df)


# # Calculate the mean download speed
# mean_download_speed = df['Download (Mb/s)'].mean()

# # Filter out download speeds greater than the mean
# df_faster_than_mean = df[df['Download (Mb/s)'] > mean_download_speed]

# print(df_faster_than_mean)

x = df[df['Download (Mb/s)'] >df['Download (Mb/s)'].mean()]

print(x)
# prints download speeds greater than mean
   
# print(f"{df['Download (Mb/s)'].min():.2f} slowest download")
# prints slowest download speed
# print(f"{df['Download (Mb/s)'].max():.2f} fastest download")
# prints fastest download speed
# print(f"{df['Upload (Mb/s)'].min():.2f} slowest upload")
# prints slowest upload speed
# print(f"{df['Upload (Mb/s)'].max():.2f} fastest upload")
# prints fastest upload speed

# national average download speed in the UK is 73.21 Mbps, 
# while the average upload speed is 18.4 Mbps

# a = 73.21
# float(b) = 18.40

df1 = pd.read_excel("group_results.xlsx")

# df = df. set_index("Internet Service Provider")

df1 = df1.drop(columns=["Package (if known)"])
# removes as was mainly empty

df1 = df1.dropna(how="any" )
# remove any empty rows

# print(f"{df1['Mean Download'].mean():.2f} mean download of group")
# prints mean of group download
# print(f"{df1['Mean Upload'].mean():.2f} mean upload of group")
# prints mean of groups upload
# print(f"{df1['Mean Download'].min():.2f} slowest download of group")
# prints slowest download speed
# print(f"{df1['Mean Download'].max():.2f} fastest download of group")
# prints fastest download speed
# print(f"{df1['Mean Upload'].min():.2f} slowest upload of group")
# prints slowest upload speed
# print(f"{df1['Mean Upload'].max():.2f} fastest upload of group")
# prints fastest upload speed

# profile = ProfileReport(df1, title="Group Speed")

# profile.to_file('gsr.html')