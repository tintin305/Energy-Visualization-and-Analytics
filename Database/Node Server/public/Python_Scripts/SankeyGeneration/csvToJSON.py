import numpy as np
import pandas as pd
import json
import requests
import sys
import os
from collections import namedtuple
import csv      
from time import sleep
      
        # csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/temp.csv")
csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/temp.csv")
try:
    data_raw = pd.read_csv(csvPath)
except:
    print("error loading csv")
    sys.exit()

print(data_raw.head())
outString = 'var energyjson = { "nodes":[{"name":"Middle"},'
for row_index,row in data_raw.iterrows():
    outString = outString + '{"name":"' + data_raw.DataLogger[row_index] + '"},'

outString = outString[:-1]

outString = outString + '],"links":[{"source":1, "target":0, "value":' + str(data_raw.loggerMagnitude[0]) + '},'
outString = outString + '{"source":2, "target":0, "value":' + str(data_raw.loggerMagnitude[1]) + '},'

print(list(data_raw.columns.values))
for row_index,row in data_raw.iterrows():
    if (row_index >=2):
        outString = outString + '{"source":0, "target":' + str(row_index+1) + ', "value":' + str(data_raw.loggerMagnitude[row_index]) + '},'

outString = outString[:-1]
outString = outString + ']};'

# Add last element for unaccounted energy
# TotalSum = data_raw['loggerMagnitude'].sum()
# difference = 2*data_raw.loggerMagnitude[0] - TotalSum
# print(difference)
# outString = outString + '{"source":0, "target":' + str(len(data_raw)) + ', "value":' + str(difference) + '}]};'

print(outString)


# csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
# os.chdir(csvPath)

csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
os.chdir(csvPath)
# f = open('data_energyjson.js','w')
f = open("data_energyjson.js", "w")
f.write(outString)
f.close()

print("now")

sleep(2)

print("after sleep")