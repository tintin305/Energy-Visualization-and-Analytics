import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import errno
import datetime

# Folder for stitched data
rootStitchingFolder = 'C:\Project\Data\Stitched'

rootEntireDataset = 'C:\Project\Data\Entire Dataset'

try:
    os.makedirs(rootEntireDataset)
except OSError:
    if not os.path.isdir(rootEntireDataset):
        raise  

# Makes a list of all the folders in the cwd
folderNames = []
os.chdir(rootStitchingFolder)
folderNames = os.listdir()

list_ = []
for file_ in folderNames:
    sensorPath = str(rootStitchingFolder) + '\\' + str(file_)
    os.chdir(sensorPath)
    df = pd.read_csv(file_+'.csv', index_col=None, header=0)
    list_.append(df)

# Change this for adding on to the side
test = 'ValueTimestamp'
final = pd.concat(list_)

fileName = 'Entire Dataset.csv'


os.chdir(rootEntireDataset)
final.to_csv(fileName, sep=",", encoding='utf-8', index=False)



    # At this stage, it may be useful to convert the date to a date time object, or a UNIX goody
    # One can do this: http://pbpython.com/excel-file-combine.html
