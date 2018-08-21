import json
import os
import pandas as pd
import sys

# Read in geoJSON data as a string
f = open("../../tmp/Map/wits-buildings.txt","r")
stringVar = f.read()
f.close()
stringVar = stringVar.replace("var statesData = {", "{")

#  Read in data file containing dataloggers and their respective summed total
csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Map/temp.csv")
try:
    data_raw = pd.read_csv(csvPath)
except:
    print("error loading csv")
    sys.exit()

data = json.loads(stringVar)

#  Set all density's to 0
for z in range(0, len(data['features'])):
    data['features'][z]['properties']['density'] = 0

# Loop through each logger
for row_index,row in data_raw.iterrows():
    # Loop through each building
    for z in range(0, len(data['features'])):
        # Check if the logger matches a logger for the building
        if data_raw.DataLogger[row_index] in data['features'][z]['properties']['loggers']:
            # Add the logger's sum to the building's density
            data['features'][z]['properties']['density'] = data['features'][z]['properties']['density'] + data_raw.loggerMagnitude[row_index]




# Create a string to output the updated geoJSON data
stringVar = "var statesData = " + json.dumps(data)

# Output to a file
f = open("../../tmp/Map/wits-buildings.txt","w")
f.write(stringVar)
f.close()
