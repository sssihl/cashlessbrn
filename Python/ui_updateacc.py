import datetime
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
import mysql.connector as sq


import homeicon_rc

class ui_updateAcc(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(726, 489)
        MainWindow.setMinimumSize(QSize(726, 489))
        MainWindow.setMaximumSize(QSize(726, 489))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 726, 489))
        self.frame.setStyleSheet(u"background:url(:/home/updateBg2.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_15 = QLineEdit(self.frame)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(360, 190, 131, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setAutoFillBackground(False)
        self.lineEdit_15.setStyleSheet(u"QLineEdit {\n"
"	background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_15.setMaxLength(32767)
        self.lineEdit_15.setCursorPosition(0)
        self.lineEdit_15.setReadOnly(False)
        self.lineEdit_16 = QLineEdit(self.frame)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(360, 230, 131, 31))
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setAutoFillBackground(False)
        self.lineEdit_16.setStyleSheet(u"QLineEdit {\n"
"	background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_16.setMaxLength(32767)
        self.lineEdit_16.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_16.setCursorPosition(0)
        self.lineEdit_16.setReadOnly(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 110, 231, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"		color:rgb(40,40, 40);\n"
"		font: 24pt \"FONTSPRING DEMO - Grotesco Book Bold\";\n"
"background:transparent;\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(320, 40, 81, 61))
        self.frame_2.setStyleSheet(u"background:url(:/home/user.png)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 190, 91, 31))
        self.label_3.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 230, 111, 31))
        self.label_4.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 270, 201, 31))
        self.label_5.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_17 = QLineEdit(self.frame)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(360, 270, 131, 31))
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setAutoFillBackground(False)
        self.lineEdit_17.setStyleSheet(u"QLineEdit {\n"
"	background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_17.setMaxLength(32767)
        self.lineEdit_17.setEchoMode(QLineEdit.Password)
        self.lineEdit_17.setCursorPosition(0)
        self.lineEdit_17.setReadOnly(False)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(280, 330, 151, 41))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	color:White;\n"
"    font: 500 12pt \"Segoe UI \";\n"
"	background:rgb(24, 22, 100);\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 0);\n"
"    \n"
"	font: 500 12pt \"Segoe UI \";\n"
"border-radius:5px;\n"
"background:white;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_23 = QPushButton(self.frame)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(280, 420, 131, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.pushButton_23.setFont(font1)
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet(u"QPushButton{\n"
"background:transparent;\n"
"	font: 12pt \"Segoe UI\";\n"
"color:rgb(80,80,80);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{;\n"
"	font: 12.5pt \"Segoe UI\";\n"
"text-decoration: underline;\n"
"}\n"
"QPushButton:pressed {	\n"
"	color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_24 = QPushButton(self.frame)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(280, 430, 131, 41))
        self.pushButton_24.setFont(font1)
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"background:transparent;\n"
"	font: 12pt \"Segoe UI\";\n"
"color:rgb(80,80,80);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{;\n"
"	font: 13pt \"Segoe UI\";\n"
"text-decoration: underline;\n"
"}\n"
"QPushButton:pressed {	\n"
"	color: rgb(85, 170, 255);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_15.setInputMask("")
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.lineEdit_16.setInputMask("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Update Account", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" User ID :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Re enter Password :", None))
        self.lineEdit_17.setInputMask("")
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Update  User", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"New User", None))
    # retranslateUi

