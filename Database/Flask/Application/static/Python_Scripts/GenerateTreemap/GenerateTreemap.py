import numpy as np
import pandas as pd
import json
import requests
import sys
import os

#Read data from stdin
def loadMetrics():
    csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/Metrics/Metrics.csv")
    # This will need to be fixed, as python reads the file in as a string, however, the data comes through formatted as a JSON.
    metrics = open(csvPath, 'r')
    print(metrics)
    try:
        with open(csvPath) as f:
            metrics = json.load(f)
    except:
        print("error loading data")
        sys.exit()
    return metrics

def saveQueryDetails(queryDetails):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    with open('queryDetails.txt','w') as write_file:
        json.dump(queryDetails, write_file)
    return

def createQueryUrl(metricsParams, metrics):
    # Get the details out of the object
    aggregator = metricsParams['aggregator']
    downsample = metricsParams['downsample']
    rate = metricsParams['metric']
    tagKey = metricsParams['tagKey']
    host = metricsParams['host']
    port = metricsParams['port']
    ms = metricsParams['ms']
    arrays = metricsParams['arrays']
    tsuids = metricsParams['tsuids']
    annotations = metricsParams['annotations']
    startDate = metricsParams['startDate']
    endDate = metricsParams['endDate']

    startDate = dateFormatting(startDate)
    endDate = dateFormatting(endDate)

    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate



    for metric in metrics:
        addOn = '&m=' + aggregator + ':' + downsample + ':' + metric 
        url = url + addOn

    inputLine = queryDatabase(url)

    return inputLine

def saveURL(url):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/TreeMap/")
    os.chdir(csvPath)
    f = open('url.txt','w')
    f.write(url)
    f.close()
    return

def dateFormatting(date):
    formattedDate = date.replace('-', '/')

    return formattedDate

def queryDatabase(url):
    data = requests.get(url, 
                    proxies=dict(http='socks5://localhost:4242',
                                 https='socks5://localhost:4242'))
    dataJSON = data.json()

    count = 0
    inputLine = ''
    while count < len(dataJSON):
        loggerName = dataJSON[count]['metric']
        loggerDPS = dataJSON[count]['dps']
        loggerCampus = dataJSON[count]['tags']['Campus']
        loggerDPSStr = str(loggerDPS)[1:-1]
        loggerTimestampMagnitude = loggerDPSStr.strip('[').replace('], [', '\n').strip(']')
        loggerMagnitude = round(float(loggerTimestampMagnitude[15:]))

        inputLine = inputLine + str(loggerName) + ',' + str(loggerMagnitude) + ',' + loggerCampus + '\n'
        count += 1
    return inputLine

def createAccumulatedCSV(metricsParams, metrics):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/TreeMap/")
    os.chdir(csvPath)
    try:
        os.remove('temp.csv')
    except OSError:
        pass

    numLoggersPerQuery = 72
    numberOfQueries = int(np.ceil(len(metrics)/numLoggersPerQuery)) 

    f = open('temp.csv', 'a+')     
    header = "DataLogger,loggerMagnitude,Campus\n"
    f.write(header)

    for x in range(1, numberOfQueries):
        rangeStart = (x-1)*numLoggersPerQuery
        rangeEnd = x*numLoggersPerQuery -1
        f = open('temp.csv', 'a+') 
        inputLine = createQueryUrl(metricsParams, metrics[rangeStart: rangeEnd+1])

        f.write(inputLine)
        f.close()

    rangeStart = (numberOfQueries-1)*numLoggersPerQuery
    rangeEnd = len(metrics)
    f = open('temp.csv', 'a+')
    inputLine = createQueryUrl(metricsParams, metrics[rangeStart: rangeEnd+1])
    f.write(inputLine)
    f.close()

    return

def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/TreeMap/")
    os.chdir(csvPath)
    with open('pythonData.json','w') as write_file:
        json.dump(queryData, write_file)
    return

def formatToJSON():
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/TreeMap/temp.csv")

    data = pd.read_csv(csvPath)
    outString = '[' + '\n' 

    for row_index, row in data.iterrows():
        outString = outString + '{' + '\n' + '"key": "' + str(data.DataLogger[row_index]) + '",\n' + '"region": ' + '"University of the Witwatersrand"' + ',\n' + '"subregion": "' + str(data.Campus[row_index]) + '",\n' + '"value": ' + str(data.loggerMagnitude[row_index]) + '\n' + '},' + '\n' 

    outString = outString[:-2] + '\n' + ']'
    savePath = os.path.join(os.path.dirname(__file__), "../../TreeMap/")
    try:
        if not os.path.exists(savePath):
            os.makedirs(savePath)
    except OSError:
        print ('Error: Creating directory. ' +  savePath)

    os.chdir(savePath)
    f = open('accumulatedData.json', 'w')
    f.write(outString)
    f.close()


    return

def generateTreeMap(metricsParams):
    metrics = loadMetrics()

    # Remove the loggers that are for kVarh as this can distort the visual
    # Other loggers that are removed as this should just show loads
    metrics[:] = [x for x in metrics if 'kVarh' not in x]
    metrics[:] = [x for x in metrics if 'Incomer' not in x]
    metrics[:] = [x for x in metrics if 'GEN' not in x]
    metrics[:] = [x for x in metrics if 'Gen' not in x]
    metrics[:] = [x for x in metrics if 'HT' not in x]

    writeDataToCSV(metrics)

    createAccumulatedCSV(metricsParams, metrics)

    formatToJSON()
    
    return 