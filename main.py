
import os
import time
from socket import socket

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 460, 361, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 460, 361, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 520, 361, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 520, 361, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 490, 361, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 490, 361, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 20, 571, 231))
        self.textEdit.setObjectName("textEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 280, 751, 161))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 10, 361, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 40, 361, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 70, 361, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 100, 361, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 130, 361, 25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(380, 10, 361, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 260, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_8.clicked.connect(self.operatingSystemInfo)  # type: ignore
        self.pushButton_9.clicked.connect(self.infoMachinn)  # type: ignore
        self.pushButton_10.clicked.connect(self.runningApplications)  # type: ignore
        self.pushButton_11.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_12.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_13.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_6.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_4.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_7.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_5.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def operatingSystemInfo(self):

        hostname = os.getlogin()

        self.textEdit.append("Loading Information ")
       


        time.sleep(1.5)
        self.textEdit.append("Your Computer Name is       :    " + hostname)

    def infoMachinn(self):
        import requests
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        self.textEdit.append("Your Public Ip Adress Is : %s" % ip)

    def runningApplications(self):
        import psutil
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                processID = proc.pid
                print(processName, ' ::: ', processID)
                self.textEdit.append("PROCESS ID          %s     PROCESS NAME      %s" % (processID, processName))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Windows To The Moon   V0.0.1                            ~By ArMin~"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear Prefetch"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear Local Temp"))
        self.pushButton_4.setText(_translate("MainWindow", "C:WindowsDownloaded Program Files"))
        self.pushButton_5.setText(_translate("MainWindow", "C:WindowsLiveKernelReports"))
        self.pushButton_6.setText(_translate("MainWindow", "C:Windows.old"))
        self.pushButton_7.setText(_translate("MainWindow", "C:WindowsTemp"))
        self.pushButton_8.setText(_translate("MainWindow", "Windows Name"))
        self.pushButton_9.setText(_translate("MainWindow", "Ip Adress"))
        self.pushButton_10.setText(_translate("MainWindow", "Running Apps"))
        self.pushButton_11.setText(_translate("MainWindow", "StartUp Items"))
        self.pushButton_12.setText(_translate("MainWindow", "Running Apps"))
        self.pushButton_13.setText(_translate("MainWindow", "Check Regedit"))
        self.label.setText(_translate("MainWindow", "Windows Information"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
