import numpy as np
import pandas as pd
import json
import requests
import sys
import os
import socket
# from collections import namedtuple
# import csv
# from time import sleep
#  /usr/share/opentsdb/bin/tsdb query 1y-go  sum LoggerName

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def saveQueryDetails(queryDetails):
    # csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    # os.chdir(csvPath)
    # with open('queryDetails.txt','w') as write_file:
        # json.dump(queryDetails, write_file)
    return

def createQueryUrl(queryFlask, loggerList):
    # Get the details out of the object
    aggregator = queryFlask['aggregator']
    downsample = queryFlask['downsample']
    rate = queryFlask['metric']
    tagKey = queryFlask['tagKey']
    host = queryFlask['host']
    port = queryFlask['port']
    ms = queryFlask['ms']
    arrays = queryFlask['arrays']
    tsuids = queryFlask['tsuids']
    annotations = queryFlask['annotations']
    startDate = queryFlask['startDate']
    endDate = queryFlask['endDate']

    # host = 'localhost'
    # port = 4242
    # ms = 'true'
    # arrays = 'false'
    # tsuids = 'false'
    # annotations = 'false'
    # startDate = '2018/03/01-00:00'
    # endDate =  '2018/06/01-23:30'
    # aggregator = 'avg'
    # downsample = '0all-sum'

    startDate = dateFormatting(startDate)
    endDate = dateFormatting(endDate)

    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate

    for logger in loggerList:
        addOn = '&m=' + aggregator + ':' + downsample + ':' + logger 
        url = url + addOn
   


    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Map/")
    os.chdir(csvPath)
    f = open('url.txt','w')
    f.write(url)
    f.close()

    return url

def dateFormatting(date):
    formattedDate = date.replace('-', '/')

    return formattedDate

def queryDatabase(url):
    data = requests.get(url, 
                    proxies=dict(http='socks5://localhost:4242',
                                 https='socks5://localhost:4242'))
    dataJSON = data.json()

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Map/")
    os.chdir(csvPath)
    try:
        os.remove('temp.csv')
    except OSError:
        pass
    
    header = "DataLogger,loggerMagnitude\n"
    f = open('temp.csv', 'a+')
    f.write(header)
    count = 0
    while count < len(dataJSON):
        loggerName = dataJSON[count]['metric']
        loggerDPS = dataJSON[count]['dps']
        loggerDPSStr = str(loggerDPS)[1:-1]
        loggerTimestampMagnitude = loggerDPSStr.strip('[').replace('], [', '\n').strip(']')
        loggerMagnitude = loggerTimestampMagnitude[15:]

        inputLine = str(loggerName) + ',' + loggerMagnitude + '\n'
        f = open('temp.csv', 'a+')
        f.write(inputLine)
        count += 1

def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Map/")
    os.chdir(csvPath)
    with open('pythonData.csv','w') as write_file:
        json.dump(queryData, write_file)
    return

def specifyLoggers():

    loggers = ["WITS_WC_Sturrock_Park_Main_kWh","WITS_WC_Barnato_Sub_Residence_A___D_kWh","WITS_WC_CLM_Building_TRF_1_kWh","WITS_WC_CLM_Building_TRF_2_kWh","WITS_WC_CLTD_Building_kWh","WITS_WC_Catering_Mayas_kWh","WITS_WC_Chamber_of_Mines_TRF_1_kWh","WITS_WC_Chamber_of_Mines_TRF_2_kWh","WITS_WC_Claude_Vergie_House_kWh","WITS_WC_Club_Minisub_Total_kWh","WITS_WC_Convocation_Kitchen_kWh","WITS_WC_DJ_du_Plessis_Building_kWh","WITS_WC_David_Webster_Hall_kWh","WITS_WC_Dig_Fields_Rugby_kWh","WITS_WC_Dig_Fields_Soccer_kWh","WITS_WC_Educom_Building_Trf_2_kWh","WITS_WC_Educom_Building_Trf_3_kWh","WITS_WC_Educom_Building_Trf_4_kWh","WITS_WC_FNB_Building_TRF_1_kWh","WITS_WC_FNB_Building_TRF_2_kWh","WITS_WC_Flower_Hall_kWh","WITS_WC_Genmin_LAB_kWh","WITS_WC_Gymnasium_kWh","WITS_WC_Hall_29A_kWh","WITS_WC_Hall_29B_kWh","WITS_WC_Hall_29C_kWh","WITS_WC_Humphrey_Raikes_kWh","WITS_WC_Maths_Science_Building_kWh","WITS_WC_Old_Grandstand_kWh","WITS_WC_Oliver_Schreiner_School_of_Law_kWh","WITS_WC_PIMD_Supply_No_1_kWh","WITS_WC_PIMD_Supply_No_2_kWh","WITS_WC_PIMD_Wash_Bay_kWh","WITS_WC_Science_Stadium_TRF_1_kWh","WITS_WC_Science_Stadium_TRF_2_kWh","WITS_WC_Squash_Courts_kWh","WITS_WC_Stdnts_Village_Unit_A_kWh","WITS_WC_Stdnts_Village_Unit_B_kWh","WITS_WC_Stdnts_Village_Unit_C_kWh","WITS_WC_Stdnts_Village_Unit_D_kWh","WITS_WC_Stdnts_Village_Unit_E_kWh","WITS_WC_Stdnts_Village_Unit_F_kWh","WITS_WC_Stdnts_Village_Unit_G_kWh","WITS_WC_Stdnts_Village_Unit_H_kWh","WITS_WC_The_Barns_kWh","WITS_WC_Tower_of_Lights_Total_kWh","WITS_WC_Village_Zesti_Lemonz_kWh","WITS_EC_New_Commerce_Building_kWh"]
    return loggers

def upDateGeoJSON(startDate, endDate):
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


    #  Set the dates
    data['dates']['start'] = startDate
    data['dates']['end'] = endDate

    #  Set all density's to 0
    for z in range(0, len(data['features'])):
        data['features'][z]['properties']['density'] = 0

    # # Make all per unit
    # maxValue = data_raw['loggerMagnitude'].max()
    # data_raw.loggerMagnitude = data_raw.loggerMagnitude/maxValue
    
    # Loop through each logger
    for row_index,row in data_raw.iterrows():
        # Loop through each building
        for z in range(0, len(data['features'])):
            # Check if the logger matches a logger for the building
            if data_raw.DataLogger[row_index] in data['features'][z]['properties']['loggers']:
                # Add the logger's sum to the building's density
                data['features'][z]['properties']['density'] = data['features'][z]['properties']['density'] + data_raw.loggerMagnitude[row_index]


    
    # # Make all per unit
    maxValue = data_raw['loggerMagnitude'].max()
    
    for z in range(0, len(data['features'])):
        data['features'][z]['properties']['per_unit'] = data['features'][z]['properties']['density']/maxValue


    # Round off values
    for z in range(0, len(data['features'])):
        data['features'][z]['properties']['density'] =np.floor(data['features'][z]['properties']['density'])



    # Create a string to output the updated geoJSON data
    stringVar = "var statesData = " + json.dumps(data)

    # Output to a file
    f = open("../../tmp/Map/wits-buildings.txt","w")
    f.write(stringVar)
    f.close()



def generateMapData(queryFlask, startDate, endDate):
    loggerList = specifyLoggers()
    print(loggerList)
    url = createQueryUrl(queryFlask, loggerList)
    print(url)

    queryDatabase(url)
    upDateGeoJSON(startDate, endDate)
