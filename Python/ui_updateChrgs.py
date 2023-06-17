from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate,
QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt,
QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import homeicon_rc

class updateChrgs(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 580)
        MainWindow.setMinimumSize(QSize(580, 580))
        MainWindow.setMaximumSize(QSize(580, 580))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 580, 580))
        self.frame.setStyleSheet(u"background:url(:/home/updatechargsBg.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 120, 201, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"		color:rgb(71, 71, 71);\n"
"		font: 22pt \"FONTSPRING DEMO - Grotesco Book bold \";\n"
"background:transparent;\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(250, 50, 70, 70))
        self.frame_2.setStyleSheet(u"background:url(:/home/updatechrg.png)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 200, 91, 31))
        self.label_4.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_17 = QLineEdit(self.frame)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(300, 200, 111, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
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
        self.lineEdit_17.setCursorPosition(0)
        self.lineEdit_17.setReadOnly(False)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 240, 141, 31))
        self.label_5.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_18 = QLineEdit(self.frame)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(300, 240, 111, 31))
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
        self.lineEdit_19 = QLineEdit(self.frame)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(300, 280, 111, 31))
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
        self.lineEdit_20.setGeometry(QRect(300, 320, 111, 31))
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
        self.lineEdit_20.setCursorPosition(0)
        self.lineEdit_20.setReadOnly(False)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 360, 101, 31))
        self.label_8.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_21 = QLineEdit(self.frame)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(300, 360, 111, 31))
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
        self.lineEdit_21.setReadOnly(False)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(180, 400, 111, 31))
        self.label_9.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.lineEdit_22 = QLineEdit(self.frame)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(300, 400, 111, 31))
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setAutoFillBackground(False)
        self.lineEdit_22.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_22.setMaxLength(32767)
        self.lineEdit_22.setCursorPosition(0)
        self.lineEdit_22.setReadOnly(False)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(220, 480, 151, 41))
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
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 280, 141, 31))
        self.label_6.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 320, 171, 31))
        self.label_7.setStyleSheet(u"QLabel{\n"
"		color:rgb(25, 25, 25);\n"
"		font: 16pt \"FONTSPRING DEMO - Grotesco Book\";\n"
"background:transparent;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Update Charges", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Printing :", None))
        self.lineEdit_17.setInputMask("")
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" Bus Charges :", None))
        self.lineEdit_18.setInputMask("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.lineEdit_19.setInputMask("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.lineEdit_20.setInputMask("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ET Wealth :", None))
        self.lineEdit_21.setInputMask("")
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"The Hindu :", None))
        self.lineEdit_22.setInputMask("")
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" Van Charges :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Economic Times :", None))
    # retranslateUi

