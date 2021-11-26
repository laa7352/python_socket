import fileinput
from MulticastSender import MulticastSender
from ServerSocket import ServerSocket

########################################################################
if __name__ == '__main__':
	mMulticastSender = MulticastSender(True, '127.0.0.1', 1102, 'Jimmy')
	mMulticastSender.start()
   # mMulticastSender.join()


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

	print("DONE")
