import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022, 2023]
python_position = [7, 4, 4, 3, 4, 3]
js_position = [1, 1, 1, 1, 1, 1]
sql_position = [4,3,3,4,3,4]
typescript_position = [12,10,9,7,5,5]

# name of graph
plt.title("Most-Wanted Language Ranking" )
# name of x axis
plt.xlabel("Year" )
# name of y axis
plt.ylabel("Position")
# set the limts of the axsis
plt.ylim(bottom=15, top=0)
# x axis first then y axis
plt.plot(years, python_position, label = "Python")
plt.plot(years, typescript_position, label = "Typescript", linestyle = "dashed")
plt.plot(years, js_position, label = "JavaScript", linestyle = "dotted")
plt.plot(years, sql_position, label = "SQL", linestyle = "dashdot")


# inserts legend in order ploted
# plt. legend([
#     "Python",
#     "JavaScript",
#     "SQL",
#     "Typescript"
# ])

# takes the legends from label set in plt.plot
plt.legend()

plt.show()