#! /usr/bin/python

import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80,21,25]:
        print "Port: %s => Service name: %s" % (
                port,socket.getservbyport(port,protocolname)) 

if __name__ == '__main__':
    find_service_name()
