
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from sqlite_db import *
import json
class Ui_MainWindow(object):
    sd = Sqlite_Database()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createRDR = QtWidgets.QPushButton(self.centralwidget)
        self.createRDR.setGeometry(QtCore.QRect(210, 60, 56, 17))
        self.createRDR.setObjectName("createRDR")
        self.createinvoice = QtWidgets.QPushButton(self.centralwidget)
        self.createinvoice.setGeometry(QtCore.QRect(360, 60, 56, 17))
        self.createinvoice.setObjectName("createinvoice")
        self.printRDR = QtWidgets.QPushButton(self.centralwidget)
        self.printRDR.setGeometry(QtCore.QRect(210, 200, 56, 17))
        self.printRDR.setObjectName("printRDR")
        self.printinvoice = QtWidgets.QPushButton(self.centralwidget)
        self.printinvoice.setGeometry(QtCore.QRect(360, 200, 56, 17))
        self.printinvoice.setObjectName("printinvoice")
        self.roomid = QtWidgets.QLineEdit(self.centralwidget)
        self.roomid.setGeometry(QtCore.QRect(120, 20, 71, 21))
        self.roomid.setObjectName("roomid")
        self.starttimeRDR = QtWidgets.QLineEdit(self.centralwidget)
        self.starttimeRDR.setGeometry(QtCore.QRect(120, 60, 71, 21))
        self.starttimeRDR.setObjectName("starttimeRDR")
        self.endtimeRDR = QtWidgets.QLineEdit(self.centralwidget)
        self.endtimeRDR.setGeometry(QtCore.QRect(120, 100, 71, 21))
        self.endtimeRDR.setObjectName("endtimeRDR")
        self.label_roomid = QtWidgets.QLabel(self.centralwidget)
        self.label_roomid.setGeometry(QtCore.QRect(80, 20, 41, 9))
        self.label_roomid.setObjectName("label_roomid")
        self.label_start = QtWidgets.QLabel(self.centralwidget)
        self.label_start.setGeometry(QtCore.QRect(70, 60, 41, 9))
        self.label_start.setObjectName("label_start")
        self.label_endtime = QtWidgets.QLabel(self.centralwidget)
        self.label_endtime.setGeometry(QtCore.QRect(70, 100, 41, 9))
        self.label_endtime.setObjectName("label_endtime")
        self.showRDR = QtWidgets.QTextBrowser(self.centralwidget)
        self.showRDR.setGeometry(QtCore.QRect(210, 90, 81, 101))
        self.showRDR.setObjectName("showRDR")
        self.showinvoice = QtWidgets.QTextBrowser(self.centralwidget)
        self.showinvoice.setGeometry(QtCore.QRect(360, 90, 81, 101))
        self.showinvoice.setObjectName("showinvoice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.createRDR.clicked.connect(lambda: self.CreateRDR())  # 这边改槽
        self.createinvoice.clicked.connect(lambda:self.CreateInvoice())#这边改槽
        self.printRDR.clicked.connect(lambda: self.PrintRDR())  # 这边改槽
        self.printinvoice.clicked.connect(lambda: self.PrintInvoice())  # 这边改槽
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createRDR.setText(_translate("MainWindow", "创建详单"))
        self.createinvoice.setText(_translate("MainWindow", "创建账单"))
        self.printRDR.setText(_translate("MainWindow", "打印详单"))
        self.printinvoice.setText(_translate("MainWindow", "打印账单"))
        self.label_roomid.setText(_translate("MainWindow", "房间号"))
        self.label_start.setText(_translate("MainWindow", "开始时间"))
        self.label_endtime.setText(_translate("MainWindow", "截至时间"))
        self.menu.setTitle(_translate("MainWindow", "前台"))

    def CreateRDR(self):
        RoomId = self.roomid.text()
        date_in = self.starttimeRDR.text()
        date_out = self.endtimeRDR.text()
        print("This is CreateRDR ",RoomId,date_in,date_out)
        createrdr = json.dumps(XXX, ensure_ascii=False)
        print(createrdr)
        self.showRDR.insertPlainText(createrdr)#
    def PrintRDR(self):  # RDR详单
        #self.printRDR.isSignalConnected()lambda: self.PrintRDR())  # 这边改槽
        print("This is PrintRDR")
        string = '1234'

       # sd_getinvoice = sd.get_invoice(111,)
      #  d = {
         #   'name': 'python书籍',
         #   'price': 62.3,
         #   'is_valid': True
       # }
        print(d) #到这儿都ok
        printinvoice = json.dumps(XXX, ensure_ascii=False)
        print(printinvoice)
        self.showRDR.insertPlainText(printinvoice)

    def CreateInvoice(self):  # Invoice 账单
        createinvoice = json.dumps(d, ensure_ascii=False)
        print(createinvoice)
        self.showRDR.insertPlainText(createinvoice)
        print("This is CreateInvoice")

    def PrintInvoice(self):
        print("This is PrintInvoice")
        printinvoice = json.dumps(d, ensure_ascii=False)
        print(printinvoice)
        self.showRDR.insertPlainText(printinvoice)

if  __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
