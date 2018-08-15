import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import matplotlib.dates as mdates
import os
import sys

def getDateStr(unix):
    dateStamp = datetime.datetime.fromtimestamp(
        unix/1000
    ).strftime('%Y-%m-%d')
    return dateStamp
    

def calculate_dates(unix):
    dateStamp = np.floor(unix/86400000)-15705
    return dateStamp
    
def calculate_times(unix):
    dateStamp = (unix%86400000)/1800000
    return dateStamp


def generateThreeDimensionalHeatMap():
    csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/temp.csv")
    try:
        data_raw = pd.read_csv(csvPath)
    except:
        print("error loading csv")
        sys.exit()


    data_raw['dates'] = data_raw.Timestamp.apply(calculate_dates)
    data_raw['times'] = data_raw.Timestamp.apply(calculate_times)
    data_raw['DateStrings'] = data_raw.Timestamp.apply(getDateStr)

    headings = pd.DataFrame(np.zeros((len(data_raw), 1)))
    headings.columns=["Dates"]

    HeadingSpace = np.ceil(len(data_raw)/5)
    # Create headings with spaces for the date axis
    for i in range(0, len(headings)):
        if i%HeadingSpace == 0:
            headings.Dates[i] = data_raw.DateStrings[i]
        else:
            headings.Dates[i] = ""


    # Create headings with spaces for the time axis
    times = [
    "22:00"," "," "," ","00:00"," "," "," ","02:00"," "," "," ","04:00"," "," "," ","06:00"," "," "," ","08:00"," "," "," ","10:00"," "," "," ","12:00"," "," "," ","14:00"," "," "," ","16:00"," "," "," ","18:00"," "," "," ","20:00"," "," "," "]


    data_raw = data_raw.drop('Timestamp', 1)
    # print(data_raw.head())
    data_raw.columns=["Z","x","y", "DateStrings"]


    # print(data_raw.head())

    fig = plt.figure()

    # fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)
    ax = fig.gca(projection='3d')
    plt.xticks(data_raw["x"], headings["Dates"])

    plt.yticks(data_raw["y"], times)
    ax.plot_trisurf(data_raw['x'], data_raw['y'], data_raw['Z'], linewidth=0.2, cmap = "BuPu")


    directory = "../../Data/ThreeDim"
    try:
            if not os.path.exists(directory):
                os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
    # print(os.path.isdir("../data/HeatMap"))
    pdfPath = os.path.join(os.path.dirname(__file__), "../../Data/ThreeDim/ThreeDim.pdf")
    plt.savefig(pdfPath)
    # plt.show()
