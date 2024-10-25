import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Data used within the matplot lib session

# Can be distributed in the session to save anyone having to type out reems of data

# -----------------------------------------------------------------------------------
#                                  Bar Chart Data
# -----------------------------------------------------------------------------------

# df = pd.DataFrame({
#     "Locations" : [
#     "Twitter",
#     "Facebook",
#     "LinkedIn",
#     "Indeed",
#     "Instagram"
# ],
#     "Responses" : [3,11,16,13,2],
# })

# df = df. sort_values("Responses")
# bar_colours = ['red' if x == df ['Responses'].max( ) else 'blue' for x in df ['Responses']]
# plt.bar("Locations", "Responses", data=df, color = bar_colours )

# # title of the graph
# plt.title("Job postings" )
# # name of x axis
# plt.xlabel("Locations" )
# # name of y axis
# plt.ylabel("Responses")

# plt.show( )
# -----------------------------------------------------------------------------------
#                                  Stacked Bar Chart Data
# -----------------------------------------------------------------------------------

# df = pd.DataFrame({
#     "Engineering":[56,13,1],
#     "Computer Science":[77,23,4],
#     "English Lit":[35,48,9],
#     "Economics": [65,45,19]
# }, index=["Male", "Female", "Non-Binary"])

# # to transpose the dataframe, making the index the columns, and the columns the index!
# df = df.T
# # Pandas has the df.plot() method which is a wrapper for matplotlib.
# my_plot = df.plot.barh(stacked=True, colormap="plasma")

# plt.show()
# -----------------------------------------------------------------------------------
#                                  Pie Chart Data
# -----------------------------------------------------------------------------------

# roles = [    
#     "Front-end", 
#     "Back-end",
#     "Full-stack",
#     "DevOps"
#     ]

# employees = [52,36,28,11]

# plt.pie(employees, labels=roles, autopct="%.1f%%",explode=[0.2,0.2,0.1,0.1])

# plt.show( )
# -----------------------------------------------------------------------------------
#                                  Scatter
# -----------------------------------------------------------------------------------

# number_of_placements=list(range(1,11))
# responses_received = [14, 21, 34, 36, 45, 51, 54, 63, 78, 92]

# number_of_placements=np.array(range(1,11))
# responses_received = np.array( [14, 21, 34, 36, 45, 51, 54, 63, 78, 92])

# a,b = np.polyfit(number_of_placements, responses_received, 1)
# plt.plot(number_of_placements,a*number_of_placements+b)

# plt.scatter(number_of_placements, responses_received)
# plt.xlabel("Number of Places Advertised")
# plt.ylabel("Responses Received" )
# plt. title("Job Posting - Junior Dev Role" )

# plt.show( )

# -----------------------------------------------------------------------------------
#                             Box Plots and Histogram Data
# -----------------------------------------------------------------------------------

dev_ages=[
        45, 23, 57, 27, 37, 39, 61, 48, 23, 27, 
        59, 60, 28, 41, 25, 39, 22, 46, 48, 52, 
        38, 41, 52, 30, 46, 62, 25, 34, 52, 35, 
        48, 43, 21, 40, 22, 22, 57, 25, 21, 30, 
        55, 50, 54, 30, 43, 40, 53, 46, 36, 61, 
        35, 39, 40, 31, 29, 65, 28, 57, 39, 36, 
        20, 49, 42, 29, 62, 52, 29, 57, 39, 32, 92
        ]

df = pd.DataFrame({"Dev Ages" : dev_ages})
# plt.boxplot(dev_ages, vert=0)
plt.boxplot(df, vert=0)
plt.xlabel("Age")
plt. title("Dev Ages" )

# plt.hist(dev_ages, edgecolor="black",bins=[20,25,30,35,40,45,50,55,60,65])
# plt.hist(df, edgecolor="black",bins=[20,25,30,35,40,45,50,55,60,65])

# Specifying the file name # and file extension.
# If you want to save a # plot, you must do this # before plt.show()
plt.savefig("Dev_age_plot.png")

plt.show( )