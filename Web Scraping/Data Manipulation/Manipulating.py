import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

# Change the working directory to where the csv files are stored.
os.chdir('C:\Project\data')

# Makes a list of all the files in the directory
allFiles = os.listdir()

# Creates an array that stores all of the names of the csv files in the cwd
files = []
for csvFiles in allFiles:
    if csvFiles.endswith(".csv"):
        files.append(csvFiles)

# # Delete the extra day in the csv files

# # Standard Python opening files
# # csvFile = open(files[0])

# # print(csvFile.read())


# # csvFile.close()


# # Using csv package

# csvFileOriginal = open(files[0])

# csvFile = csv.reader(csvFileOriginal)



# # for row in csvFile:
# #     print(row)



# csvFileOriginal.close()

s = pd.read_csv(files[0], sep=",")

# Replace NaN with 0
s = s.fillna(0)

# print(s)
# print(s.iloc[0,0])

firstEntry = s.iloc[0,0]

firstEntryMonth = firstEntry[6]
# print(firstEntryMonth)
removeAmount = 0
if (firstEntryMonth == '1'):
    # Do the delete from last day based on month check
    for i, row in s.iterrows():
        dateTime = s.iloc[i,0]
        month = dateTime[6]
        if (month == '7'):
            removeAmount = removeAmount + 1

    removedExtra = s[:-removeAmount]
else:
    # This corresponds to the second half of the year file
    # Do the delete from last day based on month check
    for i, row in s.iterrows():
        dateTime = s.iloc[i,0]
        month = dateTime[6]
        if (month == '1'):
            removeAmount = removeAmount + 1
 
    removedExtra = s[:-removeAmount]
 
os.chdir('C:\Project\data\Half Years')
s.to_csv('1.csv', sep=',', encoding='utf-8')
