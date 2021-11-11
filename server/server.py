#!/usr/bin/python3

import socket
import threading
import fileinput
import threading
#import time
#import os

HOST = ''
PORT = 1102
client_list = []

class SockerServerThread(threading.Thread):
  def __init__(self,daemon=None):
    super(SockerServerThread,self).__init__(daemon=daemon)
    self.__is_running = True
    self.daemon = daemon

  def terminate(self):
    self.__is_running = False

  def run(self):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(10)
    print("Socket Server listening")
    while True:
      conn, addr = server.accept()
      print('Client is connected', conn, addr);
      client_list.append(conn)
      print(client_list)

mSocketServer = SockerServerThread();
mSocketServer.start()
########################################################################
# TODO
#   simulator send message to clients
while True:
  message = input()
  if message == 'exit':
    break
  elif message == 'list':
    print(client_list)
  else:
    for client in client_list:
       try:
         client.sendall(message.encode())
       except Exception as e:
         print('remove client when got error')
         print(client)
         client_list.remove(client)

########################################################################


for client in client_list:
  client.close()
mSocketServer.terminate()

print("DONE")
