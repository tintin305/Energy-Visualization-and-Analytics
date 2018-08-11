import numpy as np
import pandas as pd
import json
import requests
import sys
import os
from collections import namedtuple
import csv
#  /usr/share/opentsdb/bin/tsdb query 1y-go  sum LoggerName

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def saveQueryDetails(queryDetails):
    # csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    # os.chdir(csvPath)
    # with open('queryDetails.txt','w') as write_file:
    #     json.dump(queryDetails, write_file)
    return

def createQueryUrl(queryDetails):
    # Get the details out of the object
    aggregator = queryDetails['aggregator']
    downsample = queryDetails['downsample']
    rate = queryDetails['metric']
    tagKey = queryDetails['tagKey']
    tagValue = queryDetails['tagValue']
    metric = queryDetails['metric']
    host = queryDetails['host']
    port = queryDetails['port']
    ms = queryDetails['ms']
    arrays = queryDetails['arrays']
    tsuids = queryDetails['tsuids']
    annotations = queryDetails['annotations']
    startDate = queryDetails['startDate']
    endDate = queryDetails['endDate']

    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate + '&m=' + aggregator + ':' + downsample + ':' + metric + '{' + tagKey + '=' + tagValue + '}'
   
    # csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    # os.chdir(csvPath)
    # f = open('url.txt','w')
    # f.write(url)
    # f.close()

    return url

def queryDatabase(url):
    data = requests.get(url)
    test = data.text
    return test

def writeDataToCSV(queryData):
    # csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    # os.chdir(csvPath)
    # with open('pythonData.csv','w') as write_file:
    #     json.dump(queryData, write_file)    
    return

def extractData(queryData):
    queryData = json.loads(queryData[1:-1])
    dataArray = queryData['dps']

    header = 'Timestamp,' +  str(queryData['metric'] + '\n')

    data = str(dataArray)[1:-1]
    data = data.strip('[')
    data = data.replace('], [', '\n')
    data = data.strip(']')

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    os.chdir(csvPath)
    f = open('temp.csv','w')
    f.write(header)
    f.write(data)
    f.close()

def main():
    #get our data as an array from read_in()
    queryDetails = read_in()
    # Save query details to a text file (used for testing)
    saveQueryDetails(queryDetails)

    url = createQueryUrl(queryDetails)

    queryData = queryDatabase(url)

    writeDataToCSV(queryData)

    extractData(queryData)

    print(queryDetails)

# Start process
if __name__ == '__main__':
    main()