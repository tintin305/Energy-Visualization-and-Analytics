import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import errno
import datetime
import sys

def makeDirectoryFolder(newDir):
    try:
        os.makedirs(newDir)
    except OSError:
        if not os.path.isdir(newDir):
            raise    
    return

def changeToInputDirectory(inDir):
    try:
        os.chdir(inDir) # Change to seperated directory
    except:
        sys.exit("Folder with input data does not exist") # Exit program if input data folder is not found
    return

def listOfCSV():
    allFiles = os.listdir()
    files = []
    for csvFiles in allFiles:
        if csvFiles.endswith(".csv"):
            files.append(csvFiles)
    return files

def stitchChannelData(folders):
    loggerFolder = str(rootSeparatedFolder) + '\\' + str(folders)
    changeToInputDirectory(loggerFolder)

    # Get a list for the files in the cwd
    # Now do the operations on the files
    files = listOfCSV()

    if len(files) != 12: # Only works for now... must take out later!!
        print("Missing files in folder.") 
        for index in files:
            print(index)
        print(" ")

    list_ = []
    for file_ in files:
        df = pd.read_csv(file_, index_col=None, header=0)
        list_.append(df)
    frame = pd.concat(list_)
    
        # At this stage, it may be useful to convert the date to a date time object, or a UNIX goody
        # One can do this: http://pbpython.com/excel-file-combine.html
    fileName = frame.columns.values[1]
    dataLoggerFolder = str(rootStitchingFolder) + '\\' + str(fileName)
    makeDirectoryFolder(dataLoggerFolder)
    os.chdir(dataLoggerFolder)
    frame.to_csv(fileName+'.csv', sep=",", encoding='utf-8', index=False)
    return
###########################################################
#                               Main
###########################################################

# Define variables:
# Directory for where to find the separated csv files
rootSeparatedFolder = 'C:\Project\Data\Separated'

# Create the folder for the stitched together documents (if it doesn't already exist)
rootStitchingFolder = 'C:\Project\Data\Stitched'
makeDirectoryFolder(rootStitchingFolder)
changeToInputDirectory(rootSeparatedFolder)
folderNames = os.listdir()
# Loop through all of the folders, this will work so that the work is done in each of the folders
for folders in folderNames:
    stitchChannelData(folders)