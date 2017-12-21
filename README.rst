# A simple Udp relay server & client
============================================================


.. image:: https://travis-ci.org/whatArePeopleDownloading/udp_relay.svg?branch=master
    :target: https://travis-ci.org/whatArePeopleDownloading/udp_relay

.. code:: python

    extera header for client (8 Bytes)
    +------+-------------------------------+
    | flag |      Ip address(v4)  | port   |
    |2 byte|        4 bytes       | 2 bytes|
    +--------------------------------------+
