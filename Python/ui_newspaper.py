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
        MainWindow.setMinimumSize(QSize(605, 385))
        MainWindow.setMaximumSize(QSize(605, 385))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 611, 563))
        self.frame.setStyleSheet(u"background:url(:/home/news2.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 100, 271, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"		color:rgb(71, 71, 71);\n"
"		font: 22pt \"FONTSPRING DEMO - Grotesco Book \";\n"
"background:transparent;\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(260, 30, 81, 81))
        self.frame_2.setStyleSheet(u"background:url(:/home/news.png)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 210, 91, 31))
        self.label_5.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
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
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 170, 151, 31))
        self.label_7.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(300, 170, 131, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"color:rgb(116, 116, 116);\n"
"	background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QRect(300, 210, 131, 31))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"color:rgb(116, 116, 116);\n"
"	background:WHITE;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(230, 280, 151, 41))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_5.setDefault(False)
        self.pushButton_6.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"New Paper Charges", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" Paper :", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"   Room No. :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"A2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"A3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"A4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"A5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"A6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"A7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"A8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"B1", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"B2", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"B3", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"B4", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"B5", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"B6", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"B7", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"B8", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"C1", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"C2", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"C3", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"C4", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"C5", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("MainWindow", u"C6", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("MainWindow", u"C7", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("MainWindow", u"C8", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Hindu", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"ET Only", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"ET with Wealth", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Hindu and ET only", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Hindu and ET With Wealth", None))
        self.comboBox_2.setItemText(5, "")

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Deduct", None))
    # retranslateUi

