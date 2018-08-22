import numpy as np
import pandas as pd
import json
import requests
import sys
import os
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
   


    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
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
    dataJSON = data.json()

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
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
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    with open('pythonData.csv','w') as write_file:
        json.dump(queryData, write_file)
    return

def specifyLoggers(loggersReq):

    if loggersReq == "WestCampus":
        loggers = ["WITS_WC_CLM_GEN_275_kVA_kWh", "WITS_WC_Sturrock_Park_GEN_300_kVA_kWh", "WITS_WC_WITS_CLUB_GENERATOR_100_kVa_kWh", "WITS_WC_Raikes_Road_Main_Incomer_kWh", "WITS_WC_Convocation_Dining_Hall_GEN_125_kVa_kWh", "WITS_WC_Barnato_Sub_Residence_A___D_kWh", "WITS_WC_CLM_Building_TRF_1_kWh", "WITS_WC_CLM_Building_TRF_2_kWh",  "WITS_WC_Catering_Mayas_kWh", "WITS_WC_Chamber_of_Mines_TRF_1_kWh", "WITS_WC_Chamber_of_Mines_TRF_2_kWh", "WITS_WC_Claude_Vergie_House_kWh", "WITS_WC_Club_Minisub_Total_kWh", "WITS_WC_Convocation_Kitchen_kWh", "WITS_WC_DJ_du_Plessis_Building_kWh", "WITS_WC_David_Webster_Hall_kWh", "WITS_WC_Dig_Fields_Rugby_kWh", "WITS_WC_Dig_Fields_Soccer_kWh", "WITS_WC_FNB_Building_TRF_1_kWh", "WITS_WC_FNB_Building_TRF_2_kWh", "WITS_WC_Genmin_Sub_kWh", "WITS_WC_Gymnasium_kWh", "WITS_WC_Hall_29A_kWh",  "WITS_WC_Hall_29C_kWh", "WITS_WC_Maths_Science_North_kWh", "WITS_WC_Maths_Science_South_kWh", "WITS_WC_Old_Grandstand_kWh", "WITS_WC_Oliver_Schreiner_School_of_Law_kWh", "WITS_WC_PIMD_Supply_No_1_kWh", "WITS_WC_PIMD_Supply_No_2_kWh", "WITS_WC_PIMD_Wash_Bay_kWh", "WITS_WC_Science_Stadium_TRF_1_kWh", "WITS_WC_Science_Stadium_TRF_2_kWh", "WITS_WC_Squash_Courts_kWh", "WITS_WC_Stdnts_Village_Unit_A_kWh", "WITS_WC_Stdnts_Village_Unit_B_kWh", "WITS_WC_Stdnts_Village_Unit_C_kWh", "WITS_WC_Stdnts_Village_Unit_D_kWh", "WITS_WC_Stdnts_Village_Unit_E_kWh", "WITS_WC_Stdnts_Village_Unit_F_kWh", "WITS_WC_Stdnts_Village_Unit_G_kWh", "WITS_WC_Stdnts_Village_Unit_H_kWh",  "WITS_WC_Sturrock_Park_Main_kWh", "WITS_WC_The_Barns_kWh",  "WITS_WC_Village_Zesti_Lemonz_kWh", "WITS_EC_New_Commerce_Building_kWh"
        ]

    if loggersReq == "Matrix":
        loggers = ["WITS_EC_Matrix_Main_Incomer_kWh", "WITS_EC_Main_Dining_Hall_Matrix_GEN_250_kVA_kWh", "WITS_EC_Matrix_ABSA_Bank_kWh",  "WITS_EC_Matrix_Butchers_Grill_kWh", "WITS_EC_Matrix_Capitec_Bank_kWh", "WITS_EC_Matrix_Chinese_Lantern_Takeaways_kWh", "WITS_EC_Matrix_Chinese_Lantern_kWh", "WITS_EC_Matrix_Computers__kWh", "WITS_EC_Matrix_Cross_Roads_Driving_School_kWh", "WITS_EC_Matrix_DJ_Sports_kWh", "WITS_EC_Matrix_Debonairs_1_kWh","WITS_EC_Matrix_Debonairs_2_kWh", "WITS_EC_Matrix_Delhi_Delicious_kWh", "WITS_EC_Matrix_Deli_Delicious_kWh", "WITS_EC_Matrix_FUNDI_kWh", "WITS_EC_Matrix_First_National_Bank_kWh", "WITS_EC_Matrix_Fresher_Breath_kWh", "WITS_EC_Matrix_Jetline_com_kWh", "WITS_EC_Matrix_Just_Taste_kWh","WITS_EC_Matrix_Kara_Nichha_s_kWh", "WITS_EC_Matrix_Main_Dining_Hall_East_kWh", "WITS_EC_Matrix_Main_Dining_Hall_West_kWh", "WITS_EC_Matrix_Nedbank_kWh", "WITS_EC_Matrix_Ninos_kWh", "WITS_EC_Matrix_Optometrist_kWh", "WITS_EC_Matric_PPS_for_Professionals_kWh", "WITS_EC_Matrix_Pentz_Book_Shop_2_kWh", "WITS_EC_Matrix_Pentz_Book_Shop_kWh", "WITS_EC_Matrix_Sausage_Saloon_kWh", "WITS_EC_Matrix_Sizzlers_kWh", "WITS_EC_Matrix_Standard_Bank_kWh","WITS_EC_Matrix_Stationery_kWh", "WITS_EC_Matrix_ISTPassword_Corner_kWh","WITS_EC_Matrix_The_Sweets_Park_kWh", "WITS_EC_Matrix_Van_Schaik_Bookstore_kWh", "WITS_EC_Matrix_ZA_Cellular_kWh"]
        # "WITS_EC_Matrix_SMB_G_Ground_Floor_kWh","WITS_EC_Matrix_SBM_G_Panel_kWh","WITS_EC_Matrix_Panel_D9_kWh", "WITS_EC_Matrix_Basement_DB_kWh",
    # return loggersMatrix
    return loggers

def formatToJSON(nrSuppliers):
                    # csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/temp.csv")
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/temp.csv")
    try:
        data_raw = pd.read_csv(csvPath)
    except:
        print("error loading csv")
        sys.exit()

    # Define the nodes for the diagram
    outString = 'var energyjson = { "nodes":[{"name":" "},'
    for row_index,row in data_raw.iterrows():
        outString = outString + '{"name":"' + data_raw.DataLogger[row_index] + '"},'

    outString = outString[:-1]

    # Determine the links between the nodes:
    # nrSuppliers = 3
    outString = outString + '],"links":['

    # Links for suppliers
    for sup in range(0, nrSuppliers):
        outString = outString+'{"source":' + str(sup+1) + ', "target":0, "value":' + str(data_raw.loggerMagnitude[sup]) + '},'
    # outString = outString + '],"links":[{"source":1, "target":0, "value":' + str(data_raw.loggerMagnitude[0]) + '},'
    # outString = outString + '{"source":2, "target":0, "value":' + str(data_raw.loggerMagnitude[1]) + '},'

    # links for users
    for row_index,row in data_raw.iterrows():
        if (row_index >=nrSuppliers):
            outString = outString + '{"source":0, "target":' + str(row_index+1) + ', "value":' + str(data_raw.loggerMagnitude[row_index]) + '},'

    outString = outString[:-1]
    outString = outString + ']};'


    # csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    # os.chdir(csvPath)

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    try:
        os.remove('data_energyjson.txt')
    except OSError:
        pass
    # # f = open('data_energyjson.js','w')
    f = open("data_energyjson.txt", "w")
    f.write(outString)
    f.close()
    # sys.exit()

    # sleep(5)
    return

def getNumberOfSuppliers(loggersReq):
    suppliers = 2
    return suppliers


def generateSankeyData(queryFlask, loggersReq):
    #get our data as an array from read in()
    # queryDetails = read_in()
    print(loggersReq)
    loggerList = specifyLoggers(loggersReq)
    # print(loggerList)
    nrSuppliers = getNumberOfSuppliers(loggersReq)
    url = createQueryUrl(queryFlask, loggerList)
    print(url)

    if loggersReq == "Matrix":
        suppliers = 2
    
    if loggersReq == "WestCampus":
        suppliers= 5
    queryDatabase(url)
    formatToJSON(suppliers)
