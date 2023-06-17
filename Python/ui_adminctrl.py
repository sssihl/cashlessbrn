import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate,
QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt,
QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


import homeicon_rc
class ui_adminCtr(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(892, 508)
        MainWindow.setMinimumSize(QtCore.QSize(892, 508))
        MainWindow.setMaximumSize(QtCore.QSize(892, 508))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QtCore.QRect(0, 0, 892, 508))
        self.frame.setMinimumSize(QtCore.QSize(892, 508))
        self.frame.setMaximumSize(QtCore.QSize(892, 508))
        self.frame.setStyleSheet("background:url(:/home/adminCtrBg.png)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(360, 130, 201, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"		color:rgb(71, 71, 71);\n"
"		font: 22pt \"FONTSPRING DEMO - Grotesco Book \";\n"
"background:transparent;\n"
"}")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QtCore.QRect(120, 230, 191, 31))
        #self.pushButton_5.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	font: 25 13pt \"Segoe UI Light\";\n"
"background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	color:Black;\n"
"    font:;\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 0);    \n"
"	font: 12pt \"Segoe UI Semilight\";\n"
"	border: 1px solid rgb(64, 71, 88);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(24, 22, 100);\n"
"}\n"
"\n"
"")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QtCore.QRect(360, 230, 191, 31))
        #self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	font: 25 13pt \"Segoe UI Light\";\n"
"background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	color:Black;\n"
"    font:;\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 0);    \n"
"	font: 12pt \"Segoe UI Semilight\";\n"
"	border: 1px solid rgb(64, 71, 88);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(24, 22, 100);\n"
"}\n"
"\n"
"")
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QtCore.QRect(580, 230, 191, 31))
        #self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	font: 25 13pt \"Segoe UI Light\";\n"
"background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	color:Black;\n"
"    font:;\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 0);    \n"
"	font: 12pt \"Segoe UI Semilight\";\n"
"	border: 1px solid rgb(64, 71, 88);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(24, 22, 100);\n"
"}\n"
"")
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QtCore.QRect(580, 310, 191, 31))
        #self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	font: 25 13pt \"Segoe UI Light\";\n"
"background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	color:Black;\n"
"    font:;\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 0);    \n"
"	font: 12pt \"Segoe UI Semilight\";\n"
"	border: 1px solid rgb(64, 71, 88);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(24, 22, 100);\n"
"}\n"
"")
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QtCore.QRect(360, 310, 191, 31))
        #self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	font: 25 13pt \"Segoe UI Light\";\n"
"background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	color:Black;\n"
"    font:;\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 0);    \n"
"	font: 12pt \"Segoe UI Semilight\";\n"
"	border: 1px solid rgb(64, 71, 88);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(24, 22, 100);\n"
"}\n"
"")
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QtCore.QRect(120, 310, 191, 31))
        #self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	font: 25 13pt \"Segoe UI Light\";\n"
"background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	color:Black;\n"
"    font:;\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 0);    \n"
"	font: 12pt \"Segoe UI Semilight\";\n"
"	border: 1px solid rgb(64, 71, 88);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(24, 22, 100);\n"
"}\n"
"")
        self.pushButton_10.setAutoDefault(False)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QtCore.QRect(420, 60, 81, 61))
        self.frame_2.setStyleSheet(u"background:url(:/home/user (1).png)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_5.setDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_10.setDefault(False)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Admin Controls", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Account Settings", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Update Charges", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Travel Charges", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Print Balances", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Class Charges", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Room Charges", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_adminCtr()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
