import socket
import json
import threading
import struct

class MulticastReceiver(threading.Thread):
    def __init__(self, daemon=None, onReceive=None):
        super(MulticastReceiver, self).__init__(daemon=daemon)
        self.__is_running = True
        self.daemon = daemon
        self.onReceive = onReceive

    def terminate(self):
        self.__is_running = False

    def run(self):
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5007
        IS_ALL_GROUPS = True

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if IS_ALL_GROUPS:
            # on this port, receives ALL multicast groups
            sock.bind(('', MCAST_PORT))
        else:
            # on this port, listen ONLY to MCAST_GRP
            sock.bind((MCAST_GRP, MCAST_PORT))

        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        while True:
            self.onReceive(sock.recv(10240))

########################################################################
if __name__ == '__main__':
    def onReceive(DeviceInfo):
        print(DeviceInfo["Host"])
        print(DeviceInfo["Port"])
        print(DeviceInfo["DeviceName"])

    mMulticastReceiver = MulticastReceiver(True, onReceive)
    mMulticastReceiver.start()
    mMulticastReceiver.join()
