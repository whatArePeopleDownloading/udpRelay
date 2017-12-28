import socket
import getport
import threading
import logging
import sys
from .header import encode
from .logger import logger

class Client:
    def __init__(self, relayServer):
        self.__realyServer = relayServer
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = getport.get()
        self.__sock.bind(('0.0.0.0', port))
        logger.info('client bind on ' + str(port))
        threading.Thread(target=self.recvfrom).start()
    def sendto(self, data, address):
        logging.debug('sending data to ' + str(address[0]) + ':' + str(address[1]))
        data = encode(data, address)
        logger.debug(data)
        self.__sock.sendto(data, self.__realyServer)

    def recvfrom(self,size=4096):
            return self.__sock.recvfrom(size)

if __name__ == '__main__':

    testServer = ('127.0.0.1', 10002)
    c = Client(testServer)
    c.sendto(b'hello', testServer)
    data, address = c.recvfrom(4096)
    print('receve:' + str(data))

