import numpy as np
import pandas as pd
import json
import requests
import sys
import os
import socket

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
    try:
        f = open("../../tmp/Map/wits-buildings.txt","r")
        stringVar = f.read()
        f.close()
    except:
        stringVar = 'var statesData = {"type": "FeatureCollection", "dates": {"start": "2018-01-01", "end": "2018-06-30"}, "features": [{"type": "Feature", "id": "02", "properties": {"density": 557496.0, "name": "Chamber of Mines", "loggers": "WITS_WC_Chamber_of_Mines_TRF_1_kWh,WITS_WC_Chamber_of_Mines_TRF_2_kWh", "per_unit": 0.6295756055006912}, "geometry": {"type": "Polygon", "coordinates": [[[28.0266722, -26.1913398], [28.0267363, -26.1917714], [28.0266534, -26.1917814], [28.0266921, -26.1920424], [28.027077, -26.1919964], [28.0270701, -26.1919504], [28.0273915, -26.191912], [28.0272955, -26.1912653], [28.0266722, -26.1913398]]]}}, {"type": "Feature", "id": "03", "properties": {"density": 57760.0, "name": "Flower Hall", "loggers": "WITS_WC_Flower_Hall_kWh", "per_unit": 0.06522900041530016}, "geometry": {"type": "Polygon", "coordinates": [[[28.0259729, -26.1919494], [28.0260503, -26.1919521], [28.0261211, -26.1919476], [28.0261945, -26.1919317], [28.0262771, -26.1919032], [28.0262381, -26.1918017], [28.0262619, -26.1917985], [28.0262231, -26.1917018], [28.0262461, -26.1916956], [28.026209, -26.1915963], [28.026232, -26.191595], [28.0261928, -26.1914914], [28.0259343, -26.1915195], [28.0259243, -26.1916376], [28.0259475, -26.1916325], [28.0259425, -26.191733], [28.0259654, -26.1917305], [28.0259599, -26.1918346], [28.025981, -26.1918357], [28.0259729, -26.1919494]]]}}, {"type": "Feature", "id": "04", "properties": {"name": "Hall 29", "density": 43664.0, "loggers": "WITS_WC_Hall_29A_kWh", "per_unit": 0.04931014731051908}, "geometry": {"type": "Polygon", "coordinates": [[[28.0255909, -26.18638], [28.025623, -26.1866176], [28.0265984, -26.1865116], [28.0265664, -26.186274], [28.0255909, -26.18638]]]}}, {"type": "Feature", "id": "05", "properties": {"name": "School of Law and Chalsty Centre", "density": 210407.0, "loggers": "WITS_WC_Oliver_Schreiner_School_of_Law_kWh", "per_unit": 0.23761126674495833}, "geometry": {"type": "Polygon", "coordinates": [[[28.0248822, -26.1889709], [28.0249106, -26.1891604], [28.0250207, -26.1891523], [28.0250171, -26.1891193], [28.0252027, -26.1890959], [28.0251623, -26.1887793], [28.0252791, -26.1887708], [28.0252814, -26.1888096], [28.0253702, -26.1888028], [28.0256035, -26.189051], [28.0257443, -26.1887733], [28.0257263, -26.1885958], [28.0254746, -26.188622], [28.0254637, -26.1885775], [28.0254343, -26.188531], [28.0253838, -26.1884958], [28.0253128, -26.1884748], [28.0253241, -26.1884305], [28.0249039, -26.1883075], [28.0248342, -26.1885353], [28.024832, -26.1886785], [28.0249039, -26.1886966], [28.024937, -26.1889656], [28.0248822, -26.1889709]]]}}, {"type": "Feature", "id": "06", "properties": {"name": "FNB Building", "density": 369815.0, "loggers": "WITS_WC_FNB_Building_TRF_1_kWh, WITS_WC_FNB_Building_TRF_2_kWh", "per_unit": 0.4176300273859181}, "geometry": {"type": "Polygon", "coordinates": [[[28.0268727, -26.188763], [28.0268076, -26.1882724], [28.0266406, -26.1882902], [28.0266571, -26.188414], [28.0264498, -26.1884361], [28.0264266, -26.188261], [28.0262739, -26.1882773], [28.0262974, -26.188455], [28.0260788, -26.1884783], [28.0260632, -26.1883605], [28.0259021, -26.1883777], [28.0259661, -26.1888599], [28.0261605, -26.1888406], [28.0262072, -26.1889149], [28.0262694, -26.1889701], [28.0263558, -26.1889991], [28.0264491, -26.1890043], [28.0265385, -26.1889755], [28.0266151, -26.1889261], [28.0266593, -26.1888601], [28.0266856, -26.1887869], [28.0268727, -26.188763]]]}}, {"type": "Feature", "id": "07", "properties": {"name": "Commerce Library and Law Clinic", "density": 286339.0, "loggers": "WITS_WC_Educom_Building_Trf_2_kWh,WITS_WC_Educom_Building_Trf_3_kWh,WITS_WC_Educom_Building_Trf_4_kWh", "per_unit": 0.32336054993115076}, "geometry": {"type": "Polygon", "coordinates": [[[28.0250166, -26.1896022], [28.0258021, -26.1895055], [28.0257596, -26.1892273], [28.0254839, -26.1892612], [28.025476, -26.1892094], [28.0252477, -26.1892376], [28.0252541, -26.1892797], [28.0249727, -26.1893144], [28.0250166, -26.1896022]]]}}, {"type": "Feature", "id": "08", "properties": {"name": "Commerce, law, management", "density": 547427.0, "loggers": "WITS_WC_CLM_Building_TRF_1_kWh,WITS_WC_CLM_Building_TRF_2_kWh", "per_unit": 0.6182051896471786}, "geometry": {"type": "Polygon", "coordinates": [[[28.0269545, -26.1893634], [28.0269269, -26.1891544], [28.0259673, -26.1892566], [28.025995, -26.1894656], [28.0269545, -26.1893634]]]}}, {"type": "Feature", "id": "09", "properties": {"name": "Tower of Light", "density": 40903.0, "loggers": "WITS_WC_Tower_of_Lights_Total_kWh", "per_unit": 0.04619223799770771}, "geometry": {"type": "Polygon", "coordinates": [[[28.0258882, -26.1897672], [28.0259313, -26.18977], [28.0259727, -26.1897594], [28.0260069, -26.1897374], [28.0260314, -26.1897055], [28.0260423, -26.1896681], [28.0260382, -26.1896295], [28.0260107, -26.1895845], [28.0259767, -26.1895607], [28.0259356, -26.1895487], [28.0258925, -26.1895501], [28.0258525, -26.1895647], [28.0258272, -26.1895835], [28.0258039, -26.1896161], [28.0257944, -26.1896539], [28.0257999, -26.1896923], [28.0258179, -26.1897245], [28.0258489, -26.1897514], [28.0258882, -26.1897672]]]}}, {"type": "Feature", "id": "010", "properties": {"name": "New Commerce Building", "density": 278628.0, "loggers": "WITS_EC_New_Commerce_Building_kWh", "per_unit": 0.3146531071110884}, "geometry": {"type": "Polygon", "coordinates": [[[28.026276, -26.1896156], [28.0262856, -26.1896908], [28.026243, -26.1896952], [28.0262534, -26.189776], [28.0263021, -26.189771], [28.0263295, -26.189914], [28.0270276, -26.1898394], [28.0270002, -26.189688], [28.0270436, -26.1896835], [28.0270367, -26.1896298], [28.0269903, -26.1896346], [28.0269786, -26.1895432], [28.0268246, -26.1895591], [28.0268205, -26.1895269], [28.0267289, -26.1895364], [28.0267338, -26.1895744], [28.0265186, -26.1895967], [28.0265139, -26.1895602], [28.026427, -26.1895692], [28.0264309, -26.1895996], [28.026276, -26.1896156]]]}}, {"type": "Feature", "id": "011", "properties": {"name": "Old Grandstand", "density": 19728.0, "loggers": "WITS_WC_Old_Grandstand_kWh", "per_unit": 0.022279428568588017}, "geometry": {"type": "Polygon", "coordinates": [[[28.02564, -26.1899736], [28.0256628, -26.1901275], [28.0261569, -26.1900686], [28.0261341, -26.1899146], [28.02564, -26.1899736]]]}}, {"type": "Feature", "id": "012", "properties": {"name": "TW Kambule Mathematical Sciences Building", "density": 885511.0, "loggers": "WITS_WC_Maths_Science_Building_kWh", "per_unit": 1.0}, "geometry": {"type": "Polygon", "coordinates": [[[28.0263396, -26.1899607], [28.0263778, -26.1902333], [28.0266041, -26.1902442], [28.0267489, -26.1907441], [28.0269997, -26.1907247], [28.0269391, -26.1902218], [28.0269391, -26.1901099], [28.0265542, -26.1901147], [28.0265354, -26.190057], [28.0268506, -26.1900185], [28.0268305, -26.1899053], [28.0263396, -26.1899607]]]}}, {"type": "Feature", "id": "013", "properties": {"name": "Wits Science Stadium", "density": 384793.0, "loggers": "WITS_WC_Science_Stadium_TRF_1_kWh,WITS_WC_Science_Stadium_TRF_2_kWh", "per_unit": 0.43454432842710566}, "geometry": {"type": "Polygon", "coordinates": [[[28.0253167, -26.1901645], [28.0252201, -26.1902415], [28.025145, -26.1903522], [28.0251114, -26.1904287], [28.0250923, -26.1905076], [28.025086, -26.1906024], [28.0250978, -26.1906988], [28.0251408, -26.1908093], [28.0251972, -26.1908931], [28.025263, -26.1909588], [28.0253689, -26.1910328], [28.0254619, -26.1910843], [28.025505, -26.190996], [28.025601, -26.1910254], [28.0256757, -26.1910294], [28.0257392, -26.1910275], [28.0263989, -26.1909507], [28.0265447, -26.1909316], [28.0265205, -26.1907395], [28.0265548, -26.1907386], [28.0265402, -26.1906264], [28.0256961, -26.1907216], [28.0256954, -26.1907659], [28.0256278, -26.1907734], [28.0255643, -26.190751], [28.0255082, -26.1906915], [28.0254662, -26.1906142], [28.0254665, -26.1905404], [28.025486, -26.1905051], [28.0255095, -26.1904657], [28.0255483, -26.1904357], [28.0253167, -26.1901645]]]}}, {"type": "Feature", "id": "014", "properties": {"name": "Genmin Laboratory", "density": 32414.0, "loggers": "WITS_WC_Genmin_LAB_kWh", "per_unit": 0.036605386662833785}, "geometry": {"type": "Polygon", "coordinates": [[[28.0256498, -26.1914693], [28.0263222, -26.1913967], [28.0262899, -26.1911908], [28.0262082, -26.1911991], [28.0262013, -26.1911472], [28.0259795, -26.19117], [28.0259849, -26.1912222], [28.0259098, -26.1912331], [28.0259015, -26.1911798], [28.02562, -26.1912147], [28.0256498, -26.1914693]]]}}, {"type": "Feature", "id": "015", "properties": {"name": "CLTD", "density": 42079.0, "loggers": "WITS_WC_CLTD_Building_kWh", "per_unit": 0.04752008512316641}, "geometry": {"type": "Polygon", "coordinates": [[[28.0256016, -26.1921263], [28.0256136, -26.1922372], [28.0258892, -26.1922132], [28.0258772, -26.1921024], [28.0256016, -26.1921263]]]}}, {"type": "Feature", "id": "016", "properties": {"name": "David Webster Hall", "density": 320349.0, "loggers": "WITS_WC_David_Webster_Hall_kWh", "per_unit": 0.3617678668247467}, "geometry": {"type": "Polygon", "coordinates": [[[28.0256602, -26.186779], [28.0257023, -26.1871268], [28.0266456, -26.1870011], [28.0265896, -26.1866491], [28.0256602, -26.186779]]]}}, {"type": "Feature", "id": "017", "properties": {"name": "Barnato Hall", "density": 21509.0, "loggers": "WITS_WC_Barnato_Sub_Residence_A___D_kWh", "per_unit": 0.024290244872883702}, "geometry": {"type": "Polygon", "coordinates": [[[28.0252773, -26.1866826], [28.0244507, -26.1867832], [28.0245114, -26.1872316], [28.0247869, -26.1872064], [28.0247776, -26.187131], [28.0250391, -26.18711], [28.0250485, -26.1871855], [28.025338, -26.1871561], [28.0252773, -26.1866826]]]}}, {"type": "Feature", "id": "018", "properties": {"name": "Convocation Dining Hall", "density": 97811.0, "loggers": "WITS_WC_Convocation_Kitchen_kWh", "per_unit": 0.11045816553017998}, "geometry": {"type": "Polygon", "coordinates": [[[28.0243199, -26.1868083], [28.0240538, -26.1868376], [28.0240771, -26.187022], [28.0239884, -26.1870388], [28.023993, -26.1871645], [28.0243713, -26.18711], [28.0243199, -26.1868083]]]}}, {"type": "Feature", "id": "019", "properties": {"name": "West Campus Village", "density": 179873.0, "loggers": "WITS_WC_Stdnts_Village_Unit_A_kWh,WITS_WC_Stdnts_Village_Unit_B_kWh,WITS_WC_Stdnts_Village_Unit_C_kWh,WITS_WC_Stdnts_Village_Unit_D_kWh,WITS_WC_Stdnts_Village_Unit_E_kWh,WITS_WC_Stdnts_Village_Unit_F_kWh,WITS_WC_Stdnts_Village_Unit_G_kWh,WITS_WC_Stdnts_Village_Unit_H_kWh", "per_unit": 0.20312938789663668}, "geometry": {"type": "Polygon", "coordinates": [[[28.0242219, -26.1873615], [28.02347, -26.1874201], [28.0235914, -26.1877805], [28.024418, -26.187768], [28.0242219, -26.1873615]]]}}, {"type": "Feature", "id": "020", "properties": {"name": "Wits Club", "density": 183589.0, "loggers": "WITS_WC_Club_Minisub_Total_kWh", "per_unit": 0.207325647898847}, "geometry": {"type": "Polygon", "coordinates": [[[28.0255787, -26.1857295], [28.0257061, -26.1858915], [28.0260247, -26.1857009], [28.025961, -26.185631], [28.0258902, -26.1856977], [28.0258052, -26.1855961], [28.0255787, -26.1857295]]]}}, {"type": "Feature", "id": "021", "properties": {"name": "The Barns", "density": 62426.0, "loggers": "WITS_WC_Hall_29B_kWh", "per_unit": 0.07049782205018913}, "geometry": {"type": "Polygon", "coordinates": [[[28.0256389, -26.1861709], [28.0256495, -26.1862694], [28.0259716, -26.1862218], [28.0262618, -26.1859994], [28.0263361, -26.1858184], [28.0262512, -26.1857739], [28.026145, -26.1859899], [28.025922, -26.186136], [28.0256389, -26.1861709]]]}}, {"type": "Feature", "id": "022", "properties": {"name": "Alumni House", "density": 13226.0, "loggers": "WITS_WC_Hall_29C_kWh", "per_unit": 0.014937137314142418}, "geometry": {"type": "Polygon", "coordinates": [[[28.0255717, -26.1858915], [28.0255858, -26.1860471], [28.0256778, -26.1860439], [28.0256672, -26.1858883], [28.0255717, -26.1858915]]]}}, {"type": "Feature", "id": "023", "properties": {"name": "Gym and Squash courts", "density": 122804.0, "loggers": "WITS_WC_Squash_Courts_kWh,WITS_WC_Gymnasium_kWh", "per_unit": 0.1386821514878025}, "geometry": {"type": "Polygon", "coordinates": [[[28.0267821, -26.1864949], [28.0271608, -26.1864504], [28.0270985, -26.1861331], [28.0267232, -26.1861832], [28.0267821, -26.1864949]]]}}, {"type": "Feature", "id": "024", "properties": {"name": "PIMD", "density": 265547.0, "loggers": "WITS_WC_PIMD_Supply_No_1_kWh,WITS_WC_PIMD_Supply_No_2_kWh", "per_unit": 0.29988077202827024}, "geometry": {"type": "Polygon", "coordinates": [[[28.0237883, -26.1884579], [28.0239157, -26.1894646], [28.0247828, -26.189363], [28.0246412, -26.1883499], [28.0237883, -26.1884579]]]}}, {"type": "Feature", "id": "025", "properties": {"name": "PIMD Wash Bay", "density": 257.0, "loggers": "WITS_WC_PIMD_Wash_Bay_kWh", "per_unit": 0.0002908693293561792}, "geometry": {"type": "Polygon", "coordinates": [[[28.0237776, -26.1894837], [28.023767, -26.1894075], [28.0236148, -26.1894297], [28.0236254, -26.1895091], [28.0237776, -26.1894837]]]}}, {"type": "Feature", "id": "026", "properties": {"name": "Sturrock Park", "density": 94816.0, "loggers": "WITS_WC_Sturrock_Park_Main_kWh", "per_unit": 0.10707543503454478}, "geometry": {"type": "Polygon", "coordinates": [[[28.0234768, -26.1932375], [28.0233742, -26.1928913], [28.0231547, -26.1929453], [28.023137, -26.1928818], [28.0234237, -26.1924372], [28.0233105, -26.19238], [28.0229919, -26.1928723], [28.0230344, -26.1929993], [28.0228893, -26.1930469], [28.0229424, -26.1931676], [28.0230804, -26.1931422], [28.0231618, -26.1933328], [28.0234768, -26.1932375]]]}}, {"type": "Feature", "id": "027", "properties": {"name": "DJ Du Plesis", "density": 74473.0, "loggers": "WITS_WC_DJ_du_Plessis_Building_kWh", "per_unit": 0.08410194416790535}, "geometry": {"type": "Polygon", "coordinates": [[[28.0236667, -26.1882365], [28.0236938, -26.1884498], [28.0238063, -26.1884328], [28.0246166, -26.1883302], [28.0246987, -26.1883069], [28.0248185, -26.1882894], [28.0247643, -26.188221], [28.0246964, -26.1881324], [28.024598, -26.1880679], [28.0244951, -26.1880286], [28.0243813, -26.1879974], [28.0243864, -26.188054], [28.023649, -26.1881383], [28.0236667, -26.1882365]]]}}, {"type": "Feature", "id": "028", "properties": {"name": "digs field, rugby", "density": 9648.0, "loggers": "WITS_WC_Dig_Fields_Rugby_kWh", "per_unit": 0.01089621658380502}, "geometry": {"type": "Polygon", "coordinates": [[[28.0238578, -26.1863488], [28.0237421, -26.185367], [28.0230221, -26.1854353], [28.0231378, -26.1864171], [28.0238578, -26.1863488]]]}}, {"type": "Feature", "id": "029", "properties": {"name": "digs field, soccer", "density": 6718.0, "loggers": "WITS_WC_Dig_Fields_Soccer_kWh", "per_unit": 0.0075867151823434216}, "geometry": {"type": "Polygon", "coordinates": [[[28.0239513, -26.185252], [28.0240492, -26.1861824], [28.024768, -26.1861289], [28.0246487, -26.1852094], [28.0239513, -26.185252]]]}}, {"type": "Feature", "id": "030", "properties": {"name": "Claude Vergie House", "density": 1220.0, "loggers": "WITS_WC_Claude_Vergie_House_kWh", "per_unit": 0.0013778968807910236}, "geometry": {"type": "Polygon", "coordinates": [[[28.0236714, -26.1872166], [28.023584, -26.1872294], [28.0235901, -26.1872586], [28.023521, -26.1872677], [28.0235372, -26.1873425], [28.023708, -26.1873133], [28.0236714, -26.1872166]]]}}, {"type": "Feature", "id": "031", "properties": {"name": "Zesti Lemonz", "density": 47096.0, "loggers": "WITS_WC_Village_Zesti_Lemonz_kWh", "per_unit": 0.053185954624805916}, "geometry": {"type": "Polygon", "coordinates": [[[28.0277219, -26.190267], [28.0276904, -26.1902201], [28.0276529, -26.1902022], [28.0276153, -26.1901904], [28.0275711, -26.1901904], [28.0275336, -26.1902022], [28.0274982, -26.190234], [28.0274739, -26.1902796], [28.0274762, -26.190345], [28.027496, -26.1903826], [28.0276106, -26.1903221], [28.0277219, -26.190267]]]}}]}'
        
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
    try:
        f = open("../../tmp/Map/wits-buildings.txt","w")
        f.write(stringVar)
        f.close()
    except:
        print("Could not write to the .txt")
    return

def generateMapData(queryFlask, startDate, endDate):
    loggerList = specifyLoggers()

    url = createQueryUrl(queryFlask, loggerList)

    queryDatabase(url)
    upDateGeoJSON(startDate, endDate)
    return