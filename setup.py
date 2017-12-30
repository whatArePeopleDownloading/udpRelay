import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "udprelay",
    version = "0.2.1",
    author = "meta Z",
    author_email = "zycode277@gmail.com",
    description = "another simple udp realy server and client",
    license = "MIT",
    packages = find_packages(exclude=['docs', 'test']),
    install_requires=['coloredlogs', 'getport'],
    long_description=read('README.rst'),
    url='https://github.com/whatArePeopleDownloading/udpRelay'
)
