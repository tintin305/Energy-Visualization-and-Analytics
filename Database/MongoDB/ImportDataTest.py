import csv
import json
import os
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
# from pymongo import Connection
# import pymongo
# from pymongo import connect as PyConnection

def importData(fileName,folderName):
    pymongoimport --genfieldfile fileName
    # pymongoimport --delimiter ',' --database testdatabase --collection folderName --fieldfile folderName.ff fileName.csv
    return

con = MongoClient('localhost')
test = con.database_names()



rootPath = 'C:\Project\Data\Stitched'
os.chdir(rootPath)

folderNames = []
folderNames = os.listdir()

for file_ in folderNames:
    mongodbPath = 'C:\Project\mongodb\bin\mongo.exe'
    filePath = 'C:\Project\Data\Stitched\' + file_
    os.chdir(filepath)
    fileName = str(filePath) + '.csv'
    # os.chdir(mongodbPath)
    importData(fileName,file_)