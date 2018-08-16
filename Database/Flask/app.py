from flask import Flask
from flask import render_template
import pandas as pd
import json
import sys
import random


from static.Python_Scripts.SankeyGeneration.DatabaseQuery import generateSankeyData
from static.Python_Scripts.GenerateMetrics.MetricsQuery import generateMetrics
from static.Python_Scripts.DatabaseQueryDygraphs.DatabaseQueryDygraphs import generateDygraphsData
from static.Python_Scripts.GenerateHeatMap.GenerateHeatMap import generateHeatMap
from static.Python_Scripts.DataOutages.DataOutages import generateDataOutages
from static.Python_Scripts.GenerateThreeDimensionalHeatMap.GenerateThreeDimensionalHeatMap import generateThreeDimensionalHeatMap

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/DygraphsShow/")
def DygraphsShow():
    return render_template("DygraphsShow.html")

@app.route("/TreemapShow/")
def treemap():
    return render_template("Treemap.html")

@app.route("/HeatMaps/")
def heatMapShow():
    generateHeatMap()
    return render_template("HeatMapShow.html")

@app.route("/ThreeDimensionalView/")
def threeDimensionalView():
    generateThreeDimensionalHeatMap()
    return render_template("/ThreeDimensionalViewShow.html")

@app.route("/DataOutages/")
def dataOutages():
    generateDataOutages()
    return render_template("/DataOutages.html")

@app.route("/SankeyDiagram/")
def sankeyDiagram():
    queryFlask = {'aggregator' : 'avg', 'downsample' : '0all-sum', 'rate': 'false', 'metric': 'WITS_EC_Matrix_Main_Incomer_kWh', 'tagKey': 'DataLoggerName', 'tagValue': 'WITS_EC_Matrix_Main_Incomer_kWh', 'host': 'localhost', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': '2018/03/01-00:00', 'endDate': '2018/06/01-23:30'}
    generateSankeyData(queryFlask)
    return render_template("/SankeyDiagram.html")

@app.route("/metrics/")
def metrics():
    # http://localhost:4242/api/suggest?type=metrics&max=10000s
    metricsParams = { 'host': 'localhost', 'port': 4242}
    metricsList = generateMetrics(metricsParams)
    return render_template("/loggerList.html", buttons = metricsList)
 
@app.route("/profiles/<DataloggerName>/<startDate>/<endDate>")
def getData(DataloggerName, startDate, endDate):
    
    requestedSettings = {'aggregator': 'sum', 'downsample': '5ms-avg', 'rate': 'false', 'metric': DataloggerName, 'tagKey': 'DataLoggerName', 'tagValue': DataloggerName,
        'host': 'localhost', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': startDate, 'endDate': endDate}
    generateDygraphsData(requestedSettings)

    # In order to get the Dygraphs data to get refreshed (force the browser to refresh it's cache)
    csvVersion = str(random.getrandbits(32))
    return render_template("/DygraphsShow.html", csvVersion=csvVersion)



if __name__ == "__main__":
    app.run(host='127.0.0.1',port=3000,debug=True)