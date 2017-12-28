import socket
from header import encode
import getport
import threading



class client:
    def __init__(self, relayServer):
        self.__realyServer = relayServer
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind(('0.0.0.0', getport.get()))
        threading.Thread(target=self.recvfrom).start()
    def sendto(self, data, address):
        data = encode(data, address)
        self.__sock.sendto(data, self.__realyServer)

    def recvfrom(self,size=4096):
            return self.__sock.recvfrom(size)




