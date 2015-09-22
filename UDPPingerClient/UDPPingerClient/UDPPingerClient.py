# UDPPingerClient
# By: Team 7

from socket import *
import time

#Create Socket
serverName = '127.0.0.1' #Local Host Default
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1,10): #loop 10 times
    #Send ping/Start Timer
    start = time.time()
    clientSocket.sendto(bytes('ping', 'utf-8'), (serverName, serverPort))

    #Recieve Response/End Timer
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    end = time.time()

    #Print Response (or Timeout Message)
    print(modifiedMessage, i, start-end)

clientSocket.close()
