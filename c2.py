#!/usr/bin/env python3
import socket

s = socket.socket()
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection
while True:
    c, addr = s.accept()  # Establish connection with client
    print(f"Connection from {addr} has been established.")
    c.send(b"sql select*")
    print(c.recv(1024))
    c.close()  # Close the connection