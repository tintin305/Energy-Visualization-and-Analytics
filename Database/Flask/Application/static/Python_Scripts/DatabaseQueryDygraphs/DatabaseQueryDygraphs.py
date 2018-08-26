# import pandas as pd
# import json
# import requests
# import os
# import socket
# import errno

# def saveQueryDetails(requestedSettings):
#     tmpPath = os.path.join(os.path.dirname(__file__), "../../tmp")
#     os.chdir(tmpPath)
#     directory = 'Dygraphs'
#     try:
#         os.makedirs(directory)
#     except OSError as e:
#         if e.errno != errno.EEXIST:
#             raise
#     txtPath = os.path.join(os.path.dirname(__file__), "../../tmp/Dygraphs")
#     os.chdir(txtPath)
#     with open('queryDetails.txt','w') as write_file:
#         json.dump(requestedSettings, write_file)
#     return

# def saveURL(url):
#     txtPath = os.path.join(os.path.dirname(__file__), "../../tmp/Dygraphs")
#     os.chdir(txtPath)
#     f = open('url.txt','w')
#     f.write(url)
#     f.close()
#     return

# def createQueryUrl(requestedSettings):
#     # Get the details out of the object
#     aggregator = requestedSettings['aggregator']
#     downsamplingMagnitude = requestedSettings['downsamplingMagnitude']
#     timeDownsamplingRange = requestedSettings['timeDownsamplingRange']
#     downsamplingType = requestedSettings['downsamplingType']
#     tagKey = requestedSettings['tagKey']
#     tagValue = requestedSettings['tagValue']
#     metric = requestedSettings['metric']
#     host = requestedSettings['host']
#     port = requestedSettings['port']
#     ms = requestedSettings['ms']
#     arrays = requestedSettings['arrays']
#     tsuids = requestedSettings['tsuids']
#     annotations = requestedSettings['annotations']
#     startDate = requestedSettings['startDate']
#     endDate = requestedSettings['endDate']

#     # Format the Dates
#     startDate = dateFormatting(startDate)
#     endDate = dateFormatting(endDate)

#     # Create URL
#     url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate + '&m=' + aggregator + ':' + str(downsamplingMagnitude) + str(timeDownsamplingRange) + '-' + downsamplingType + ':' + metric + '{' + tagKey + '=' + tagValue + '}'

#     return url

# def dateFormatting(date):
#     formattedDate = date.replace('-', '/')
#     return formattedDate

# def queryDatabase(url):
#     data = requests.get(url, proxies=dict(http='socks5://localhost:4242', https='socks5://localhost:4242'))
#     test = data.text
#     return test


# def writeDataToCSV(url, queryData):
#     data = requests.get(url, proxies=dict(http='socks5://localhost:4242', https='socks5://localhost:4242'))
#     test = data.json()
#     csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/Dygraphs")
#     os.chdir(csvPath)
#     with open('pythonData.csv','w') as write_file:
#         json.dump(test, write_file)    
#     return

# def extractData(queryData):
#     queryData = json.loads(queryData[1:-1])
#     dataArray = queryData['dps']

#     header = 'Timestamp,' +  str(queryData['metric'] + '\n')

#     data = str(dataArray)[1:-1]
#     data = data.strip('[')
#     data = data.replace('], [', '\n')
#     data = data.strip(']')

#     csvPath = os.path.join(os.path.dirname(__file__), "../../tmp/Dygraphs")
#     os.chdir(csvPath)
#     f = open('temp.csv','w')
#     f.write(header)
#     f.write(data)
#     f.close()
#     return

# def generateDygraphsData(requestedSettings):
#     saveQueryDetails(requestedSettings)

#     url = createQueryUrl(requestedSettings)

#     saveURL(url)

#     queryData = queryDatabase(url)

#     writeDataToCSV(url, queryData)

#     extractData(queryData)
#     return

import pandas as pd
import json
import requests
import os
import socket
import errno

def createFolder():
    tmpPath = os.path.join(os.path.dirname(__file__), '../../tmp/')
    os.chdir(tmpPath)
    directory = 'Dygraphs'
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return
    
def saveQueryDetails(requestedSettings):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Dygraphs/")
    os.chdir(csvPath)
    with open('queryDetails.txt','w') as write_file:
        json.dump(requestedSettings, write_file)
    return

def saveURL(url):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Dygraphs/")
    os.chdir(csvPath)
    f = open('url.txt','w')
    f.write(url)
    f.close()
    return

def createQueryUrl(requestedSettings, isDataOutage):
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
    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate + '&m=' + aggregator + ':' + str(downsamplingMagnitude) + str(timeDownsamplingRange) + '-' + downsamplingType + ':' + metric + '{' + 'DataOutage' + '=' + str(isDataOutage) + '}'

    return url

def dateFormatting(date):
    formattedDate = date.replace('-', '/')

    return formattedDate

def queryDatabase(url):
    data = requests.get(url, proxies=dict(http='socks5://localhost:4242', https='socks5://localhost:4242'))
    test = data.text
    return test


def writeDataToCSV(queryData):
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Dygraphs/")
    os.chdir(csvPath)
    with open('pythonData.csv','w') as write_file:
        json.dump(queryData, write_file)    
    return

def extractData(queryData):
    queryData = json.loads(queryData[1:-1])
    dataArray = queryData['dps']
    # if queryData['DataOutage'] is False:


    header = 'Timestamp,' +  str(queryData['metric'] + '\n')

    data = str(dataArray)[1:-1]
    data = data.strip('[')
    data = data.replace('], [', '\n')
    data = data.strip(']')

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Dygraphs/")
    os.chdir(csvPath)
    f = open('tempData.csv','w')
    f.write(header)
    f.write(data)
    f.close()

def extractDataOutage(queryData):
    queryData = json.loads(queryData[1:-1])
    dataArray = queryData['dps']

    header = 'Timestamp,' +  str(queryData['metric'] + '\n')

    data = str(dataArray)[1:-1]
    data = data.strip('[')
    data = data.replace('], [', '\n')
    data = data.strip(']')
    # data = data.replace('0.0', '-1')

    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Dygraphs/")
    os.chdir(csvPath)
    f = open('tempDataOutage.csv','w')
    f.write(header)
    f.write(data)
    f.close()

def concatCSV():
    csvPath = os.path.join(os.path.dirname(__file__),"../../tmp/Dygraphs/")
    os.chdir(csvPath)

    dataOutage = pd.read_csv('tempDataOutage.csv', sep=',')
    data = pd.read_csv('tempData.csv', sep=',')

    concatList = [dataOutage, data]
    
    completeData = pd.concat(concatList)
    sortedData = completeData.sort_values(by=['Timestamp'])
    sortedData.to_csv('temp.csv', sep=',', index=False)
    return

def generateDygraphsData(requestedSettings):

    createFolder()
    # Save query details to a text file (used for testing)
    saveQueryDetails(requestedSettings)

    urlDataOutage = createQueryUrl(requestedSettings, True)
    urlData = createQueryUrl(requestedSettings, False)

    saveURL(urlDataOutage)

    queryDataOutage = queryDatabase(urlDataOutage)
    queryData = queryDatabase(urlData)

    # writeDataToCSV(queryDataOutage)
    # writeDataToCSV(queryData)

    # Write to two separate csv files
    extractData(queryData)
    extractDataOutage(queryDataOutage)

    # Concatenate the two csv files
    concatCSV()
