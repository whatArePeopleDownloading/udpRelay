import socket
import getport
import threading



class client:
    def __init__(self, relayServer):
        self.__realyServer = relayServer
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind(('0.0.0.0', getport.get()))
        self.__FLAG = 0x7f7f
        threading.Thread(target=self.recvfrom).start()

    def sendto(self, data, address):
        """
   extera header for client (8 Bytes)
+------+-------------------------------+
| flag |      Ip address(v4)  | port   |
|2 byte|        4 bytes       | 2 bytes|
+--------------------------------------+

        """
        flag = self.__FLAG.to_bytes(2, 'big')
        ip = self.ip2bytes(address[0])
        port = int(address[1]).to_bytes(2, 'big')
        data = flag + ip + port + data
        self.__sock.sendto(data, self.__realyServer)

    def recvfrom(self,size=4096):
            return self.__sock.recvfrom(size)



    @staticmethod
    def ip2bytes(ipaddress):
        ipadd = ipaddress.split('.')
        assert len(ipadd) == 4
        ipadd = list(map(int, ipadd))
        ipNum = int.from_bytes(ipadd, 'big')
        return ipNum.to_bytes(4, 'big')
