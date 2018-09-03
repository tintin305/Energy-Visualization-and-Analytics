from sshtunnel import SSHTunnelForwarder
import socket
import time
import requests
import subprocess
import os
from subprocess import call
import platform

def createTunnel():
    # Find the operating system
    operatingSystem = platform.system()
    if operatingSystem is 'Windows':
        # os.system('plink -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242')
        call('putty -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242')
        # rc = call('putty -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242', shell=True)
    if operatingSystem is "Mac":
        # Make sure that sshpass is installed
        call('sshpass -p password ssh username@tsdb.eie.wits.ac.za -D 4242')
    if operatingSystem is "Linux":
        # Make sure that sshpass is installed
        call('sshpass -p password ssh username@tsdb.eie.wits.ac.za -D 4242')
    return

createTunnel()