# # from IPython.core.display import HTML
import pandas as pd
import numpy as np
import seaborn as sns
import sys
import os
import numpy as np
# import numpy.random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
import datetime
import matplotlib.dates as mdates

import sys 

# The /1000 is to counteract the extra zero's in the CSV. Dygraphs reads the csv using the three zero's so it is easy to remove them for this specific case.
def calculate_dates(unix):
    dateStamp = datetime.datetime.fromtimestamp(
        unix/1000
    ).strftime('%Y-%m-%d')
    return dateStamp
    
def calculate_times(unix):
    dateStamp = datetime.datetime.fromtimestamp(
        unix/1000
    ).strftime('%H:%M:%S')
    return dateStamp

csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/temp.csv")
try:
    data_raw = pd.read_csv(csvPath)
except:
    print("error loading csv")
    sys.exit()

data_raw['Date'] = data_raw.Timestamp.apply(calculate_dates)
data_raw['Time of day'] = data_raw.Timestamp.apply(calculate_times)
# newdata = data_raw.drop('Timestamp', 1)

# newdata["times"] = pd.Categorical(data_raw["times"], data_raw.times.unique())

datamatrix = data_raw.pivot("Time of day", "Date", data_raw.columns.values[1])

fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
sns.heatmap(datamatrix, xticklabels=50)
plt.subplots_adjust(bottom=0.23, right=1, top=0.88)

ax.set_title(data_raw.columns.values[1])
directory = "../data/HeatMap"
try:
        if not os.path.exists(directory):
            os.makedirs(directory)
except OSError:
    print ('Error: Creating directory. ' +  directory)
# print(os.path.isdir("../data/HeatMap"))
pdfPath = os.path.join(os.path.dirname(__file__), "../../data/HeatMap/HeatMap.pdf")
plt.savefig(pdfPath)
# plt.show()
