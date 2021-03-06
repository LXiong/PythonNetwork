#! /usr/bin/python

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Get the size of the buffer before modify
    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print 'Buffer size [before] : %d' % bufsize

    sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)
    
    # Get the size of the buffer after modify
    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
    print 'Buffer size [after] : %d' % bufsize

if __name__ == '__main__':
    modify_buff_size()
