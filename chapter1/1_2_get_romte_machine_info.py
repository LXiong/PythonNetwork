#! /usr/bin/python

import socket

def get_remote_machine_info():
    remote_host = 'www.baidu.com'
    try:
        print "IP adress: %s" % socket.gethostbyname(remote_host)
    except socket.error,e:
        print "%s:%s" % (remote_host,e)

if __name__ == '__main__':
    get_remote_machine_info()
