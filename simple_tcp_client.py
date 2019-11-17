"""
    Simple client for TCP
Adapted from: https://medium.com/python-pandemonium/python-socket-communication-e10b39225a4c
"""

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
# ip = '192.168.0.105'
port = 10000

# Connect the socket to the port where the server is listening
server_address = (ip, port)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = str.encode(input('\nEnter message: '))
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(b'ok')

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
    
