# import numpy as np
import pandas as pd
import json
import requests
# import sys
import os
# from collections import namedtuple
# import csv
#  /usr/share/opentsdb/bin/tsdb query 1y-go  sum LoggerName

def saveQueryDetails(queryDetails):
    # csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/")
    # os.chdir(csvPath)
    # with open('queryDetails.txt','w') as write_file:
    #     json.dump(queryDetails, write_file)
    return

def createQueryUrl(metricsParams):

    host = metricsParams['host']
    port = metricsParams['port']


    url = 'http://' + str(host) + ':' + str(port) + '/api/suggest?type=metrics&max=10000'

    return url

def queryDatabase(url):
    data = requests.get(url)
    test = data.json()
    return test

def writeDataToCSV(queryData):
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
    # extractData(queryData)
