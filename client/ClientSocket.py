#!/usr/bin/python3

import socket
import sys
import threading
import fileinput

class ClientSocket(threading.Thread):
    DefaultHOST = '127.0.0.1'
    DefaultPort = 1102
    CONNECTED = 1
    CONNECTING = 2
    FAILED = 3
    DISCONNECTED = 4
    STATUS = 4
    def __init__(self, daemon=None, HOST=DefaultHOST, PORT=DefaultPort, onStatusChange=None, onReceive=None):
        super(ClientSocket, self).__init__(daemon=daemon)
        self.__is_running = True
        self.daemon = daemon
        self.HOST = HOST
        self.PORT = PORT
        self.socket = None
        self.__is_running = True
        self.onStatusChange = onStatusChange
        self.onReceive = onReceive

    def terminate(self):
        if self.socket != None:
            self.socket.close()

        self.socket = None
        self.__is_running = False

    def connect(self):
        self.setStatus(self.CONNECTING)
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.HOST, self.PORT))
            self.setStatus(self.CONNECTED)
            self.receive()
        except Exception as e:
            self.socket = None
            self.setStatus(self.FAILED)
            print ("Connect error %s" %  e)

    def setStatus(self, status):
        self.STATUS = status
        self.onStatusChange(status)

    def receive(self):
        while True:
            try:
                serverMessage = str(self.socket.recv(1024), encoding='utf-8')
                if len(serverMessage) > 0:
                    self.onReceive(serverMessage)
                else:
                    print('Receive error, len:', len(serverMessage))
                    self.setStatus(self.DISCONNECTED)
                    break
            except socket.error as e:
                print ("Error receiving data: %s" %  e)
                self.setStatus(self.DISCONNECTED)
                break

    def sendall(self, message):
        if self.socket:
            self.socket.sendall(message)

    def run(self):
        self.connect()

########################################################################
if __name__ == '__main__':
    def onStatusChange(data):
        print(data)
    def onReceive(data):
        print('Server:', data)

    # prepare HOST and PORT
    if len(sys.argv) == 3:
        try:
            socket.inet_aton(sys.argv[1])
            # legal
            HOST = sys.argv[1]
            PORT = int(sys.argv[2])
        except socket.error:
            print('ip format got error, use default ip: ' + HOST)
            HOST = '127.0.0.1'
            PORT = 1102
    else:
        HOST = '127.0.0.1'
        PORT = 1102

    mClientSocket = ClientSocket(True, HOST, PORT, onStatusChange, onReceive)
    mClientSocket.start()
    while True:
        message = input()
        if message == 'exit':
            mClientSocket.terminate()
            break
        elif message == 'restart':
#            mClientSocket = ClientSocket(True, HOST, PORT, onStatusChange, onReceive)
#            mClientSocket.start()
            mClientSocket.__is_running = True
            mClientSocket.start()
        elif message == 'disconnect':
            mClientSocket.terminate()
        else:
            if mClientSocket and mClientSocket.STATUS == ClientSocket.CONNECTED:
                mClientSocket.sendall(message.encode())
        continue

    print("DONE")

    exit()

