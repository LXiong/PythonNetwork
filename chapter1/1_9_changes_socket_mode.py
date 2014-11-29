#! /usr/bin/python

import socket

def test_socket_modes():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setblocking(0)
    sock.settimeout(1)
    try:
        sock.bind(('127.0.0.1',8080))
        socket_address = sock.getsockname()
        print "Trivial Server launched on socket:%s" % str(socket_address)
        while(1):
            sock.listen(1)
    except socket.error,e:
        print "Error:%s" % e

if __name__ == '__main__':
    test_socket_modes()
        
