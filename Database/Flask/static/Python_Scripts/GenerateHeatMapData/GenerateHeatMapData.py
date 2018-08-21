import pandas as pd
import json
import requests
import os

def saveQueryDetails(requestedSettings):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/HeatMaps/")
    os.chdir(csvPath)
    with open('queryDetails.txt','w') as write_file:
        json.dump(requestedSettings, write_file)
    return

def saveURL(url):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/HeatMaps/")
    os.chdir(csvPath)
    f = open('url.txt','w')
    f.write(url)
    f.close()
    return

def createQueryUrl(requestedSettings):
    # Get the details out of the object
    aggregator = requestedSettings['aggregator']
    downsamplingMagnitude = requestedSettings['downsamplingMagnitude']
    timeDownsamplingRange = requestedSettings['timeDownsamplingRange']
    downsamplingType = requestedSettings['downsamplingType']
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

    # Format the Dates
    startDate = dateFormatting(startDate)
    endDate = dateFormatting(endDate)

    # Create URL
    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate + '&m=' + aggregator + ':' + str(downsamplingMagnitude) + str(timeDownsamplingRange) + '-' + downsamplingType + ':' + metric + '{' + tagKey + '=' + tagValue + '}'

    return url

def dateFormatting(date):
    formattedDate = date.replace('-', '/')

    return formattedDate

def queryDatabase(url):
    data = requests.get(url)
    test = data.text
    return test


def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/HeatMaps/")
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

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/HeatMaps/")
    os.chdir(csvPath)
    f = open('temp.csv','w')
    f.write(header)
    f.write(data)
    f.close()

def generateHeatMapData(requestedSettings):
    # Save query details to a text file (used for testing)
    saveQueryDetails(requestedSettings)

    url = createQueryUrl(requestedSettings)

    # saveQueryDetails(url)

    queryData = queryDatabase(url)

    # writeDataToCSV(queryData)

    extractData(queryData)


