# A snoob udp relay server
# This file aim to bypass NAT
# run this on server which have public IP
# 2017-12-12

import logging
import socket
logger = logging.getLogger('relay-server')
logging.basicConfig(filename='udp_relay_server.log', level='DEBUG')



class server:
    def __init__(self, port=10002):
        self.__FLAG = 0x7f7f    # 以此开头的流量讲被标志为转发流量
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind(('0.0.0.0', port))
        self.__client_address = ()
        logger.info('server start on ' + str(port))

    def start(self):
        while True:
            print('test')
            data, address = self.__sock.recvfrom(4096)
            logger.info('收到消息!')
            if data:
                if int.from_bytes(data[:2], 'big') == self.__FLAG:
                    self.__client_address = address
                    ip = data[2:6]
                    port = data[6:8]
                    data = data[8:]
                    relay = (self.byte2IP(ip), self.byte2Int(port))
                    logger.info('转发来自 ' + str(address) + '的流量:' + str(data))
                    self.__sock.sendto(data, relay)
                else:
                    if len(self.__client_address) == 0:
                        logger.error('无client!')
                        return
                    else:
                        logger.info(str(address) + ' -> ' + str(self.__client_address) + ' || ' + str(data))
                        self.__sock.sendto(data, self.__client_address)



    @staticmethod
    def byte2Int(bytes):
        return int.from_bytes(bytes, 'big')

    @staticmethod
    def byte2IP(bytes):

        assert len(bytes) == 4
        # ip=''
        # for i in bytes:
        #     ip += str(i)
        # return ip
        return '.'.join(map(str, bytes))

    def close(self):
        self.__sock.close()

if __name__ == '__main__':
    server = server()
    server.start()
