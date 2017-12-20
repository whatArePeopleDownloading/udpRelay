from udp_relay import client,server
# import pytest


def test_ip2bytes():
    import ipaddress
    ip = "192.168.0.1"
    bytesIP = ipaddress.IPv4Address(ip).packed

    assert client.ip2bytes(ip) == bytesIP

