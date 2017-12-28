from udprelay.header import *

def test_main():
    address = ('192.168.0.2', 1092)
    data = b'asdlfja;lksjfO(*)*#(*$)@#&$)@#(*$LJDSJF'
    encodeData = encode(data, address)
    d, a = decode(encodeData)
    assert a == address
    assert d == data
