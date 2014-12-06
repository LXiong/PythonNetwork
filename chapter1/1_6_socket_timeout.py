#! /usr/bin/python

import socket

def get_socket_timeout():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "Default socket timeout: %s" % s.gettimeout()
    s.settimeout(50)
    print "Current socket timeout: %s" % s.gettimeout()

if __name__ == '__main__':
    get_socket_timeout()
