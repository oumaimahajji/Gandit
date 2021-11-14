from socket import *

serverName = "oumaima-VivoBook-ASUSLaptop-X515JA-X515JA"
serverPort = 6688


clientSocket = socket()
clientSocket.connect((serverName, serverPort))

while True:
    response_data = clientSocket.recv(1024)
    print("Response data from server : ", response_data.decode())

