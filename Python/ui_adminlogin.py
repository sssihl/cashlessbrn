# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_adminctrlrPuanO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate,
QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt,
QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import homeicon_rc

class ui_adminLogin(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(389, 464)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 726, 489))
        self.frame.setMinimumSize(QSize(726, 489))
        self.frame.setMaximumSize(QSize(726, 489))
        self.frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame.setStyleSheet(u"background:url(:/home/admin login.png)")
        self.frame.setInputMethodHints(Qt.ImhNoEditMenu)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 220, 211, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI ")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(Qt.TabFocus)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(0,0,0);\n"
"    font: 80 11pt \"Segoe UI \";\n"
"	border-radius:5px;\n"
"background:rgb(255, 255, 255);\n"
"border:none;\n"
"box-shadow: 0px -3px 5px #a6a6a6;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"color:white;\n"
"    \n"
"	font: 500 13pt \"Segoe UI \";\n"
"border-radius:5px;\n"
"background:rgb(129, 196, 255)\n"
"}")
        self.lineEdit.setInputMethodHints(Qt.ImhNoTextHandles|Qt.ImhPreferNumbers)
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit.setProperty("onlyInt", 6)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 270, 211, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(0,0,0);\n"
"    font: 80 11pt \"Segoe UI \";\n"
"	border-radius:5px;\n"
"background:rgb(255, 255, 255);\n"
"border:none;\n"
"box-shadow: 0px -3px 5px #a6a6a6;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"color:white;\n"
"    \n"
"	font: 500 13pt \"Segoe UI \";\n"
"border-radius:5px;\n"
"background:rgb(129, 196, 255)\n"
"}")
        self.lineEdit_2.setMaxLength(5)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 340, 151, 31))
        font1 = QFont()
        font1.setFamily(u"Ebrima")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.NoAntialias)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color:white;\n"
"	background:rgb(20, 35, 83);\n"
"	border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:5px;\n"
"background:rgb(79, 155, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(160, 50, 81, 61))
        self.frame_2.setAcceptDrops(False)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background:url(:/home/user (1).png);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(100, 110, 191, 41))
        font2 = QFont()
        font2.setFamily(u"FONTSPRING DEMO - Grotesco Medium")
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background:transparent")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(130, 140, 131, 41))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background:transparent")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Login to access ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"dashboard", None))
    # retranslateUi

