import numpy as np
import pandas as pd
import json
import requests
import sys
import os
import errno

def createFolder():
    tmpPath = os.path.join(os.path.dirname(__file__), '../../tmp/')
    os.chdir(tmpPath)
    directory = 'SankeyDiagram'
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return

def saveQueryDetails(queryDetails):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    with open('queryDetails.txt','w') as write_file:
        json.dump(queryDetails, write_file)
    return

def dateFormatting(date):
    formattedDate = date.replace('-', '/')
    return formattedDate

def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    with open('pythonData.csv','w') as write_file:
        json.dump(queryData, write_file)
    return

def formatToJSON(nrSuppliers):
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
    outString = outString + '],"links":['

    # Links for suppliers
    for sup in range(0, nrSuppliers):
        outString = outString+'{"source":' + str(sup+1) + ', "target":0, "value":' + str(data_raw.loggerMagnitude[sup]) + '},'

    # links for users
    for row_index,row in data_raw.iterrows():
        if (row_index >=nrSuppliers):
            outString = outString + '{"source":0, "target":' + str(row_index+1) + ', "value":' + str(data_raw.loggerMagnitude[row_index]) + '},'

    outString = outString[:-1]
    outString = outString + ']};'

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/SankeyDiagram/")
    os.chdir(csvPath)
    try:
        os.remove('data_energyjson.txt')
    except OSError:
        pass
    f = open("data_energyjson.txt", "w")
    f.write(outString)
    f.close()
    return

def queryDatabase(url):
    data = requests.get(url, proxies=dict(http='socks5://localhost:4242', https='socks5://localhost:4242'))
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
        loggerMagnitude = float(loggerTimestampMagnitude[15:])
        roundedMagnitude = round(loggerMagnitude,4)

        inputLine = str(loggerName) + ',' + str(roundedMagnitude) + '\n'
        f = open('temp.csv', 'a+')
        f.write(inputLine)
        count += 1
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

def specifyLoggers(loggersReq):
    if loggersReq == "WestCampus":
        loggers = ["WITS_WC_CLM_GEN_275_kVA_kWh", "WITS_WC_Sturrock_Park_GEN_300_kVA_kWh", "WITS_WC_WITS_CLUB_GENERATOR_100_kVa_kWh", "WITS_WC_Raikes_Road_Main_Incomer_kWh", "WITS_WC_Convocation_Dining_Hall_GEN_125_kVa_kWh", "WITS_WC_Barnato_Sub_Residence_A___D_kWh", "WITS_WC_CLM_Building_TRF_1_kWh", "WITS_WC_CLM_Building_TRF_2_kWh",  "WITS_WC_Catering_Mayas_kWh", "WITS_WC_Chamber_of_Mines_TRF_1_kWh", "WITS_WC_Chamber_of_Mines_TRF_2_kWh", "WITS_WC_Claude_Vergie_House_kWh", "WITS_WC_Club_Minisub_Total_kWh", "WITS_WC_Convocation_Kitchen_kWh", "WITS_WC_DJ_du_Plessis_Building_kWh", "WITS_WC_David_Webster_Hall_kWh", "WITS_WC_Dig_Fields_Rugby_kWh", "WITS_WC_Dig_Fields_Soccer_kWh", "WITS_WC_FNB_Building_TRF_1_kWh", "WITS_WC_FNB_Building_TRF_2_kWh", "WITS_WC_Genmin_Sub_kWh", "WITS_WC_Gymnasium_kWh", "WITS_WC_Hall_29A_kWh",  "WITS_WC_Hall_29C_kWh", "WITS_WC_Maths_Science_North_kWh", "WITS_WC_Maths_Science_South_kWh", "WITS_WC_Old_Grandstand_kWh", "WITS_WC_Oliver_Schreiner_School_of_Law_kWh", "WITS_WC_PIMD_Supply_No_1_kWh", "WITS_WC_PIMD_Supply_No_2_kWh", "WITS_WC_PIMD_Wash_Bay_kWh", "WITS_WC_Science_Stadium_TRF_1_kWh", "WITS_WC_Science_Stadium_TRF_2_kWh", "WITS_WC_Squash_Courts_kWh", "WITS_WC_Stdnts_Village_Unit_A_kWh", "WITS_WC_Stdnts_Village_Unit_B_kWh", "WITS_WC_Stdnts_Village_Unit_C_kWh", "WITS_WC_Stdnts_Village_Unit_D_kWh", "WITS_WC_Stdnts_Village_Unit_E_kWh", "WITS_WC_Stdnts_Village_Unit_F_kWh", "WITS_WC_Stdnts_Village_Unit_G_kWh", "WITS_WC_Stdnts_Village_Unit_H_kWh",  "WITS_WC_Sturrock_Park_Main_kWh", "WITS_WC_The_Barns_kWh",  "WITS_WC_Village_Zesti_Lemonz_kWh","WITS_EC_New_Commerce_Building_kWh"]

    if loggersReq == "Matrix":
        loggers = ["WITS_EC_Matrix_Main_Incomer_kWh", "WITS_EC_Main_Dining_Hall_Matrix_GEN_250_kVA_kWh", "WITS_EC_Matrix_ABSA_Bank_kWh",  "WITS_EC_Matrix_Butchers_Grill_kWh", "WITS_EC_Matrix_Capitec_Bank_kWh", "WITS_EC_Matrix_Chinese_Lantern_Takeaways_kWh", "WITS_EC_Matrix_Chinese_Lantern_kWh", "WITS_EC_Matrix_Computers__kWh", "WITS_EC_Matrix_Cross_Roads_Driving_School_kWh", "WITS_EC_Matrix_DJ_Sports_kWh", "WITS_EC_Matrix_Debonairs_1_kWh","WITS_EC_Matrix_Debonairs_2_kWh", "WITS_EC_Matrix_Delhi_Delicious_kWh", "WITS_EC_Matrix_Deli_Delicious_kWh", "WITS_EC_Matrix_FUNDI_kWh", "WITS_EC_Matrix_First_National_Bank_kWh", "WITS_EC_Matrix_Fresher_Breath_kWh", "WITS_EC_Matrix_Jetline_com_kWh", "WITS_EC_Matrix_Just_Taste_kWh","WITS_EC_Matrix_Kara_Nichha_s_kWh", "WITS_EC_Matrix_Main_Dining_Hall_East_kWh", "WITS_EC_Matrix_Main_Dining_Hall_West_kWh", "WITS_EC_Matrix_Nedbank_kWh", "WITS_EC_Matrix_Ninos_kWh", "WITS_EC_Matrix_Optometrist_kWh", "WITS_EC_Matric_PPS_for_Professionals_kWh", "WITS_EC_Matrix_Pentz_Book_Shop_2_kWh", "WITS_EC_Matrix_Pentz_Book_Shop_kWh", "WITS_EC_Matrix_Sausage_Saloon_kWh", "WITS_EC_Matrix_Sizzlers_kWh", "WITS_EC_Matrix_Standard_Bank_kWh","WITS_EC_Matrix_Stationery_kWh", "WITS_EC_Matrix_ISTpassword_Corner_kWh","WITS_EC_Matrix_The_Sweets_Park_kWh", "WITS_EC_Matrix_Van_Schaik_Bookstore_kWh", "WITS_EC_Matrix_ZA_Cellular_kWh"]
    return loggers

def generateSankeyData(queryFlask, loggersReq):
    createFolder()
    #get our data as an array from read in()
    loggerList = specifyLoggers(loggersReq)
    url = createQueryUrl(queryFlask, loggerList)

    if loggersReq == "Matrix":
        suppliers = 2
    
    if loggersReq == "WestCampus":
        suppliers= 5
    queryDatabase(url)
    formatToJSON(suppliers)
    return