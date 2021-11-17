#!/usr/bin/python3

import socket
import sys
import threading
import fileinput

class ClientSocketThread(threading.Thread):
    DefaultHOST = '127.0.0.1'
    DefaultPort = 1102
    def __init__(self, daemon=None, HOST=DefaultHOST, PORT=DefaultPort):
        super(ClientSocketThread, self).__init__(daemon=daemon)
        self.__is_running = True
        self.daemon = daemon
        self.HOST = HOST
        self.PORT = PORT
        self.socket = None
        self.__is_running = True

    def terminate(self):
        if self.socket != None:
            self.socket.close()

        self.socket = None
        self.__is_running = False

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))

    def receive(self):
        while True:
            try:
                serverMessage = str(self.socket.recv(1024), encoding='utf-8')
                if len(serverMessage) > 0:
                    print('Server:', serverMessage)
                else:
                    print('Receive error, len:', len(serverMessage))
                    break
            except socket.error as e:
                print ("Error receiving data: %s" %  e)
                break

    def sendall(self, message):
        if self.socket != None:
            self.socket.sendall(message)

    def run(self):
        self.connect()
        self.receive()

if __name__ == '__main__':

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

    mClientSocket = ClientSocketThread(True, HOST, PORT)
    mClientSocket.start()
    while True:
        message = input()
        if message == 'exit':
            mClientSocket.terminate()
            break
        elif message == 'restart':
            mClientSocket = ClientSocketThread(True, HOST, PORT)
            mClientSocket.start()
        elif message == 'disconnect':
            mClientSocket.terminate()
        else:
            mClientSocket.sendall(message.encode())
        continue

    print("DONE")

    exit()

