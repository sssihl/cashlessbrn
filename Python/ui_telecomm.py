from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate,
QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt,
QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import homeicon_rc

class ui_telecomm(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 541)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 738, 543))
        self.frame.setStyleSheet(u"background:url(:/home/telecommBg.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(530, 110, 81, 81))
        self.label_4.setStyleSheet(u"background:url(:/home/image.png);")
        self.lineEdit_15 = QLineEdit(self.frame)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(260, 120, 111, 31))
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
        self.lineEdit_15.setMaxLength(5)
        self.lineEdit_15.setCursorPosition(0)
        self.lineEdit_15.setReadOnly(False)
        self.lineEdit_16 = QLineEdit(self.frame)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(260, 160, 251, 31))
        self.lineEdit_16.setFont(font)
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
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_19 = QLineEdit(self.frame)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(390, 280, 111, 31))
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setAutoFillBackground(False)
        self.lineEdit_19.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_19.setMaxLength(32767)
        self.lineEdit_19.setCursorPosition(0)
        self.lineEdit_19.setReadOnly(False)
        self.lineEdit_20 = QLineEdit(self.frame)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(390, 320, 111, 31))
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setAutoFillBackground(False)
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
        self.lineEdit_20.setMaxLength(32767)
        self.lineEdit_20.setEchoMode(QLineEdit.Normal)
        self.lineEdit_20.setCursorPosition(0)
        self.lineEdit_20.setReadOnly(False)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 520, 101, 21))
        self.label_10.setStyleSheet(u"QLabel{\n"
"		color:rgb(85, 85, 85);\n"
"		font: 9pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_17 = QLineEdit(self.frame)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(390, 360, 81, 31))
        self.lineEdit_17.setFont(font)
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
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_18 = QLineEdit(self.frame)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(390, 400, 81, 31))
        self.lineEdit_18.setFont(font)
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
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(290, 450, 151, 41))
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 160, 161, 31))
        self.label_2.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 320, 101, 31))
        self.label_7.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 15pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 360, 161, 31))
        self.label_8.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 15pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 120, 91, 31))
        self.label_3.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 230, 171, 31))
        self.label_5.setStyleSheet(u"QLabel{\n"
"		color:rgb(71, 71, 71);\n"
"		font: 18pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 50, 281, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"		color:rgb(71, 71, 71);\n"
"		font: 22pt \"FONTSPRING DEMO - Grotesco Book Bold\";\n"
"background:transparent;\n"
"}")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 280, 121, 31))
        self.label_6.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 15pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 400, 101, 31))
        self.label_9.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 15pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.pushButton_23 = QPushButton(self.frame)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(300, 500, 131, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.pushButton_23.setFont(font1)
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet(u"QPushButton{\n"
                                         "background:transparent;\n"
                                         "	font: 8pt \"Segoe UI\";\n"
                                         "color:rgb(80,80,80);\n"
                                         "border-radius:10px;\n"
                                         "}\n"
                                         "QPushButton:hover{;\n"
                                         "	font: 9.5pt \"Segoe UI\";\n"
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
        self.label_4.setText("")
        self.lineEdit_15.setInputMask("")
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Student Name", None))
        self.lineEdit_19.setInputMask("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telephone ID", None))
        self.lineEdit_20.setInputMask("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Operated by:", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amt", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"DEDUCT", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Clear details", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Student Name :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" Current Balance :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" User ID :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Account Details", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Telecomm Deartment", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Telephone ID :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" Amount :", None))
    # retranslateUi

