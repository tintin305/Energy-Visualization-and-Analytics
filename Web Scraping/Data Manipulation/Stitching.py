import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import errno
import datetime
import sys

# Directory for where to find the separated csv files
rootSeparatedFolder = 'C:\Project\Data\Separated'

# Create the folder for the stitched together documents (if it doesn't already exist)
rootStitchingFolder = 'C:\Project\Data\Stitched'
try:
    os.makedirs(rootStitchingFolder)
except OSError:
    if not os.path.isdir(rootStitchingFolder):
        raise    

# Makes a list of all the folders in the cwd
folderNames = []

try:
    os.chdir(rootSeparatedFolder) # Change to seperated directory
except:
    sys.exit("Folder with seperated data does not exist") # Exit program if input data folder is not found

folderNames = os.listdir()

# Loop through all of the folders, this will work so that the work is done in each of the folders
for folders in folderNames:
    loggerFolder = str(rootSeparatedFolder) + '\\' + str(folders)
    os.chdir(loggerFolder)

    # Get a list for the files in the cwd
    allFiles = os.listdir()
    files = []
    for csvFiles in allFiles:
        if csvFiles.endswith(".csv"):
            files.append(csvFiles)
    # Now do the operations on the files

    mergedFrames = pd.DataFrame()
    list_ = []
    for file_ in files:
        df = pd.read_csv(file_, index_col=None, header=0)
        list_.append(df)
    frame = pd.concat(list_)

    fileName = frame.columns.values[1]
    dataLoggerFolder = str(rootStitchingFolder) + '\\' + str(fileName)

    try:
        os.makedirs(dataLoggerFolder)
    except OSError:
        if not os.path.isdir(dataLoggerFolder):
            raise    

    os.chdir(dataLoggerFolder)
    frame.to_csv(fileName+'.csv', sep=",", encoding='utf-8', index=False)
    
    
    
        # At this stage, it may be useful to convert the date to a date time object, or a UNIX goody
        # One can do this: http://pbpython.com/excel-file-combine.html
