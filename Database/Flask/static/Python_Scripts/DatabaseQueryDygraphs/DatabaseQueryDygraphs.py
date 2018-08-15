import numpy as np
import pandas as pd
import json
import requests
import sys
import os
from collections import namedtuple
import csv
#  /usr/share/opentsdb/bin/tsdb query 1y-go  sum LoggerName


def saveQueryDetails(requestedSettings):
    # csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    # os.chdir(csvPath)
    # with open('queryDetails.txt','w') as write_file:
    #     json.dump(queryDetails, write_file)
    return

def createQueryUrl(requestedSettings):
    # Get the details out of the object
    aggregator = requestedSettings['aggregator']
    downsample = requestedSettings['downsample']
    tagKey = requestedSettings['tagKey']
    tagValue = requestedSettings['tagValue']
    metric = requestedSettings['metric']
    host = requestedSettings['host']
    port = requestedSettings['port']
    ms = requestedSettings['ms']
    arrays = requestedSettings['arrays']
    tsuids = requestedSettings['tsuids']
    annotations = requestedSettings['annotations']
    startDate = requestedSettings['startDate']
    endDate = requestedSettings['endDate']

    startDate = dateFormatting(startDate)
    endDate = dateFormatting(endDate)

    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate + '&m=' + aggregator + ':' + downsample + ':' + metric + '{' + tagKey + '=' + tagValue + '}'
   
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    os.chdir(csvPath)
    f = open('url.txt','w')
    f.write(url)
    f.close()

    return url

def dateFormatting(date):
    formattedDate = date.replace('-', '/')

    return formattedDate

def queryDatabase(url):
    data = requests.get(url)
    test = data.text
    return test


def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    os.chdir(csvPath)
    with open('pythonData.csv','w') as write_file:
        json.dump(queryData, write_file)    
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

def generateDygraphsData(requestedSettings):
    # Save query details to a text file (used for testing)
    saveQueryDetails(requestedSettings)

    url = createQueryUrl(requestedSettings)

    queryData = queryDatabase(url)

    # writeDataToCSV(queryData)

    extractData(queryData)


