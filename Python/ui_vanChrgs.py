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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(605, 385)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 605, 385))
        self.frame.setStyleSheet(u"background:url(:/home/news2.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 90, 151, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"		color:rgb(71, 71, 71);\n"
"		font: 21pt \"FONTSPRING DEMO - Grotesco Book \";\n"
"background:transparent;\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(270, 20, 81, 81))
        self.frame_2.setStyleSheet(u"background:url(:/home/front-of-bus.png)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(220, 440, 151, 41))
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
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(230, 310, 151, 41))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_6.setAutoDefault(False)
        self.lineEdit_20 = QLineEdit(self.frame)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(300, 240, 81, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet(u"QLineEdit {\n"
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
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 240, 101, 31))
        self.label_11.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 15pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_21 = QLineEdit(self.frame)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(300, 200, 191, 31))
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setAutoFillBackground(False)
        self.lineEdit_21.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_21.setMaxLength(32767)
        self.lineEdit_21.setCursorPosition(0)
        self.lineEdit_21.setReadOnly(True)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 200, 131, 31))
        self.label_9.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 15pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_23 = QLineEdit(self.frame)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(300, 160, 111, 31))
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setAutoFillBackground(False)
        self.lineEdit_23.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_23.setMaxLength(32767)
        self.lineEdit_23.setCursorPosition(0)
        self.lineEdit_23.setReadOnly(False)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 160, 91, 31))
        self.label_10.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 15pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_5.setDefault(False)
        self.pushButton_6.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Van Charges", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Deduct", None))
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amt", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"  Amount :", None))
        self.lineEdit_21.setInputMask("")
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Name :", None))
        self.lineEdit_23.setInputMask("")
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"   User ID :", None))
    # retranslateUi

