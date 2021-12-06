# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WiredDeviceUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 478))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.HostList = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.HostList.setObjectName("HostList")
        self.horizontalLayout_3.addWidget(self.HostList)
        self.RefreshHostListBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.RefreshHostListBTN.setMinimumSize(QtCore.QSize(20, 0))
        self.RefreshHostListBTN.setMaximumSize(QtCore.QSize(100, 16777215))
        self.RefreshHostListBTN.setBaseSize(QtCore.QSize(20, 0))
        self.RefreshHostListBTN.setObjectName("RefreshHostListBTN")
        self.horizontalLayout_3.addWidget(self.RefreshHostListBTN)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.HostName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.HostName.setObjectName("HostName")
        self.horizontalLayout.addWidget(self.HostName)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.PortNumber = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PortNumber.setMaximumSize(QtCore.QSize(102, 16777215))
        self.PortNumber.setObjectName("PortNumber")
        self.horizontalLayout.addWidget(self.PortNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ConnectBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ConnectBTN.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ConnectBTN.setObjectName("ConnectBTN")
        self.horizontalLayout_5.addWidget(self.ConnectBTN)
        self.ConnectionStatus = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ConnectionStatus.setObjectName("ConnectionStatus")
        self.horizontalLayout_5.addWidget(self.ConnectionStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.Acc = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Acc.setObjectName("Acc")
        self.Acc.addItem("")
        self.Acc.addItem("")
        self.Acc.addItem("")
        self.Acc.addItem("")
        self.horizontalLayout_2.addWidget(self.Acc)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.SampleFreq = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.SampleFreq.setObjectName("SampleFreq")
        self.SampleFreq.addItem("")
        self.SampleFreq.addItem("")
        self.SampleFreq.addItem("")
        self.SampleFreq.addItem("")
        self.SampleFreq.addItem("")
        self.horizontalLayout_2.addWidget(self.SampleFreq)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.SampleSize = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SampleSize.setMaximumSize(QtCore.QSize(102, 16777215))
        self.SampleSize.setObjectName("SampleSize")
        self.horizontalLayout_2.addWidget(self.SampleSize)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.GetMeasureBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.GetMeasureBTN.setMaximumSize(QtCore.QSize(200, 16777215))
        self.GetMeasureBTN.setObjectName("GetMeasureBTN")
        self.verticalLayout.addWidget(self.GetMeasureBTN)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(530, 0, 16, 481))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(550, 0, 491, 481))
        self.graphicsView.setObjectName("graphicsView")
        self.DrawTestBTN = QtWidgets.QPushButton(self.centralwidget)
        self.DrawTestBTN.setGeometry(QtCore.QRect(550, 520, 80, 25))
        self.DrawTestBTN.setObjectName("DrawTestBTN")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(550, 490, 481, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DrawXBTN = QtWidgets.QPushButton(self.widget)
        self.DrawXBTN.setObjectName("DrawXBTN")
        self.horizontalLayout_4.addWidget(self.DrawXBTN)
        self.DrawYBTN = QtWidgets.QPushButton(self.widget)
        self.DrawYBTN.setObjectName("DrawYBTN")
        self.horizontalLayout_4.addWidget(self.DrawYBTN)
        self.DrawZBTN = QtWidgets.QPushButton(self.widget)
        self.DrawZBTN.setObjectName("DrawZBTN")
        self.horizontalLayout_4.addWidget(self.DrawZBTN)
        self.DrawClearBTN = QtWidgets.QPushButton(self.widget)
        self.DrawClearBTN.setObjectName("DrawClearBTN")
        self.horizontalLayout_4.addWidget(self.DrawClearBTN)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Acc.setCurrentIndex(3)
        self.SampleFreq.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RefreshHostListBTN.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "Host"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.ConnectBTN.setText(_translate("MainWindow", "Connect"))
        self.ConnectionStatus.setText(_translate("MainWindow", "Status:"))
        self.label_7.setText(_translate("MainWindow", "Accelerometer"))
        self.Acc.setItemText(0, _translate("MainWindow", "2G"))
        self.Acc.setItemText(1, _translate("MainWindow", "4G"))
        self.Acc.setItemText(2, _translate("MainWindow", "8G"))
        self.Acc.setItemText(3, _translate("MainWindow", "16G"))
        self.label_9.setText(_translate("MainWindow", "Frequency(Hz)"))
        self.SampleFreq.setItemText(0, _translate("MainWindow", "800"))
        self.SampleFreq.setItemText(1, _translate("MainWindow", "1600"))
        self.SampleFreq.setItemText(2, _translate("MainWindow", "3200"))
        self.SampleFreq.setItemText(3, _translate("MainWindow", "6400"))
        self.SampleFreq.setItemText(4, _translate("MainWindow", "12800"))
        self.label_8.setText(_translate("MainWindow", "Sample size"))
        self.SampleSize.setText(_translate("MainWindow", "12800"))
        self.GetMeasureBTN.setText(_translate("MainWindow", "Get measure"))
        self.DrawTestBTN.setText(_translate("MainWindow", "Test Draw"))
        self.DrawXBTN.setText(_translate("MainWindow", "X"))
        self.DrawYBTN.setText(_translate("MainWindow", "Y"))
        self.DrawZBTN.setText(_translate("MainWindow", "Z"))
        self.DrawClearBTN.setText(_translate("MainWindow", "Clear"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
