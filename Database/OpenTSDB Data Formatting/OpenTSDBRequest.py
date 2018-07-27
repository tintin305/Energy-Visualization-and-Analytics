import numpy as np
import pandas as pd
import json
import requests


url="http://127.0.0.1:4242/api/query?start=16h-ago&m=sum:WITS.EC.Bernard.Price.Sub.Total_kWh"

r = requests.get(url)
print(r.text)
