import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import errno
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

def changeToOutputDirectory(outDir):
    # change to output directory
    try:
        os.chdir('C:\Project\Data\Separated')
    # if output directory does not exist, make an output directory and change to it
    except :
        os.makedirs('C:\Project\Data\Separated') 
        os.chdir('C:\Project\Data\Separated')
    return

def makeDir(dirName, folderName):

    try:
        os.makedirs(folderName)
    except OSError:
        if not os.path.isdir(folderName):
            raise    
    directory = dirName + '\\' +  str(folderName) 
    os.chdir(directory)

    return

def splitIntoIndividualChannels(files, dataDirectory, outputDirectory):
    for fileToSplit in files:
        os.chdir(dataDirectory)
        # Open the csv file so that panda can work with it
        s = pd.read_csv(fileToSplit, sep=",")
        # Looping through the files and getting out the date column and the selected column
        for columns in range(1,(len(s.columns.values))):
            # s.columns.values[] is used to select the columns required
            extracted = s[[s.columns.values[0], s.columns.values[columns]]]

            folderName = s.columns.values[columns]
            changeToOutputDirectory()
            makeDir(outputDirectory)

    return
    



        # Making the file name
        sensorName = extracted.columns.values[1]
        date = extracted.iloc[1,0]
        year = date[:4]
        month = date[5:7]
        if month == '01':
            yearHalf = 1
        else:
            yearHalf = 2

        filename = str(s.columns.values[columns]) + '-' + str(year) + '-' + str(yearHalf)  + '.csv'

        s.to_csv(filename, sep=",", encoding='utf-8',columns=list(extracted), index=False)



################################################################
#                               Main
################################################################

dataDirectory = 'C:\Project\Data\Half Years'
outputDirectory = 'C:\Project\Data\Separated' 
csvFileList = findCsvFiles(dataDirectory)
splitIntoIndividualChannels(csvFileList, dataDirectory, outputDirectory)