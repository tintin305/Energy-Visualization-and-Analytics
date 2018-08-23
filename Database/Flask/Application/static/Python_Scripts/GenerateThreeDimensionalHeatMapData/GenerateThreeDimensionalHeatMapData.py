import pandas as pd
import json
import requests
import os
import socket
import errno

def saveQueryDetails(requestedSettings):
    tmpPath = os.path.join(os.path.dirname(__file__), "../../tmp")
    os.chdir(tmpPath)
    directory = 'ThreeDimensionalHeatMap'
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    txtPath = os.path.join(os.path.dirname(__file__), "../../tmp/ThreeDimensionalHeatMap")
    os.chdir(txtPath)
    with open('queryDetails.txt','w') as write_file:
        json.dump(requestedSettings, write_file)
    return

def saveURL(url):
    txtPath = os.path.join(os.path.dirname(__file__), "../../tmp/ThreeDimensionalHeatMap")
    os.chdir(txtPath)
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
    data = requests.get(url, 
                    proxies=dict(http='socks5://localhost:4242',
                                 https='socks5://localhost:4242'))
    test = data.text
    return test


def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/ThreeDimensionalHeatMap")
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

    csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/ThreeDimensionalHeatMap")
    os.chdir(csvPath)
    f = open('temp.csv','w')
    f.write(header)
    f.write(data)
    f.close()
    return

def generateThreeDimensionHeatMapData(requestedSettings):
    saveQueryDetails(requestedSettings)

    url = createQueryUrl(requestedSettings)

    queryData = queryDatabase(url)

    extractData(queryData)
    return