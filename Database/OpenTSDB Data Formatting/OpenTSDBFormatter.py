import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime
import time

# directory = 'C:\Users\Tristan\Desktop'
# folder = 'WITS 3 Jubilee Road_kVarh'
# mainFolder = directory + '\\' + folder

# Doesn't work unless the r is there (not sure why, it didn't need it before)
os.chdir(r'C:\Users\Tristan\Desktop\WITS 3 Jubilee Road_kVarh')

allFiles = []
allFiles = os.listdir()

s = pd.read_csv('WITS EC Bernard Price Sub Total_kWh.csv', sep=',')
try:
    os.remove(r'EC')
except OSError:
    pass
# os.remove(r'EC.txt')
testTextFile = open('EC', 'a')

# Metric for this data logger
metric = s.columns.values[1]
# print(metric)


for cell in range(2,(s.shape[0])):
    # Unix Epoch Timestamp
    cellSelected = s.iloc[cell,0]
    year = cellSelected[0:4]
    month = cellSelected[5:7]
    day = cellSelected[8:10]
    hour = cellSelected[11:13]
    minute = cellSelected[14:16]
    timeToDatetime = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))    
    unixTimestamp = time.mktime(timeToDatetime.timetuple())

    # Magnitude Parameter
    magnitude = s.iloc[cell,1]

    # Additional Tags
    tag = 'DataLoggerName=WITS.EC.Bernard.Price.Sub.Total.kWh'

    # Exporting to a file which can be imported into the database
    testTextFile.write(str(metric) + ' ' + str(unixTimestamp) + ' ' + str(magnitude) + ' ' + tag + '\n')


testTextFile.close()




