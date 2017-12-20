# A snoob udp relay server
# This file aim to bypass NAT
# run this on server which have public IP
# 2017-12-12

import logging
import socket
from .udp_header import decode
logger = logging.getLogger('relay-server')
logging.basicConfig(filename='udp_relay_server.log', level='DEBUG')



class server:
    def __init__(self, port=10002):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind(('0.0.0.0', port))
        self.__client_address = ()
        logger.info('server start on ' + str(port))

    def start(self):
        while True:
            data, address = self.__sock.recvfrom(4096)
            logger.info('收到消息!')
            if data:
                decode_data, decode_address = decode(data)
                if decode_address != 0:
                    logger.info('转发来自 ' + str(decode_address) + '的流量:' + str(decode_data))
                    self.__sock.sendto(decode_data, decode_address)
                else:
                    if len(self.__client_address) == 0:
                        logger.error('无client!')
                        return
                    else:
                        logger.info(str(address) + ' -> ' + str(self.__client_address) + ' || ' + str(data))
                        self.__sock.sendto(data, self.__client_address)







    def close(self):
        self.__sock.close()

if __name__ == '__main__':
    server = server()
    server.start()
