import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import errno
import sys

try:
    os.chdir('C:\Project\Data\Half Years')
except:
    sys.exit('Data folder does not exist')

# Makes a list of all the files in the directory
allFiles = os.listdir()

# Creates an array that stores all of the names of the csv files in the cwd
csvFiles = []
for files in allFiles:
    if files.endswith(".csv"):
        csvFiles.append(files)

for filename in csvFiles:
    try:
        os.chdir('C:\Project\Data\Half Years')
    except:
        os.makedirs('C:\Project\Data\Half Years')
        os.chdir('C:\Project\Data\Half Years')
    
    # Open the csv file so that panda can work with it
    s = pd.read_csv(filename, sep=",")

    # Replace NaN with 0
    s = s.fillna(0)

    # Looping through the files and getting out the date column and the selected column
    for columns in range(1,(len(s.columns.values))):
        # s.columns.values[] is used to select the columns required
        extracted = s[[s.columns.values[0], s.columns.values[columns]]]

        folderName = s.columns.values[columns]

        try:
            os.chdir('C:\Project\Data\Separated')
        except:
            os.makedirs('C:\Project\Data\Separated')
            os.chdir('C:\Project\Data\Separated')
            


        try:
            os.makedirs(folderName)
        except OSError:
            if not os.path.isdir(folderName):
                raise    
        directory = 'C:\Project\Data\Separated' + '\\' +  str(folderName) 
        os.chdir(directory)

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

