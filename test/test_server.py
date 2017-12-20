from multiprocessing import Process
from udp_relay.server import server
from udp_relay.client import client
import time
import os
import pytest

c = client(('0.0.0.0', 10002))
data = ''
address = ''
def startEchoServer():
    os.system('python test/udp_echo_server.py')

def startRelayServer():
    s =server()
    s.start()

def receive():
    while True:
        data, address = c.recvfrom(4096)



def test_client():
    flaga = Process(target=startEchoServer, name='echoServer')
    flagb = Process(target=startRelayServer, name='relayServer')
    flagc = Process(target=receive, name='receive')
    flaga.start()
    print('1')
    flagb.start()
    print('2')
    flagc.start()

    print('123')
    c.sendto(b'hello', ('127.0.0.1', 10000))
    time.sleep(1000)
    assert data == b'hello'
    assert address == ('127.0.0.1', 10000)


    flaga.terminate()
    flagb.terminate()
    flagc.terminate()

if __name__ == '__main__':
    import sys
    sys.path.append("..")
    test_client()
