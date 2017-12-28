from udprelay import Server, Client
import getport
import pytest
import threading
PORT = getport.get()
server = Server(PORT)
@pytest.mark.timeout(4)
def test_client():
    threading.Thread(target = start_server).start()
    serverAddress = ('127.0.0.1', PORT)
    payload = b'hello 123daslfjals;dkj'

    client = Client(serverAddress)
    client.sendto(payload, serverAddress)
    while True:
        data, address = client.recvfrom(4096)
        if data:
            assert data == payload
            assert address == address
            break
    server.close()
def start_server():
    server.start()

