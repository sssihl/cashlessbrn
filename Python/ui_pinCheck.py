from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate,
QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt,
QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import homeicon_rc

class ui_pinCheck(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(439, 259)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dropshadow = QFrame(self.centralwidget)
        self.dropshadow.setObjectName(u"dropshadow")
        self.dropshadow.setGeometry(QRect(10, 10, 421, 231))
        self.dropshadow.setStyleSheet(u"QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 0, 127, 255), stop:1 rgba(105, 0, 170, 255));\n"
"color:rgb(220,220,220);\n"
"border-radius:10px;\n"
"}")
        self.dropshadow.setFrameShape(QFrame.StyledPanel)
        self.dropshadow.setFrameShadow(QFrame.Raised)
        self.label_tagline = QLabel(self.dropshadow)
        self.label_tagline.setObjectName(u"label_tagline")
        self.label_tagline.setGeometry(QRect(40, 40, 301, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.label_tagline.setFont(font)
        self.label_tagline.setStyleSheet(u"color:rgb(227, 227, 227);\n"
"background-color:transparent")
        self.label_tagline.setAlignment(Qt.AlignCenter)
        self.label_tagline_2 = QLabel(self.dropshadow)
        self.label_tagline_2.setObjectName(u"label_tagline_2")
        self.label_tagline_2.setGeometry(QRect(110, 80, 191, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(20)
        self.label_tagline_2.setFont(font1)
        self.label_tagline_2.setStyleSheet(u"color:rgb(227, 227, 227);\n"
"background-color:transparent")
        self.label_tagline_2.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.dropshadow)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 120, 141, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.lineEdit.setFont(font2)
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(255, 0, 255);\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.pushButton = QPushButton(self.dropshadow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 180, 75, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color:rgb(170, 0, 127);\n"
"    font: 500 8pt \"Segoe UI \";\n"
"	background:white;\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:white;\n"
"    \n"
"	font: 500 10pt \"Segoe UI \";\n"
"border-radius:5px;\n"
"background:qconicalgradient(cx:1, cy:1, angle:0, stop:0.164773 rgba(255, 0, 255, 255), stop:1 rgba(170, 85, 255, 255))\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_tagline.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Your transaction amount is</span></p></body></html>", None))
        self.label_tagline_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">ENTER</span> PIN :</p></body></html>", None))
        self.lineEdit.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

