#!/usr/bin/python3

import socket
import threading
import fileinput
import threading
#import time
#import os

#HOST = ''
#PORT = 1102
#client_list = []

class ServerSocket(threading.Thread):
    def __init__(self, daemon=None):
        super(ServerSocket, self).__init__(daemon=daemon)
        self.__is_running = True
        self.daemon = daemon
        self.client_list = []
        self.HOST = ''
        self.PORT = 1102

    def printList(self):
        print(self.client_list)

    def broadcast(self, message):
        remove_client_list = []
        for client in self.client_list:
            try:
                client.sendall(message)
            except Exception as e:
                print('remove client when got error')
                print(client)
                remove_client_list.append(client)

        for client in remove_client_list:
            self.client_list.remove(client)

    def terminate(self):
        for client in self.client_list:
            client.close()
        self.__is_running = False


    def listenToClient(self, client, address):
        size = 1024
        print('listen client %d ' % client.fileno())
        while True:
            try:
                message = str(client.recv(1024), encoding='utf-8')
                if message:
                    # Set the response to echo back the recieved data 
                    #response = data
                    #print('Client %d: %s' %client.fileno(), message)
                    print('{} {}{} {}'.format('Client', client.fileno(), ':', message))
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.HOST, self.PORT))
        server.listen(10)
        print("Socket Server listening")
        while True:
            client, address = server.accept()
            print('Client is connected', client, address)
            self.client_list.append(client)
            print(self.client_list)
            threading.Thread(target = self.listenToClient, args = (client, address)).start()


if __name__ == '__main__':
    mServerSocket = ServerSocket(True)
    mServerSocket.start()
    ########################################################################
    # TODO
    #   simulator send message to clients
    while True:
        message = input()
        if message == 'exit':
            mServerSocket.terminate()
            break
        elif message == 'list':
            mServerSocket.printList();
        else:
            mServerSocket.broadcast(message.encode())

    ########################################################################
    print("DONE")
