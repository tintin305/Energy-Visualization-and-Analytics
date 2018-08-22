import pandas as pd
import numpy as np
import seaborn as sns
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl
import datetime
import socket

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

def generateDataOutage():
    csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/DataOutage/completeData.csv")
    try:
        data_raw = pd.read_csv(csvPath)
    except:
        print("error loading csv")
        sys.exit()

    data_raw['dates'] = data_raw.Timestamp.apply(calculate_dates)
    data_raw['times'] = data_raw.Timestamp.apply(calculate_times)
    newdata = data_raw.drop('Timestamp', 1)

    newdata["times"] = pd.Categorical(data_raw["times"], data_raw.times.unique())

    datamatrix = data_raw.pivot("times", "dates", data_raw.columns.values[1])

    # Set two colours for the heatmap
    cmap =  mpl.colors.ListedColormap(['#000000','#ffffff'])

    fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)
    # Set the colorbar to not show, and make the maximum value be 0 such 
    sns.heatmap(datamatrix, xticklabels=50, cmap=cmap,vmax=0, cbar=False)
    plt.subplots_adjust(bottom=0.23, right=1, top=0.88)

    ax.invert_yaxis()
    # directory = "../Data/DataOutage"
    # try:
    #         if not os.path.exists(directory):
    #             os.makedirs(directory)
    # except OSError:
    #     print ('Error: Creating directory. ' +  directory)
    # txtPath = os.path.join(os.path.dirname(__file__), "../../tmp/DataOutage")
    # os.chdir(txtPath)

    pdfPath = os.path.join(os.path.dirname(__file__), "../../tmp/DataOutage/DataOutage.pdf")
    plt.savefig(pdfPath)
    plt.close()

    return
