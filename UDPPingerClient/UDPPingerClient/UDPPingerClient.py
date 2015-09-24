# UDPPingerClient
# By: Team 7 (Andrew Fillmore, Colby Gerdes, Nathan Emerson)

import socket
from socket import AF_INET, SOCK_DGRAM
import time

sum = 0.0
min = 2.0
max = 0.0
numSuccessPing = 0
total = 10

#Create Socket
serverName = '10.209.0.21' #Local Host Default
serverPort = 12000
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)


for i in range(1,total + 1): #loop 10 times
    #Send ping/Start Timer
    start = time.time()
    clientSocket.sendto(bytes('ping', 'utf-8'), (serverName, serverPort))
    
    #Recieve Response/End Timer
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        rtt = end - start
        print(modifiedMessage.decode('utf-8'), i, float("{0:.5f}".format(rtt)))
        sum += rtt

        #Set min
        if (rtt < min):
            min = rtt
        #Set max
        if (rtt > max):
            max = rtt
        #Count Successful pings
        numSuccessPing += 1
    except socket.timeout:
        print('Request timed out', i)

print('\nMin =', float("{0:.5f}".format(min)),
      ' Max =', float("{0:.5f}".format(max)),
      ' Average =', float("{0:.5f}".format(sum / numSuccessPing)))

print('Lost =', ((total - numSuccessPing) / total) * 100,'%')

clientSocket.close()
