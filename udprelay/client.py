import socket
import getport
import threading
import logging
import sys
from .header import encode
from .logger import getLogger
logger = getLogger('[client]')
class Client:
    def __init__(self, relayServer, logger_level=logging.DEBUG):
        self.checkaddress(relayServer)
        self.__realyServer = relayServer
        logger.setLevel(logger_level)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = getport.get()
        self.__sock.bind(('0.0.0.0', port))
        self.recvfrom = self.__sock.recvfrom
        logger.info('client bind on ' + str(port))
    def sendto(self, data, address):
        self.checkaddress(address)
        logger.debug('forword data to ' + str(address[0]) + ':' + str(address[1]))
        data = encode(data, address)
        # logger.debug(data)
        self.__sock.sendto(data, self.__realyServer)
    @staticmethod
    def checkaddress(address):
        assert address[0] != None
        assert isinstance(address[1], int)

# if __name__ == '__main__':


