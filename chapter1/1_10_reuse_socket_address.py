#! /usr/bin/python

import socket

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print "Old sock state: %s" %old_state

    # Set sock reuseaddress
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print 'New sock stare: %s' % new_state

if __name__ == '__main__':
    main()
