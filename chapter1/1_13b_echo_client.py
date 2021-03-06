import socket
import argparse
import sys

host = 'localhost'

def echo_client(port):
    """A echo client"""
    # Create a TCP/TP client
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = (host,port)
        sock.connect(server_address)
        data = 'Hi,I\'m echo client.'
        sock.sendall(data)
        response = sock.recv(1024)
        print 'Receive: %s' % response
    except socket.error,msg:
        print "Socket error: %s" %  msg
        sys.exit(1)
    finally:
        print "Connection is closing..."
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='a simple example')
    parser.add_argument('--port',action='store',type=int,dest='port',required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)

    
        
