from flask import Flask
from flask import render_template
import sys
import os
import random
import subprocess
# from threading import Thread
# from static.Python_Scripts.SSHTunnel.SSHTunnel import createTunnel

# def openTunnel():
#     createTunnel()
    # return

# def flaskServer():
from static.Python_Scripts.GenerateMetrics.MetricsQuery import generateMetrics

from static.Python_Scripts.DatabaseQueryDygraphs.DatabaseQueryDygraphs import generateDygraphsData

from static.Python_Scripts.GenerateHeatMap.GenerateHeatMap import generateHeatMap

from static.Python_Scripts.DataOutages.DataOutages import generateDataOutages

from static.Python_Scripts.SankeyGeneration.DatabaseQuery import generateSankeyData

from static.Python_Scripts.GenerateThreeDimensionalHeatMap.GenerateThreeDimensionalHeatMap import generateThreeDimensionalHeatMap

from static.Python_Scripts.GenerateTreemap.GenerateTreemap import generateTreeMap

from static.Python_Scripts.GeographicRepresentation.generateMaps import generateMapData

from static.Python_Scripts.ShutdownServer.ShutdownServer import shutdown_server

from static.Python_Scripts.GenerateHeatMapData.GenerateHeatMapData import generateHeatMapData

from static.Python_Scripts.GenerateDataOutageData.GenerateDataOutageData import generateDataOutageData

# from static.Python_Scripts.SSHTunnel.SSHTunnel import createTunnel

app = Flask(__name__, static_url_path='')
# process = subprocess.Popen(createTunnel())

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/Maps/")
def map():
    queryFlask = {'aggregator' : 'avg', 'downsample' : '0all-sum', 'rate': 'false', 'metric': 'WITS_EC_Matrix_Main_Incomer_kWh', 'tagKey': 'DataLoggerName', 'tagValue': 'WITS_EC_Matrix_Main_Incomer_kWh', 'host': 'tsdb.eie.wits.ac.za', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': '2018-01-01', 'endDate': "2018-06-30"}
    generateMapData(queryFlask)
    refreshCache = str(random.getrandbits(32))
    return render_template("/MapShow.html", refreshCache=refreshCache)


    # generateMapData()
    # return render_template("MapShow.html")

@app.route("/DygraphsShow/")
def DygraphsShow():
    refreshCache = str(random.getrandbits(32))
    return render_template("DygraphsShow.html", refreshCache=refreshCache)

@app.route("/HeatMapConfig/")
def heatMapConfig():
    metricsParams = { 'host': 'tsdb.eie.wits.ac.za', 'port': 4242}
    metricsList = generateMetrics(metricsParams)
    refreshCache = str(random.getrandbits(32))
    return render_template("HeatMapConfig.html", refreshCache=refreshCache, buttons=metricsList)

@app.route("/HeatMapConfig/<DataloggerName>/<startDate>/<endDate>/<aggregator>/<downsamplingMagnitude>/<timeDownsamplingRange>/<downsamplingType>/")
def getHeatMapData(DataloggerName, startDate, endDate, aggregator, downsamplingMagnitude, timeDownsamplingRange, downsamplingType):
    
    requestedSettings = {'aggregator': aggregator, 'downsamplingMagnitude': downsamplingMagnitude, 'timeDownsamplingRange': timeDownsamplingRange, 'downsamplingType': downsamplingType, 'rate': 'false', 'metric': DataloggerName, 'tagKey': 'DataLoggerName', 'tagValue': DataloggerName,
        'host': 'tsdb.eie.wits.ac.za', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': startDate, 'endDate': endDate}
    generateHeatMapData(requestedSettings)

    # In order to get the Dygraphs data to get refreshed (force the browser to refresh it's cache)
    refreshCache = str(random.getrandbits(32))
    return render_template("/HeatMapShow.html", refreshCache=refreshCache)

@app.route("/DataOutageConfig/<DataloggerName>/<startDate>/<endDate>/<aggregator>/<downsamplingMagnitude>/<timeDownsamplingRange>/<downsamplingType>/")
def getDataOutageData(DataloggerName, startDate, endDate, aggregator, downsamplingMagnitude, timeDownsamplingRange, downsamplingType):
    
    requestedSettings = {'aggregator': aggregator, 'downsamplingMagnitude': downsamplingMagnitude, 'timeDownsamplingRange': timeDownsamplingRange, 'downsamplingType': downsamplingType, 'rate': 'false', 'metric': DataloggerName, 'tagKey': 'DataOutage', 'tagValue': False,
        'host': 'tsdb.eie.wits.ac.za', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': startDate, 'endDate': endDate}
    generateDataOutageData(requestedSettings)

    # In order to get the Dygraphs data to get refreshed (force the browser to refresh it's cache)
    refreshCache = str(random.getrandbits(32))
    return render_template("/DataOutages.html", refreshCache=refreshCache)

@app.route("/HeatMaps/")
def heatMapShow():
    # generateHeatMap()
    refreshCache = str(random.getrandbits(32))
    return render_template("HeatMapShow.html", refreshCache=refreshCache)

@app.route("/DataOutages/")
def dataOutages():
    # generateDataOutages()
    refreshCache = str(random.getrandbits(32))
    return render_template("/DataOutages.html", refreshCache=refreshCache)


@app.route("/ThreeDimensionalView/")
def threeDimensionalView():
    generateThreeDimensionalHeatMap()
    refreshCache = str(random.getrandbits(32))
    return render_template("/ThreeDimensionalViewShow.html", refreshCache=refreshCache)

@app.route("/SankeyConfig/")
def sankeyConfig():
    return render_template("/SankeyConfig.html")
    
@app.route("/TreeMapShow/")
def treeMap():
    refreshCache = str(random.getrandbits(32))
    return render_template("TreeMap.html", refreshCache=refreshCache)

@app.route("/TreeMapConfig/<startDate>/<endDate>")
def treeMapQuery(startDate, endDate):
    metricsParams = { 'host': 'tsdb.eie.wits.ac.za', 'port': 4242}
    queryDetails = {'aggregator' : 'avg', 'downsample' : '0all-sum', 'rate': 'false', 'metric': 'WITS_EC_Matrix_Main_Incomer_kWh', 'tagKey': 'DataLoggerName', 'tagValue': 'WITS_EC_Matrix_Main_Incomer_kWh', 'host': 'tsdb.eie.wits.ac.za', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': startDate, 'endDate': endDate}
    generateMetrics(metricsParams)
    generateTreeMap(queryDetails)
    refreshCache = str(random.getrandbits(32))
    return render_template("TreeMap.html", refreshCache=refreshCache)

@app.route("/TreeMapConfig/")
def treeMapConfig():
    refreshCache = str(random.getrandbits(32))
    return render_template("TreeMapConfig.html", refreshCache=refreshCache)

@app.route("/SankeyDiagram/")
def sankeyDiagram():
    # queryFlask = {'aggregator' : 'avg', 'downsample' : '0all-sum', 'rate': 'false', 'metric': 'WITS_EC_Matrix_Main_Incomer_kWh', 'tagKey': 'DataLoggerName', 'tagValue': 'WITS_EC_Matrix_Main_Incomer_kWh', 'host': 'tsdb.eie.wits.ac.za', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': '2018/03/01-00:00', 'endDate': '2018/06/01-23:30'}
    # loggersReq = 'Matrix'
    # generateSankeyData(queryFlask, loggersReq)
    refreshCache = str(random.getrandbits(32))
    return render_template("/SankeyDiagram.html", refreshCache=refreshCache)

@app.route("/metrics/")
def metrics():
    # http://localhost:4242/api/suggest?type=metrics&max=10000s
    metricsParams = { 'host': 'tsdb.eie.wits.ac.za', 'port': 4242}
    metricsList = generateMetrics(metricsParams)
    return render_template("/loggerList.html", buttons = metricsList)

@app.route("/profiles/<DataloggerName>/<startDate>/<endDate>/<aggregator>/<downsamplingMagnitude>/<timeDownsamplingRange>/<downsamplingType>/")
def getData(DataloggerName, startDate, endDate, aggregator, downsamplingMagnitude, timeDownsamplingRange, downsamplingType):
    
    requestedSettings = {'aggregator': aggregator, 'downsamplingMagnitude': downsamplingMagnitude, 'timeDownsamplingRange': timeDownsamplingRange, 'downsamplingType': downsamplingType, 'rate': 'false', 'metric': DataloggerName, 'tagKey': 'DataLoggerName', 'tagValue': DataloggerName,
        'host': 'tsdb.eie.wits.ac.za', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': startDate, 'endDate': endDate}
    generateDygraphsData(requestedSettings)

    # In order to get the Dygraphs data to get refreshed (force the browser to refresh it's cache)
    refreshCache = str(random.getrandbits(32))
    return render_template("/DygraphsShow.html", refreshCache=refreshCache)

@app.route("/sankey/<loggersReq>/<startDate>/<endDate>")
def getSankey(loggersReq, startDate, endDate):
    print(loggersReq)
    queryFlask = {'aggregator' : 'avg', 'downsample' : '0all-sum', 'rate': 'false', 'metric': 'WITS_EC_Matrix_Main_Incomer_kWh', 'tagKey': 'DataLoggerName', 'tagValue': 'WITS_EC_Matrix_Main_Incomer_kWh', 'host': 'tsdb.eie.wits.ac.za', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': startDate, 'endDate': endDate}
    generateSankeyData(queryFlask, loggersReq)
    refreshCache = str(random.getrandbits(32))
    return render_template("/SankeyDiagram.html", refreshCache=refreshCache)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=3000,debug=True, threaded=False)
    # app.run(host='127.0.0.1',port=3000,debug=True, threaded=True)
# return

# Thread(target = flaskServer).start() 
# Thread(target = openTunnel).start()