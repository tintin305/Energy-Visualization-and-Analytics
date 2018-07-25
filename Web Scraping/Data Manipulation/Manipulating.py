import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

def findCsvFiles(dataDirectory):
    # Change the working directory to where the csv files are stored.
    try:
        os.chdir(dataDirectory)
    except:
        sys.exit("Data directory does not exist")

    # Makes a list of all the files in the directory
    allFiles = os.listdir()

    # Creates an array that stores all of the names of the csv files in the cwd
    csvFiles = []
    for fileName in allFiles:
        if fileName.endswith(".csv"):
            csvFiles.append(fileName)
    return csvFiles

def replaceNan(inFile):
    inFile = inFile.fillna(-1)
    return inFile

def removeExtraLines(inFile):
    # Obtain time-date stamp of the first entry
    firstEntry = inFile.iloc[0,0]
    # Access the month in the time-date stamp
    firstEntryMonth = firstEntry[6]
    removeAmount = 0 # Used to track how many lines need to be removed from the file
    if (firstEntryMonth == '1'):
        removeMonth = '07'
    else:
        removeMonth = '01'

    # Do the delete from last day based on month check
    for i, row in inFile.iterrows():
        dateTime = inFile.iloc[i,0]
        if len(dateTime) <=7:
            removeAmount = removeAmount + 1
            # print(len(dateTime))
        else:
            month = dateTime[5]+ dateTime[6]
            if (month == removeMonth):
                removeAmount = removeAmount + 1
    
    removedExtra = inFile[:-removeAmount]
    return removedExtra

def outputToCsv(outputData, nameOfFile):
    try:
        os.chdir('C:\Project\Data\Half Years')
    except:
            os.makedirs('C:\Project\Data\Half Years')
            os.chdir('C:\Project\Data\Half Years')

    # print(list(outputData).count('Unnamed: 26'))
    if list(outputData).count('Unnamed: 26') >= 1:
        outputData = outputData.drop('Unnamed: 26', 1)
    # print(outputData)
    # print(list(outputData))
    
    # print(list(outputData).count('Unnamed: 26'))
    outputData.to_csv("Cut_"+nameOfFile, sep=',', encoding='utf-8', index = False, columns =list(outputData) )
    os.chdir('C:\Project\Data\Raw Data')
    return
################################################################
#                               Main
################################################################

files = findCsvFiles('C:\Project\Data\Raw Data')
# print(files)
for nameOfFile in files:
    fileData = pd.read_csv(nameOfFile, sep=",")
    # print(nameOfFile)

    fileData = replaceNan(fileData)

    halfYearOut = removeExtraLines(fileData)
    outputToCsv(halfYearOut, nameOfFile)
