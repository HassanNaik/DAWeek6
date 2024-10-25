import pandas as pd
import numpy as np
from  ydata_profiling import ProfileReport

df = pd.read_excel("results2024-10-24-1512.xlsx")

df = df. set_index("Unnamed: 0")

# print(f"{df['Download (Mb/s)'].mean():.2f} mean downlad")
# print(f"{df['Download (Mb/s)'].median():.2f} median download")
# print(f"{df['Upload (Mb/s)'].mean():.2f} mean upload")
# print(f"{df['Upload (Mb/s)'].median():.2f} median upload")
 
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

# print(df)
# print(df[])
# print(df.describe)
# print(df.info())

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
   

# print(f"{df['Download (Mb/s)'].min():.2f} slowest downlad")
# print(f"{df['Download (Mb/s)'].max():.2f} fastest download")
# print(f"{df['Upload (Mb/s)'].min():.2f} slowest upload")
# print(f"{df['Upload (Mb/s)'].max():.2f} fastest upload")

# national average download speed in the UK is 73.21 Mbps, 
# while the average upload speed is 18.4 Mbps

a = 73.21
# float(b) = 18.40

df1 = pd.read_excel("group_results.xlsx")

# df = df. set_index("Internet Service Provider")

df1 = df1.drop(columns=["Package (if known)"])

df1 = df1.dropna(how="any" )

print(f"{df1['Mean Download'].mean():.2f} mean downlad of group")

print(f"{df1['Mean Upload'].mean():.2f} mean upload of group")

# print(df1)
# print(df1[])
# print(df1.describe)
# print(df1.info())

profile = ProfileReport(df1, title="Group Speed")

profile.to_file('gsr.html')