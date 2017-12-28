# A snoob udp relay server
# This file aim to bypass NAT
# run this on server which have public IP
# 2017-12-12

import socket
from .header import decode
from .logger import getLogger
logger = getLogger('[server]')


class Server:
    def __init__(self, port=10002):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind(('0.0.0.0', port))
        self.__client_address = ()
        logger.info('server start on ' + str(port))

    def start(self):
        while True:
            data, address = self.__sock.recvfrom(4096)
            if data:
                decode_data, decode_address = decode(data)
                if decode_address != 0:
                    self.forword(decode_data, decode_address, address)
                else:
                    if len(self.__client_address) == 0:
                        logger.error('无client!')
                        return
                    else:
                        logger.info('Forword back:\t' + str(address) + '\t->\t' +
                                    str(self.__client_address) + ' || ' + str(data))
                        self.__sock.sendto(data, self.__client_address)

    def forword(self, decode_data, decode_address, address):
        self.__client_address = address
        logger.info('Forword\t' + str(address) + '\t->\t' +
                    str(decode_address) + ' data:' + str(decode_data))
        self.__sock.sendto(decode_data, decode_address)
    def close(self):
        self.__sock.close()


if __name__ == '__main__':
    server = Server()
    server.start()
