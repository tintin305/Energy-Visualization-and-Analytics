import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime
import time
# This is the Linux version of the formatter
# Doesn't work unless the r is there (not sure why, it didn't need it before)

rootFormattingFolder = '/home/username/Stitched'
rootFormattedFolder = '/home/username/OpenTSDB_Data'
try:
    os.makedirs(rootFormattedFolder)
except OSError:
    if not os.path.isdir(rootFormattedFolder):
        raise

os.chdir(rootFormattingFolder)


allFolders = []
allFolders = os.listdir()

for folders in allFolders:
    os.chdir(rootFormattingFolder + '/' + str(folders))

    allFiles = []
    allFiles = os.listdir()
    print(allFiles)
    s = pd.read_csv(allFiles[0], sep=',')
    # try:
    #     os.remove(allFiles)
    # except OSError:
    #     pass
    os.chdir(rootFormattedFolder)
    testTextFile = open(s.columns.values[1], 'a')

    # Metric for this data logger
    metric = s.columns.values[1]
    # print(metric)

    newline = ''
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

        # Remove trailing '.0' as this is not accepted by Opentsdb
        unixTimestamp = str(unixTimestamp)
        unixTimestamp = unixTimestamp[:-2]
        # print(unixTimestamp)
        test = s.iloc[cell,1]
        test2 = str(test)
        test3 = test2[:-2]
        # print(test3)
        # Magnitude Parameter
        magnitude = s.iloc[cell,1]

        # Additional Tags
        # Assigning the first tag to the name of the datalogger
        tagName = 'DataLoggerName=' + str(s.columns.values[1])

        # Assigning the second tag to the status of the datalogger on that event
        if (s.iloc[cell,1] == -1):
            tagDataOutage = 'DataOutage=True'
        else:
            tagDataOutage = 'DataOutage=False'
        # Exporting to a file which can be imported into the database




        testTextFile.write(newline + str(metric) + ' ' + unixTimestamp + ' ' + str(magnitude) + ' ' + tagName + ' ' + tagDataOutage)

        # Redefine \n so that you do not have a newline character at the end of the file created
        newline = '\n'

    testTextFile.close()
