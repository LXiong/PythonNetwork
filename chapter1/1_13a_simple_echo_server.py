#! /usr/bin/python

import socket
import sys
import argparse

host = 'localhost'
data_payload = 4098
backlog = 5

def echo_server(port):
    """A simple echo server"""
    # Create socket object
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Enable reuse address
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # Bind the socket to a address
    server_address = (host,port)
    sock.bind(server_address)
    print "Start service on port : %d" % port
    sock.listen(backlog)
    while True:
        print "Waiting to receive from client..."
        client,addr = sock.accept()
        recv_data = client.recv(data_payload)
        if recv_data:
            response = "OK.I have received"
            size = client.send(response)
            print "Sending %s byte to client." % size
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket echo server')
    parser.add_argument('--port',action='store',dest='port',type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
        
