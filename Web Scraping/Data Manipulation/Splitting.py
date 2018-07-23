import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import errno
import sys

def listDataFiles(directory):
    try:
        os.chdir(directory)
    except:
        sys.exit(directory)
        
    # Makes a list of all the files in the directory
    allFiles = os.listdir()

    # Creates an array that stores all of the names of the csv files in the cwd
    csvFiles = []
    for files in allFiles:
        if files.endswith(".csv"):
            csvFiles.append(files)
    return csvFiles

def makeAndChangeDir(newDirectory):
    try:
        os.chdir(newDirectory)
    except:
        os.makedirs(newDirectory)
        os.chdir(newDirectory)
    return

def newOutputDir(folderName, outputDir):
    
    try:
        os.makedirs(folderName)
    except OSError:
        if not os.path.isdir(folderName):
            raise    
    directory = outputDir + '\\' +  str(folderName)
    
    os.chdir(directory)

    return

def makeFilename(extractedData):
    # Making the file name
    sensorName = extractedData.columns.values[1]
    date = extractedData.iloc[1,0]
    year = date[:4]
    month = date[5:7]
    if month == '01':
        yearHalf = 1
    else:
        yearHalf = 2

    filename = sensorName+ '-' + str(year) + '-' + str(yearHalf)  + '.csv'
    return filename



def separateChannels(csvFiles, outputDir, dataDir):
    for filename in csvFiles:
        makeAndChangeDir(dataDir)
        # Open the csv file so that panda can work with it
        s = pd.read_csv(filename, sep=",")
        # Looping through the files and getting out the date column and the selected column
        for columns in range(1,(len(s.columns.values))):
            # s.columns.values[] is used to select the columns required
            extracted = s[[s.columns.values[0], s.columns.values[columns]]]

            folderName = s.columns.values[columns]
            makeAndChangeDir(outputDir)
            newOutputDir(folderName, outputDir)
            filename = makeFilename(extracted)
            s.to_csv(filename, sep=",", encoding='utf-8',columns=list(extracted), index=False)


    return
###########################################################
#                               Main
###########################################################
dataDirectory = 'C:\Project\Data\Half Years'
outputDirectory = 'C:\Project\Data\Separated'
listOfFiles = listDataFiles(dataDirectory)
separateChannels(listOfFiles, outputDirectory, dataDirectory)

