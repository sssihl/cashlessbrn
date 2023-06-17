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
        MainWindow.resize(605, 563)
        MainWindow.setMinimumSize(QSize(605, 563))
        MainWindow.setMaximumSize(QSize(605, 563))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 611, 563))
        self.frame.setStyleSheet(u"background:url(:/home/classChrgs.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 120, 241, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"		color:rgb(71, 71, 71);\n"
"		font: 24pt \"FONTSPRING DEMO - Grotesco Book \";\n"
"background:transparent;\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(250, 40, 80, 80))
        self.frame_2.setStyleSheet(u"background:url(:/home/group.png)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEdit_18 = QLineEdit(self.frame)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(300, 250, 111, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setAutoFillBackground(False)
        self.lineEdit_18.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_18.setMaxLength(32767)
        self.lineEdit_18.setCursorPosition(0)
        self.lineEdit_18.setReadOnly(False)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 200, 71, 31))
        self.label_4.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 250, 91, 31))
        self.label_5.setStyleSheet(u"QLabel{\n"
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
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(300, 200, 141, 31))
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
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 350, 111, 31))
        self.label_6.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_16 = QLineEdit(self.frame)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(300, 350, 131, 31))
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
        self.lineEdit_16.setEchoMode(QLineEdit.Password)
        self.lineEdit_16.setCursorPosition(0)
        self.lineEdit_16.setReadOnly(False)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 300, 111, 31))
        self.label_3.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_15 = QLineEdit(self.frame)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(300, 300, 131, 31))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Class Charges", None))
        self.lineEdit_18.setInputMask("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" Purpose :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"B.Com.(Hons.) I", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"B.Com.(Hons.)II", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"B.Com.(Hons.) III", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BSc.(Hons.) I", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"BSc.(Hons.) II", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"BSc.(Hons.) Maths", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"BSc.(Hons.) Physics", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"BSc.(Hons.) Chem.", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"BSc.(Hons.) Bio.", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.lineEdit_16.setInputMask("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" Admin ID :", None))
        self.lineEdit_15.setInputMask("")
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Admin ID", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

