import matplotlib.pyplot as plt

days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

YouTube = [2,1,3,6,3]
Twitter = [1,1,0,0,2]
WhatsApp = [3,1,0,2,1]
Raid = [0,4,2,3,3]
TikTok = [3,0,1,0,2]

# title of the graph
plt.title("Screen Time per day" )
# name of x axis
plt.xlabel("Days of the week" )
# name of y axis
plt.ylabel("Hours")
# set the limts of the axsis
plt.ylim(bottom=0, top=7)
# x axis first then y axis
plt.plot(days, YouTube, label = "YouTube", marker = "*", c = "Chartreuse" )
plt.plot(days, Twitter, label = "Twitter", linestyle = "dashed", marker = "o", c = "BlueViolet" )
plt.plot(days, WhatsApp, label = "WhatsApp", linestyle = "dotted", marker = "D", c = "#00008B" )
plt.plot(days, Raid, label = "Raid", linestyle = "dashdot", marker = "x", c = "#8B0000" )
plt.plot(days, TikTok, label = "TikTok", linestyle = "dashdot", marker = "+", c = "#FFA500" )

# takes the legends from label set in plt.plot
plt.legend()

plt.show()