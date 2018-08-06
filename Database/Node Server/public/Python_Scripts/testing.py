# # from IPython.core.display import HTML
import pandas as pd
import numpy as np
import seaborn as sns

import numpy as np
# import numpy.random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
import datetime
import matplotlib.dates as mdates

def calculate_dates(unix):
    dateStamp = datetime.datetime.fromtimestamp(
        unix
    ).strftime('%Y-%m-%d')
    return dateStamp
    
def calculate_times(unix):
    dateStamp = datetime.datetime.fromtimestamp(
        unix
    ).strftime('%H:%M:%S')
    return dateStamp



data_raw = pd.read_csv("temp.csv")
# data_raw['Timestamp'] = pd.to_datetime(data_raw['Timestamp'], unit='s')

data_raw['dates'] = data_raw.Timestamp.apply(calculate_dates)
data_raw['times'] = data_raw.Timestamp.apply(calculate_times)
newdata = data_raw.drop('Timestamp', 1)


# print(newdata)


# flights_raw = pd.read_csv('flights.csv')
# flights_raw["month"] = pd.Categorical(flights_raw["month"], flights_raw.month.unique())
newdata["times"] = pd.Categorical(data_raw["times"], data_raw.times.unique())
# flights_raw.head()
# print(newdata.head())

# flight_matrix = flights_raw.pivot("month", "year", "passengers")
datamatrix = data_raw.pivot("times", "dates", data_raw.columns.values[1])
# flight_rows = flights_raw
# print(flight_matrix)

# print(datamatrix)
# fig, ax = plt.subplots(1,1, figsize=(12,12))
# heatplot = ax.imshow(datamatrix, cmap='BuPu')
# # ax.set_xticklabels(datamatrix.columns)
# # ax.set_yticklabels(datamatrix.index)
# tickLabelsX = ['00:00:00', " ", '01:00:00'," ",  '02:00:00', " ",
#        '03:00:00', " ",'04:00:00', " ",'05:00:00', " ",
#        '06:00:00'," ", '07:00:00', " ", '08:00:00', " ",
#        '09:00:00'," ",  '10:00:00'," ", '11:00:00'," ",
#        '12:00:00', " ", '13:00:00'," ", '14:00:00'," ",
#        '15:00:00'," ", '16:00:00', " ",'17:00:00', " ",
#        '18:00:00', " ", '19:00:00'," ",  '20:00:00', " ",
#        '21:00:00'," ",  '22:00:00'," ", '23:00:00'," "]
# ax.set_yticklabels(tickLabelsX)
# # print(enumerate(ax.yaxis.get_ticklabels()))

# # for label in ax.set_yticklabels(datamatrix.index)[::2]:
# #     label.set_visible(False)
# # plt.setp(ax.set_yticklabels(datamatrix.index)[::2], visible=False)
# # for index, label in enumerate(ax.yaxis.get_ticklabels()):
# #     print(index)
# #     print(label)
# #     if index % 2 != 0:
# #         label.set_visible(False)
# # ymin, ymax = ax.get_ylim()
# # ax.set_yticks(np.round(np.linspace(ymin, ymax, 1), 2))
# # start, end = ax.get_xlim()
# # ax.xaxis.set_ticks(np.arange(start, end, 2))

# tick_spacing = 1
# # ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

# # ax.xaxis.set_major_locator(ticker.LinearLocator(20))

# # ax.xaxis.set_major_locator(ticker.AutoLocator())

# years = mdates.YearLocator()   # every year
# months = mdates.MonthLocator()  # every month
# yearsFmt = mdates.DateFormatter('%Y')


# ax.xaxis.set_major_locator(years)
# ax.xaxis.set_major_formatter(yearsFmt)
# ax.xaxis.set_minor_locator(months)

# datemin = datetime.date(data_raw.dates.min().year, 1, 1)
# datemax = datetime.date(data_raw.dates.max().year + 1, 1, 1)
# ax.set_xlim(datemin, datemax)

# # ax.set_title("Heatmap of Flight Density from 1949 to 1961")
# # ax.set_xlabel('Year')
# # ax.set_ylabel('Month')
# plt.savefig('books_read.svg')
# fig.autofmt_xdate()
# plt.show()

# fig = plt.figure(figsize=(12,12))

sns.heatmap(datamatrix, xticklabels=50)
plt.subplots_adjust(bottom=0.23, right=1, top=0.88)
plt.savefig('books_read.svg')
plt.show()
