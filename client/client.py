#!/usr/bin/python3

import socket
import sys
import threading

HOST = '127.0.0.1'
PORT = 1102

# TODO verify HOST' ip by command line argv
if len(sys.argv) > 1:
  try:
    socket.inet_aton(sys.argv[1])
    # legal
    HOST = sys.argv[1]
  except socket.error:
    print('ip format got error, use default ip: ' + HOST)

def connectSocket():
  #clientMessage = 'Hello!'
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((HOST, PORT))
  #client.sendall(clientMessage.encode())

  while True:
    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server:', serverMessage)


socket_t = threading.Thread(target = connectSocket)
socket_t.start();
#client.close()
