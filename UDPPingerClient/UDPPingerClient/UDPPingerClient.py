# UDPPingerClient
# By: Team 7

import socket
from socket import AF_INET, SOCK_DGRAM
import time


#Create Socket
serverName = '127.0.0.1' #Local Host Default
serverPort = 12000
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(1,11): #loop 10 times
    #Send ping/Start Timer
    start = time.time()
    clientSocket.sendto(bytes('ping', 'utf-8'), (serverName, serverPort))

    #Recieve Response/End Timer
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        print(modifiedMessage.decode('utf-8'), i, end-start)
    except socket.timeout:
        end = time.time()
        print('Request timed out', i, end-start)
    
clientSocket.close()
