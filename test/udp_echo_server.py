import socket
import sys
import time

PORT = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', PORT)
print('UDP echo server start on port :  ' + str(PORT) + '\n')
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)

    print('[' + str(time.time()) + ']received %s bytes from %s' % (len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
