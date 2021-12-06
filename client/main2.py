from PyQt5 import QtWidgets, QtGui, QtCore
from WiredDeviceUI import Ui_MainWindow
import numpy as np
import json
import threading
import time
from enum import Enum
from ClientSocket import ClientSocket
from MulticastReceiver import MulticastReceiver

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	delegate = {
		"restartMulticastReceiver": None,
		"connectServer": None,
		}

	DrawData = None
	Y_AXIS_Data_X = None
	Y_AXIS_Data_Y = None
	Y_AXIS_Data_Z = None
	X_AXIS = None

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.DrawTestBTN.clicked.connect(self.drawTest)
		self.DrawClearBTN.clicked.connect(self.clear)
		self.HostList.activated.connect(self.onHostClick)
		self.RefreshHostListBTN.clicked.connect(self.RefresHostList)
		self.ConnectBTN.clicked.connect(self.connectServer)

		self.onlyInt = QtGui.QIntValidator()
		self.PortNumber.setValidator(self.onlyInt)

		ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # Part of the regular expression
		# Regulare expression
		ipRegex = QtCore.QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
		ipValidator = QtGui.QRegExpValidator(ipRegex, self)
		self.HostName.setValidator(ipValidator)

		self.SampleSize.setValidator(self.onlyInt)

		self.GetMeasureBTN.clicked.connect(self.GetMeasure)
		self.DrawXBTN.clicked.connect(lambda: self.Draw(self.X_AXIS, self.Y_AXIS_Data_X))
		self.DrawYBTN.clicked.connect(lambda: self.Draw(self.X_AXIS, self.Y_AXIS_Data_Y))
		self.DrawZBTN.clicked.connect(lambda: self.Draw(self.X_AXIS, self.Y_AXIS_Data_Z))
		self.DrawXBTN.setEnabled(False)
		self.DrawYBTN.setEnabled(False)
		self.DrawZBTN.setEnabled(False)

	def updateHostList(self, list):
		self.HostList.clear()
		for info in list:
			infoStr = info["DeviceName"] + '(' + info["Host"] + ':' + str(info["Port"]) + ')'
			self.HostList.addItem(infoStr)

	def onHostClick(self):
		index = self.HostList.currentIndex()
		self.HostName.setText(DeviceInfoList[index]["Host"])
		self.PortNumber.setText(str(DeviceInfoList[index]["Port"]))

	def RefresHostList(self):
		# Restart MulticastReceiver
		if self.delegate["restartMulticastReceiver"]:
			self.delegate["restartMulticastReceiver"]()

	def onStatusChange(self, statusStr, btnStr):
		self.ConnectionStatus.setText(statusStr)
		self.ConnectBTN.setText(btnStr)

	def connectServer(self):
		if self.delegate["connectServer"]:
			self.delegate["connectServer"]()

	def getHostName(self):
		return self.HostName.text()

	def getPortNumber(self):
		return int(self.PortNumber.text())

	def GetMeasure(self):
		acc = self.Acc.currentText()
		sampling_f = int(self.SampleFreq.currentText())
		sampling_s = int(self.SampleSize.text())
		if self.delegate["GetMeasure"] and acc and sampling_f and sampling_s:
			self.delegate["GetMeasure"](acc, sampling_f, sampling_s)

	def Draw(self, x, y):
		self.graphicsView.plot(x, y)

	def SetDrawData(self, obj):
		DrawData = obj
		N = obj["sampling_s"]  # sampling_s = 128000
		T = 1.0 / float(obj["sampling_f"]) # sampling_f = 12800
		self.X_AXIS = np.linspace(0.0, N*T, N)

		yx = obj["result"][0] # x data
		yx_f = np.fft.fft(yx)
		self.Y_AXIS_Data_X = 1.0/N * np.abs(yx_f[:N//1])

		yy = obj["result"][1] # y data
		yy_f = np.fft.fft(yy)
		self.Y_AXIS_Data_Y = 1.0/N * np.abs(yy_f[:N//1])

		yz= obj["result"][2] # z data
		yz_f = np.fft.fft(yz)
		self.Y_AXIS_Data_Z = 1.0/N * np.abs(yz_f[:N//1])
		self.DrawXBTN.setEnabled(True)
		self.DrawYBTN.setEnabled(True)
		self.DrawZBTN.setEnabled(True)

	def drawTest(self):
		x = np.random.normal(size=1000)
		y = np.random.normal(size=(3,1000))
		for i in range(3):
			self.graphicsView.plot(x, y[i], pen=(i,3))

	def clear(self):
		self.graphicsView.clear()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()

	########################################################################	
	# Multicast
	DeviceInfoList = []
	def onMulticastReceive(data):
		try:
			DeviceInfo = json.loads(data)
			#print("Receive: ", DeviceInfo)
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
				updateHostList()
		else:
			for info in DeviceInfoList:
				info["Timeout"] += 1
				if info["Timeout"] > 5:
					removeList.append(info)
			for info in removeList:
				DeviceInfoList.remove(info)
				updateHostList()
		#print(DeviceInfoList)

	def checkDeviceInfos():
		while True:
			maintainDeviceInfos(False, None)
			time.sleep(1)

	def updateHostList():
		window.updateHostList(DeviceInfoList)

	def restartMulticastReceiver():
		global mMulticastReceiver
		mMulticastReceiver.terminate()
		mMulticastReceiver = MulticastReceiver(True, onMulticastReceive)
		mMulticastReceiver.start()

	checkDeviceInfosThread = threading.Thread(target = checkDeviceInfos, daemon=True)
	checkDeviceInfosThread.start()
	mMulticastReceiver = MulticastReceiver(True, onMulticastReceive)
	mMulticastReceiver.start()

	window.delegate["restartMulticastReceiver"] = restartMulticastReceiver
	########################################################################	
	# ClientSocket
	StatusDict = {
		1: "CONNECTED",
		2: "CONNECTING",
		3: "FAILED",
		4: "DISCONNECTED"
	}
	mClientSocket = None

	def onStatusChange(data):
		status = "Status:  " + StatusDict.get(data, "Invalid season")
		if data == ClientSocket.CONNECTED or data == ClientSocket.CONNECTING:
			btnStr = "Disconnect"
		elif data == ClientSocket.FAILED or data == ClientSocket.DISCONNECTED:
			btnStr = "Connect"

		window.onStatusChange(status, btnStr)
		print(status, btnStr)

	def onClientSocketReceive(data):
		print('receive data from Server: ', data, ', length:', len(data))
		#print('Server:', data)
		#logOutput['text'] += data + '\n'
		try:
			obj = json.loads(data)
			print("ClientSocketReceive", obj["command"])
			if obj["command"] == CommandList.GET_MEASURE:
				#print("x:", obj["result"][0])
				#print("y:", obj["result"][1])
				#print("z:", obj["result"][2])
				#N = 10
				#T = 1.0 / 12800.0
				#y_f = np.fft.fft(obj["result"][0])
				#x_f = np.linspace(0.0, 100,10)
				#plt.plot(x_f, y_f)
				#plt.show()
				window.SetDrawData(obj)

		except Exception as e:
			print("json parsing error", e)

	def connectClientSocket(Host, Port):
		global mClientSocket
		mClientSocket = ClientSocket(True, Host, Port, onStatusChange, onClientSocketReceive)
		mClientSocket.start()

	def disconnectClientSocket():
		global mClientSocket
		print("disconnectClientSocket", mClientSocket)
		if mClientSocket:
			mClientSocket.terminate()

	def connectServer():
		Host = window.getHostName()
		Port = window.getPortNumber()

		global mClientSocket

		if mClientSocket and mClientSocket.STATUS <= 2:
			print("do disconnect")
			disconnectClientSocket()
		elif Host and Port:
			print("do connect", Host, str(Port))
			#logOutput['text'] = 'connect to ' + Host + ':' + str(Port) + '\n'
			connectClientSocket(Host, Port)

	window.delegate["connectServer"] = connectServer

	########################################################################
	# Command
	class CommandList():
		SET_PORT = 1
		SET_DEVICENAME = 2
		GET_ALL_TELEMETRY = 3
		GET_MEASURE = 4

	def getCommand(command):
		CommandTemple = json.loads('{"command": 0}')
		CommandTemple["command"] = command
		return CommandTemple

	def GetMeasure(acc, sampling_f, sampling_s):
		command = getCommand(CommandList.GET_MEASURE)
		command["acc_range"] = acc
		command["sampling_f"] = sampling_f
		command["sampling_s"] = sampling_s
		print("GetMeasure:", acc, sampling_f, sampling_s)
		global mClientSocket
		if mClientSocket and mClientSocket.STATUS == ClientSocket.CONNECTED:
			try:
				mClientSocket.sendall(json.dumps(command).encode())
			except Exception as e:
				print("error:", e)

	window.delegate["GetMeasure"] = GetMeasure
	########################################################################
	# Draw
	########################################################################

	window.show()
	sys.exit(app.exec_())
