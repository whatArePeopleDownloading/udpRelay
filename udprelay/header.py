import socket
import ipaddress
from .logger import getLogger
logger = getLogger('[udpRelayHeader]')

"""
   extera header for client (8 Bytes)
+------+-------------------------------+
| flag |      Ip address(v4)  | port   |
|2 byte|        4 bytes       | 2 bytes|
+--------------------------------------+
"""
def getIP(address):
    try:
        ipaddress.ip_address(address)
    except ValueError:
        val = socket.gethostbyname(address)
        # logger.info(address + '->' + val)
        return val
    return address
AUTH_FLAG=0x7f7f
# encode extera udp header
def encode(data, address):

    flag = AUTH_FLAG.to_bytes(2, 'big')
    ip = getIP(address[0])

    Bip = ip2bytes(ip)
    port = int(address[1]).to_bytes(2, 'big')
    return flag + Bip + port + data


# decode udp header
# return (address, data)
# return (0,0) if flag is wrong
def decode(data):
    if int.from_bytes(data[:2], 'big') == AUTH_FLAG:
        ip = byte2IP(data[2:6])
        port = byte2Int(data[6:8])
        data = data[8:]
        return data,(ip,port)
    return 0, 0

def byte2IP(bytes):

    assert len(bytes) == 4
    # ip=''
    # for i in bytes:
    #     ip += str(i)
    # return ip
    return '.'.join(map(str, bytes))

def byte2Int(bytes):
    return int.from_bytes(bytes, 'big')

def ip2bytes(ipaddress):
    ipadd = ipaddress.split('.')
    assert len(ipadd) == 4
    ipadd = list(map(int, ipadd))
    ipNum = int.from_bytes(ipadd, 'big')
    return ipNum.to_bytes(4, 'big')


