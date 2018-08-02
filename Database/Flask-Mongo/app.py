from flask import Flask
from flask import render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/D3RadialHeatMap")
def index2():
    return render_template("D3RadialHeatMap.ejs")

@app.route("/Test")
def index3():
    df = pd.read_csv('data.csv').drop('Open', axis=1)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("Test.ejs", data=data)


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)