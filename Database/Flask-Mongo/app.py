from flask import Flask
from flask import render_template
import pandas as pd
import json

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def DygraphsShow():
    return render_template("DygraphsShow.html")

@app.route("/TreemapShow/")
def treemap():
    return render_template("Treemap.html")

@app.route("/DygraphsShow/")
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
    return render_template("/SankeyDiagram.html")

@app.route("/metrics/")
def metrics():
    return render_template("/logger_list.html")


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