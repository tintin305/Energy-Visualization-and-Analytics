from sshtunnel import SSHTunnelForwarder
import socket
import time
# open ssh tunnel
server = SSHTunnelForwarder(
    'tsdb.eie.wits.ac.za',
    ssh_username="username",
    ssh_password="password",
    remote_bind_address=('127.0.0.1', 22)
)

server.start()

print('local port:', server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 8080
s.connect(('127.0.0.1', server.local_bind_port))
s.send(b'GET / HTTP/1.0 \r\n\r\n')
print(s.recv(1000))

time.sleep(20)
s.close()

server.stop()