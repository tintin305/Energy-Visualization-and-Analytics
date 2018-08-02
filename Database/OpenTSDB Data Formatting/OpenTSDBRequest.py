import numpy as np
import pandas as pd
import json
import requests

#  /usr/share/opentsdb/bin/tsdb query 1y-go  sum LoggerName

url="http://127.0.0.1:4242/api/query?start=16h-ago&m=sum:WITS_EC_Bernard_Price_Sub_Total_kWh"

r = requests.get(url)
print(r.text)
