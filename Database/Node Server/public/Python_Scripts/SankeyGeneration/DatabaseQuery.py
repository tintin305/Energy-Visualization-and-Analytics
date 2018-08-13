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
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    with open('queryDetails.txt','w') as write_file:
        json.dump(queryDetails, write_file)
    return

def createQueryUrl(queryDetails, loggerList):
    # Get the details out of the object
    aggregator = queryDetails['aggregator']
    downsample = queryDetails['downsample']
    rate = queryDetails['metric']
    tagKey = queryDetails['tagKey']
    # tagValue = logger
    # metric = logger
    host = queryDetails['host']
    port = queryDetails['port']
    ms = queryDetails['ms']
    arrays = queryDetails['arrays']
    tsuids = queryDetails['tsuids']
    annotations = queryDetails['annotations']
    startDate = queryDetails['startDate']
    endDate = queryDetails['endDate']

    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate

    for logger in loggerList:
        addOn = '&m=' + aggregator + ':' + downsample + ':' + logger 
        url = url + addOn
   
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    f = open('url.txt','w')
    f.write(url)
    f.close()

    return url

def queryDatabase(url):
    data = requests.get(url)
    dataJSON = data.json()

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    try:
        os.remove('temp.csv')
    except OSError:
        pass
    
    count = 0
    while count < len(dataJSON):
        loggerName = dataJSON[count]['metric']
        loggerDPS = dataJSON[count]['dps']
        loggerDPSStr = str(loggerDPS)[1:-1]
        loggerTimestampMagnitude = loggerDPSStr.strip('[').replace('], [', '\n').strip(']')
        loggerMagnitude = loggerTimestampMagnitude[15:]

        header = str(loggerName) + ',' + loggerMagnitude + '\n'
        f = open('temp.csv', 'a+')
        f.write(header)
        count += 1

def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    with open('pythonData.csv','w') as write_file:
        json.dump(queryData, write_file)
    return

def specifyLoggers():
    loggers = ["WITS_EC_Main_Dining_Hall_Matrix_GEN_250_kVA_kWh", "WITS_EC_Matrix_ABSA_Bank_kWh", "WITS_EC_Matrix_Basement_DB_kWh", "WITS_EC_Matrix_Butchers_Grill_kWh", "WITS_EC_Matrix_Capitec_Bank_kWh", "WITS_EC_Matrix_Chinese_Lantern_Takeaways_kWh", "WITS_EC_Matrix_Chinese_Lantern_kWh", "WITS_EC_Matrix_Computers__kWh", "WITS_EC_Matrix_Cross_Roads_Driving_School_kWh", "WITS_EC_Matrix_DJ_Sports_kWh", "WITS_EC_Matrix_Debonairs_1_kWh","WITS_EC_Matrix_Debonairs_2_kWh", "WITS_EC_Matrix_Delhi_Delicious_kWh", "WITS_EC_Matrix_Deli_Delicious_kWh", "WITS_EC_Matrix_FUNDI_kWh", "WITS_EC_Matrix_First_National_Bank_kWh", "WITS_EC_Matrix_Fresher_Breath_kWh", "WITS_EC_Matrix_Jetline_com_kWh", "WITS_EC_Matrix_Just_Taste_kWh","WITS_EC_Matrix_Kara_Nichha_s_kWh", "WITS_EC_Matrix_Main_Dining_Hall_East_kWh", "WITS_EC_Matrix_Main_Dining_Hall_West_kWh", "WITS_EC_Matrix_Main_Incomer_kWh", "WITS_EC_Matrix_Nedbank_kWh", "WITS_EC_Matrix_Ninos_kWh", "WITS_EC_Matrix_Optometrist_kWh", "WITS_EC_Matric_PPS_for_Professionals_kWh", "WITS_EC_Matrix_Panel_D9_kWh", "WITS_EC_Matrix_Pentz_Book_Shop_2_kWh", "WITS_EC_Matrix_Pentz_Book_Shop_kWh", "WITS_EC_Matrix_SBM_G_Panel_kWh","WITS_EC_Matrix_SMB_G_Ground_Floor_kWh","WITS_EC_Matrix_Sausage_Saloon_kWh", "WITS_EC_Matrix_Sizzlers_kWh", "WITS_EC_Matrix_Standard_Bank_kWh","WITS_EC_Matrix_Stationery_kWh", "WITS_EC_Matrix_ISTPassword_Corner_kWh","WITS_EC_Matrix_The_Sweets_Park_kWh", "WITS_EC_Matrix_Van_Schaik_Bookstore_kWh", "WITS_EC_Matrix_ZA_Cellular_kWh"]

    return loggers

def main():
    #get our data as an array from read in()
    queryDetails = read_in()
    loggerList = specifyLoggers()

    url = createQueryUrl(queryDetails, loggerList)

    queryDatabase(url)

# Start process


if __name__ == '__main__':
    main()