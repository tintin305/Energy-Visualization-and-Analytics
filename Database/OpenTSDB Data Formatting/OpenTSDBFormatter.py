import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime
import time
import gzip
import shutil
# This is the windows version of the formatter
# Doesn't work unless the r is there (not sure why, it didn't need it before)

rootFormattingFolder = 'C:\Project\Data\Stitched'
rootFormattedFolder = 'C:\Project\Data\OpenTSDB'
try:
    os.makedirs(rootFormattedFolder)
except OSError:
    if not os.path.isdir(rootFormattedFolder):
        raise

os.chdir(rootFormattingFolder)


allFolders = []
allFolders = os.listdir()

for folders in allFolders:
    os.chdir(rootFormattingFolder + '\\' + str(folders))

    allFiles = []
    allFiles = os.listdir()
    print(allFiles)
    s = pd.read_csv(allFiles[0], sep=',')
    # try:
    #     os.remove(allFiles)
    # except OSError:
    #     pass
    os.chdir(rootFormattedFolder)
    fileName = s.columns.values[1]
    testTextFile = open(str(fileName), 'w')

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



         # Additional Tags
        # Assigning the first tag to the name of the datalogger
        tagName = 'DataLoggerName=' + str(s.columns.values[1])

        # Assigning the second tag to the status of the datalogger on that event
        if (s.iloc[cell,1] == -1):
            tagDataOutage = 'DataOutage=True'
            s.iloc[cell,1] = 0
        else:
            tagDataOutage = 'DataOutage=False'
        # Exporting to a file which can be imported into the database
        
         # Magnitude Parameter (defined now that the -1 values have been managed)       
        magnitude = s.iloc[cell,1]


        tempText = str(s.columns.values[1])
        # Assigning tags which relate to the campus
        if ((tempText.find("_13_Jubilee_Road_")) is not -1):
            tagLocation = "Campus=13_Jubilee_Road"

        elif ((tempText.find("_Campus_Lodge_")) is not -1):
            tagLocation = "Campus=Campus_Lodge"
     
        elif ((tempText.find("_College_House_")) is not -1):
            tagLocation = "Campus=College_House"
     
        elif ((tempText.find("_EC_")) is not -1):
            tagLocation = "Campus=East_Campus"
     
        elif ((tempText.find("_Essellen_")) is not -1):
            tagLocation = "Campus=Essellen"
   
        elif ((tempText.find("_Graduate_Lodge_")) is not -1):
            tagLocation = "Campus=Graduate_Lodge"
    
        elif ((tempText.find("_IBM_")) is not -1):
            tagLocation = "Campus=IBM"
    
        elif ((tempText.find("_Ithemba_Labs_")) is not -1):
            tagLocation = "Campus=Ithemba_Labs"
   
        elif  ((tempText.find("_Knockando_")) is not -1):
            tagLocation = "Campus=Knockando"
     
        elif  ((tempText.find("_Medical_School_")) is not -1):
            tagLocation = "Campus=Medical_School"
     
        elif  ((tempText.find("_PEC_")) is not -1):
            tagLocation = "Campus=Parktown_Education_Campus"
    
        elif  ((tempText.find("_Philip_V_Tobias_")) is not -1):
            tagLocation = "Campus=Philip_V_Tobias"
    
        elif  ((tempText.find("_Science_Park_")) is not -1):
            tagLocation = "Campus=Science_Park"
    
        elif  ((tempText.find("South_Court_")) is not -1):
            tagLocation = "Campus=South_Court"
  
        elif  ((tempText.find("_Junction_")) is not -1):
            tagLocation = "Campus=Junction"
    
        elif  ((tempText.find("_Tshimologong_")) is not -1):
            tagLocation = "Campus=Tshimologong"
    
        elif  ((tempText.find("_University_Corner_")) is not -1):
            tagLocation = "Campus=University_Corner"
     
        elif  ((tempText.find("WBS_Albert_Wessels_Building_")) is not -1):
            tagLocation = "Campus=WBS_Albert_Wessels_Building"
   
        elif  ((tempText.find("_WBS_Albert_Wessels_gen_300_kVA_")) is not -1):
            tagLocation = "Campus=WBS_Albert_Wessels_gen_300_kVA"

        elif  ((tempText.find("_WBS_Donald_Gordon_")) is not -1):
            tagLocation = "Campus=WBS_Donald_Gordon"

        elif  ((tempText.find("_WBS_")) is not -1):
            tagLocation = "Campus=WBS"

        elif  ((tempText.find("_WC_")) is not -1):
            tagLocation = "Campus=West_Campus"
        
        else:
            tagLocation = "Campus=NA"


        testTextFile.write(newline + str(metric) + ' ' + unixTimestamp + ' ' + str(magnitude) + ' ' + tagName + ' ' + tagDataOutage + ' ' + tagLocation)

        # Redefine \n so that you do not have a newline character at the end of the file created
        newline = '\n'



    testTextFile.close()
    fileNameZipped = fileName + '.gz'
    with open(fileName, 'rb') as f_in:
        with gzip.open(fileNameZipped, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)