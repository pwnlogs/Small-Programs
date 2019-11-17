"""
    Simple listener for TCP
Adapted from: https://medium.com/python-pandemonium/python-socket-communication-e10b39225a4c
"""

import socket

# Create a TCP/IP socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = ''
port = 10000
host = 'localhost'

# Bind the socket to the port
server_address = (host, port)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    sleep(1)

while True:
    # Wait for data
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('\nreceived {!r}'.format(data))
            if data:
                print('sending "ok" back to the client')
                connection.sendall(b'ok')
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()
        
