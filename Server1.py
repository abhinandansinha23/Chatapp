import socket
import sys
import time

import portal as portal

s=socket.socket()
host=input(str("Please enter the host you want to connect to: "))
port=1025

try:
    s.connect((host,portal))
    print("Connected to host")
except:
    print(" Connection failed")

while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Reply-> ", incoming_message)

    message=input(str("Enter your message-> "))
    message=message.encode()
    s.send(message)