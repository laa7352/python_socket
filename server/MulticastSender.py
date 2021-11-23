import socket
import json
import threading
import time

class MulticastSender(threading.Thread):
    DefaultHost = '127.0.0.1'
    DefaultPort = 1102
    DefaultDeviceName = 'raseberry pi'
    def __init__(self, daemon=None, Host=DefaultHost, Port=DefaultPort, DeviceName=DefaultDeviceName):
        super(MulticastSender, self).__init__(daemon=daemon)
        self.__is_running = True
        self.daemon = daemon
        DefaultJsonStr= '{ "Host": "", "Port": 0, "DeviceName": "" }'
        self.deviceInfo = json.loads(DefaultJsonStr)
        self.deviceInfo["Host"] = Host
        self.deviceInfo["Port"] = Port
        self.deviceInfo["DeviceName"] = DeviceName

    def get_Ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception as e:
            print('test99', e)
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def setPort(self, Port):
        self.deviceInfo["Port"] = Port

    def setDeviceName(self, DeviceName):
        self.deviceInfo["Port"] = DeviceNamePort

    def getDeviceInfo(self):
        #print('test3', self.get_Ip())
        self.deviceInfo["Host"] = self.get_Ip()
        return self.deviceInfo

    def terminate(self):
        self.__is_running = False

    def run(self):
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5007
        # regarding socket.IP_MULTICAST_TTL
        # ---------------------------------
        # for all packets sent, after two hops on the network the packet will not 
        # be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
        MULTICAST_TTL = 2
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

        # For Python 3, change next line to 'sock.sendto(b"robot", ...' to avoid the
        # "bytes-like object is required" msg (https://stackoverflow.com/a/42612820)
        print("Multicast sender is started")
        while True:
            DeviceInfoStr = json.dumps(self.getDeviceInfo())
            sock.sendto(DeviceInfoStr.encode(encoding="utf-8"), (MCAST_GRP, MCAST_PORT))
            #print('test5 %s %s %s' %(time.ctime(), self.getDeviceInfo(), DeviceInfoStr))
            time.sleep(2)


if __name__ == '__main__':
    mMulticastSender = MulticastSender(True, '127.0.0.1', 1102, 'Jimmy')
    mMulticastSender.start()
    mMulticastSender.join()
    #print(get_ip())
