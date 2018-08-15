from flask import Flask
from flask import render_template
import pandas as pd
import json
import sys


# Importing Database Queries
# sys.path.append('/static/Python_Scripts/SankeyGeneration')
# import DatabaseQuery
from static.Python_Scripts.SankeyGeneration.DatabaseQuery import generateSankeyData
from static.Python_Scripts.GenerateMetrics.DatabaseQuery import generateMetrics

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
    return render_template("HeatMapShow.html")

@app.route("/ThreeDimensionalView/")
def threeDimensionalView():
    return render_template("/ThreeDimensionalViewShow.html")

@app.route("/DataOutages/")
def dataOutages():
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
    generateMetrics(metricsParams)
    return render_template("/logger_list.ejs")
    # return app.send_static_file('./templates/logger_list.html')

# @app.route("/profiles/<DataloggerName>/<startDate>/<endDate>")
# def getData(DataloggerName, startDate, endDate):

# @app.route("/Test")
# def index3():
#     df = pd.read_csv('data.csv').drop('Open', axis=1)
#     chart_data = df.to_dict(orient='records')
#     chart_data = json.dumps(chart_data, indent=2)
#     data = {'chart_data': chart_data}
#     return render_template("Test.ejs", data=data)


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=3000,debug=True)