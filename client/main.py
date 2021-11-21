import tkinter as tk
import tkinter.ttk as ttk
import threading
import time
import json
from MulticastReceiver import MulticastReceiver
from ClientSocket import ClientSocket

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Python socket")
    root.geometry("600x400")
    uiRow=0

    DeviceInfoList = []
    mMulticastReceiver = None
    mClientSocket = None

    ######################################################################## 
    # UI
    def connect():
        logOutput['text'] = 'connect to ' + hostText.get() + ':' + portText.get()
        Host = hostText.get()
        Port = int(portText.get())

        global mClientSocket

        print("test", mClientSocket)
        if mClientSocket and mClientSocket.STATUS <= 2:
            disconnectClientSocket()
        elif Host and Port:
            connectClientSocket(Host, Port)

    # combobox
    def onComboxSelected(*args):
        index = serverList.current()
        print(index, DeviceInfoList[index]['Host'], DeviceInfoList[index]['Port'])
        hostText.set(DeviceInfoList[index]['Host'])
        portText.set(str(DeviceInfoList[index]['Port']))

    serverList = ttk.Combobox(root, values=[], state='readonly')
    serverList.grid(row=uiRow, column=0, columnspan=3)
    serverList.bind("<<ComboboxSelected>>", onComboxSelected)
    uiRow+=1

    # Server IP
    tk.Label(root, text="Server IP").grid(row=uiRow, stick="w")
    hostText = tk.StringVar()
    hostInput = tk.Entry(root, textvariable = hostText)
    hostInput.grid(row=uiRow, column=1)
    uiRow+=1
    # Port
    tk.Label(root, text="Port").grid(row=uiRow, stick="w")
    portText = tk.StringVar()
    portInput = tk.Entry(root, textvariable = portText)
    portInput.grid(row=uiRow, column=1)
    uiRow+=1

    # Status
    tk.Label(root, text="Status").grid(row=uiRow)
    statusText = tk.Label(root, text="DISCONNECT")
    statusText.grid(row=uiRow, column=1)
    uiRow+=1

    # Button
    connectBTN = tk.Button(text="Connect", width=10, command=connect)
    connectBTN.grid(row=uiRow, columnspan=2, pady=5)
    uiRow+=1

    # Log
    tk.Label(root, text="Log:").grid(row=uiRow, column=0, rowspan=10, stick="N")
    logOutput = tk.Label(root, text="")
    logOutput.grid(row=uiRow, column=1, rowspan=10, stick="N")
    uiRow+=1

    ######################################################################## 
    # MulticastReceiver
    def onMulticastReceive(data):
        try:
            DeviceInfo = json.loads(data)
            maintainDeviceInfos(True, DeviceInfo)
        except Exception as e:
            print("parsing json error", e)

    def maintainDeviceInfos(isReceived, DeviceInfo):
        removeList = []
        if (isReceived):
            isExisted = False
            for info in DeviceInfoList:
                if DeviceInfo["Host"] == info["Host"] and DeviceInfo["Port"] == info["Port"]:
                        info["Timeout"] = 0
                        info["DeviceName"] = DeviceInfo["DeviceName"]
                        isExisted = True
                        break
            if not isExisted:
                DeviceInfo["Timeout"] = 0
                DeviceInfoList.append(DeviceInfo)
                updateCombobox()
        else:
            for info in DeviceInfoList:
                info["Timeout"] += 1
                if info["Timeout"] > 5:
                    removeList.append(info)
            for info in removeList:
                DeviceInfoList.remove(info)
                updateCombobox()
        #print(DeviceInfoList)

    def checkDeviceInfos():
        while True:
            maintainDeviceInfos(False, None)
            time.sleep(1)

    def updateCombobox():
        list = []
        maxWidth = 20
        for info in DeviceInfoList:
            DeviceInfostr = info["DeviceName"] + '(' + info["Host"] + ':' + str(info["Port"]) + ')'
            if len(DeviceInfostr) >= maxWidth:
                maxWidth = len(DeviceInfostr)
            list.append(DeviceInfostr)
        serverList['values'] = list
        serverList['width'] = maxWidth

    checkDeviceInfosThread = threading.Thread(target = checkDeviceInfos)
    checkDeviceInfosThread.setDaemon(True)
    checkDeviceInfosThread.start()

    mMulticastReceiver = MulticastReceiver(True, onMulticastReceive)
    mMulticastReceiver.start()

    ############################################
    # ClientSocket
    StatusDict = {
        1: "CONNECTED",
        2: "CONNECTING",
        3: "FAILED",
        4: "DISCONNECTED"
    }

    def onStatusChange(data):
        status = StatusDict.get(data, "Invalid season")
        statusText["text"] = status
        if data == ClientSocket.CONNECTED or data == ClientSocket.CONNECTING:
            connectBTN['text'] = "Disconnect"
        elif data == ClientSocket.FAILED or data == ClientSocket.DISCONNECTED:
            connectBTN['text'] = "Connect"

        print(status)

    def onClientSocketReceive(data):
        print('Server:', data)

    def connectClientSocket(Host, Port):
        global mClientSocket
        mClientSocket = ClientSocket(True, Host, Port, onStatusChange, onClientSocketReceive)
        mClientSocket.start()

    def disconnectClientSocket():
        global mClientSocket
        if mClientSocket:
            mClientSocket.terminate()

    ############################################
    root.mainloop()
