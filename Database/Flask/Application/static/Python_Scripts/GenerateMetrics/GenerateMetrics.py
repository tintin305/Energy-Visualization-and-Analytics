import pandas as pd
import json
import requests
import os
import socket
import errno

def saveQueryDetails(queryDetails):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    os.chdir(csvPath)
    with open('queryDetails.txt','w') as write_file:
        json.dump(queryDetails, write_file)
    return

def createQueryUrl(metricsParams):
    host = metricsParams['host']
    port = metricsParams['port']

    url = 'http://' + str(host) + ':' + str(port) + '/api/suggest?type=metrics&max=10000'
    return url

def queryDatabase(url):
    data = requests.get(url, 
                    proxies=dict(http='socks5://localhost:4242',
                                 https='socks5://localhost:4242'))
    test = data.json()
    return test

def writeDataToCSV(queryData):
    tmpPath = os.path.join(os.path.dirname(__file__), "../../tmp")
    os.chdir(tmpPath)
    directory = 'Metrics'
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Metrics/")
    os.chdir(csvPath)
    with open('Metrics.csv','w') as write_file:
        json.dump(queryData, write_file)
    return

def generateMetrics(metricsParams):
    url = createQueryUrl(metricsParams)

    queryData = queryDatabase(url)

    writeDataToCSV(queryData)
    return queryData