from sshtunnel import SSHTunnelForwarder
import socket
import time
import requests
import subprocess
import os
from subprocess import call
import platform

resp = requests.get('http://tsdb.eie.wits.ac.za:4242/api/query?start=1y-ago&m=sum:WITS_13_Jubilee_Road_kWh', 
                    proxies=dict(http='socks5://localhost:4242',
                                 https='socks5://localhost:4242'))

print(resp.text)
