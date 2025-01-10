import pandas as pd
import matplotlib.pyplot as plt

# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]
# }
#
# myvar = pd.DataFrame(mydataset)
# print(myvar, "\n")
#
# print(myvar)
# print(pd.__version__)
#
# a = [1, 7, 'sadf']
# myvar = pd.Series(a, index=["x", "y", "z"])

# print(myvar)
# print(myvar['z'])

# calories = {"day1": 420, "day2": 380, "day3": 390}
#
# myvar = pd.Series(calories, index=["day1", "day2"])
#
# print(myvar)
# print(myvar[1])

# calories = {"day1": [420], "day2": [380], "day3": [390]}
# calories1 = {"day1": 420, "day2": 380, "day3": 390}
# print(pd.Series(calories1, index=["day1", "day3"]))

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df.loc[["day1", "day2"]])  # stands for locate???

# read in csv files
# df = pd.read_csv('data.csv')
# print(df.to_string())
# displays the max number of rows for the dataframe, can be modified
# can also set this to an integer to display more rows
# print(pd.options.display.max_rows)


# read JSON
# df = pd.read_json('data.json')
# print(df.to_string())


# analyzing dataframes
# df = pd.read_csv('data.csv')
# print(df.head(10))
# print(df.tail(10))
# print(df.info())


# DATA CLEANING!!!🗣️🔥
# drop empty cells
# df = pd.read_csv('data.csv')
# df.dropna(inplace = True)
# print(df.to_string())


# replace empty cells
# df = pd.read_csv('data.csv')
#
# df.fillna(130, inplace=True)
#
# print(df.to_string())


# replace only specified columns
# df = pd.read_csv('data.csv')
# df["Calories"].fillna(130, inplace=True)
# print(df.to_string())


# replace with MEAN, MEDIAN, OR MODE
# df = pd.read_csv('data.csv')
# calorie_mean = df["Calories"].mean()
# all_mean = df.mean()
# print(all_mean)
# print(calorie_mean)
#
# df["Calories"].fillna(calorie_mean, inplace=True)
# print(df.to_string())
#
# calorie_mode = df["Calories"].mode()
# print(calorie_mode[0])


# find and replace using loc
# file = pd.read_csv('data.csv')
# df = pd.DataFrame(file)
# for i in df.index:
#     # df.loc[df['Duration'] == 45, 'Duration'] = 450
#     if df.loc[i, 'Duration'] == 45:
#         df.loc[i, 'Duration'] = 450
#
# print(df.to_string())


# finding relationships using corr()
# file = pd.read_csv('data.csv')
# df = pd.DataFrame(file)
#
# print(df.to_string())
# print(df.corr())


# plotting in pandas using plot()
# df = pd.read_csv('data.csv')


# df.plot()
# plt.show()

# plotting a scatter plot
# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# plt.show()

# plotting a histogram
# df['Duration'].plot(kind = 'hist')
# plt.show()

# left off on https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp



# file = pd.read_csv('data.csv')
# df = pd.DataFrame(file)
#
# df.shape()

a, b = 4, 5
print("value assigned to a")
print(a)
print("value assigned to b")
print(b)
