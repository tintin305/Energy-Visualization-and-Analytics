import pandas as pd
import numpy as np
import seaborn as sns
import sys
import os
import numpy as np
import matplotlib
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

def generateHeatMap(cmapChoice):
    csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/HeatMap/temp.csv")
    try:
        data_raw = pd.read_csv(csvPath)
    except:
        print("error loading csv")
        sys.exit()

    data_raw['Date'] = data_raw.Timestamp.apply(calculate_dates)
    data_raw['Time of Day'] = data_raw.Timestamp.apply(calculate_times)

    datamatrix = data_raw.pivot("Time of Day", "Date", data_raw.columns.values[1])

    fig, ax = plt.subplots()
    fig.set_size_inches(20, 8.27)
    if cmapChoice == "default":
        sns.heatmap(datamatrix, xticklabels=50, linewidths=0, linecolor='black')
    else:
        sns.heatmap(datamatrix, xticklabels=50, linewidths=0, linecolor='black', cmap=cmapChoice)

    plt.subplots_adjust(bottom=0.23, right=1, top=0.88)

    ax.set_title(data_raw.columns.values[1])
    ax.invert_yaxis()

    pdfPath = os.path.join(os.path.dirname(__file__), "../../tmp/HeatMap/HeatMap.pdf")
    plt.savefig(pdfPath)
    plt.close()
    return