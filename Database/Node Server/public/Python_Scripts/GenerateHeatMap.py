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


csvPath = os.path.join(os.path.dirname(__file__), "../tmp/temp.csv")
data_raw = pd.read_csv(csvPath)

data_raw['dates'] = data_raw.Timestamp.apply(calculate_dates)
data_raw['times'] = data_raw.Timestamp.apply(calculate_times)
newdata = data_raw.drop('Timestamp', 1)


newdata["times"] = pd.Categorical(data_raw["times"], data_raw.times.unique())


datamatrix = data_raw.pivot("times", "dates", data_raw.columns.values[1])


sns.heatmap(datamatrix, xticklabels=50)
plt.subplots_adjust(bottom=0.23, right=1, top=0.88)
pdfPath = os.path.join(os.path.dirname(__file__), "../data/HeatMap/HeatMap.pdf")
plt.savefig(pdfPath)
# plt.show()
