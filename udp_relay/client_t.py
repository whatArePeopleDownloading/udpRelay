from client import client

c = client(('0.0.0.0', 10002))
c.sendto(b'hello',('127.0.0.1', 10000))

while True:
    data, address = c.recvfrom(4096)
    if data:
        print(str(address))
