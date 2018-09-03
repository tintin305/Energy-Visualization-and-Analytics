from sshtunnel import SSHTunnelForwarder
import socket
import time
import requests
import subprocess
import os
from subprocess import call
import platform

# open ssh tunnel
# server = SSHTunnelForwarder(
#     'tsdb.eie.wits.ac.za',
#     ssh_username="username",
#     ssh_password="password",
#     # remote_bind_address=('127.0.0.1', 4242),
#     remote_bind_address=('127.0.0.1', 4242),
#     local_bind_address=('127.0.0.1',4242)
#     # threaded=True
#     # set_keepalive=1.0
# )

# server.start()

# print(server.local_bind_port)  # show assigned local port
# # work with `SECRET SERVICE` through `server.local_bind_port`.

# # request = b"GET / HTTP/1.1\nHost: wits.ac.za\n\n"
# # s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # s.connect(('127.0.0.1',4242))
# # s.send(request)
# # result = s.recv(10000)
# # while(len(result) > 0):
# #     print('result---')
# #     print(result)
# #     result = s.recv(10000)

# # print("Is Active: %s" % (server.is_active))
# # server.check_tunnels()
# # print(server.tunnel_is_up)

# time.sleep(20)

# server.stop()

bashPath = os.path.join(os.path.dirname(__file__),"../../Python_Scripts/SSHTunnel/")
os.chdir(bashPath)
# os.system("SSHLogin.sh")

def createTunnel():
    # Find the operating system
    operatingSystem = platform.system()
    if operatingSystem is 'Windows':
        # os.system('plink -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242')
        call('putty -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242')
        # rc = call('putty -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242', shell=True)
    if operatingSystem is "Mac":
        print('Mac System')
    if operatingSystem is "Linux":
        call('./SSHLogin.sh')
    return

createTunnel()

# os.chmod('SSHLogin.sh', 0o755)
# # test = call('./SSHLogin.sh', shell=True)

# with open('SSHLogin.sh', 'rb') as file:
#     script = file.read()
# rc = call(script, shell=True)



# resp = requests.get('http://tsdb.eie.wits.ac.za:4242/api/query?start=1y-ago&m=sum:WITS_13_Jubilee_Road_kWh', 
#                     proxies=dict(http='socks5://localhost:4242',
#                                  https='socks5://localhost:4242'))

# print(resp.text)
