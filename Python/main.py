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


#importing all the UIs

from ui_adminctrl import *
from ui_adminlogin import *
from ui_printing import *
from ui_telecomm import *
from ui_pinCheck import *
from ui_newuser import *
from ui_updateacc import *
from ui_deposit import *
from ui_updateChrgs import *
class loginpage(QMainWindow):
     def __init__(self):
         QMainWindow.__init__(self)
         self.ui = ui_adminLogin()
         self.ui.setupUi(self)
         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
         self.show()
         self.ui.pushButton_4.clicked.connect(self.check_correct)

     def check_correct(self):
         global id
         self.id = self.ui.lineEdit.text()
         self.password = self.ui.lineEdit_2.text()

         #make sql connection
         sql = sq.connect(host="localhost",
                          user="root",
                          password="sairam",
                          database="cashless")
         cursor = sql.cursor()
         cursor.execute("SELECT ID, PASSWORD, department FROM ADMIN_INFO WHERE ID=%s", (int(self.id),))


         for x in cursor:
             print(x[2])
             if self.id=="" or self.password=="":
                 msg = QMessageBox()
                 msg.setWindowTitle("INVALID ENTRY!!!")
                 msg.setText("wrong username or password ")
                 msg.setIcon(QMessageBox.Critical)
                 msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                 msg.buttonClicked.connect(self.popup)
                 x = msg.exec_()

             elif int(self.id) in x and int(self.password) in x:
                 if x[2] == "T":
                     self.main = telecomm()
                     self.main
                     self.close()
                 elif x[2] == "P":
                     self.main = printing()
                     self.main
                     self.close()
                 elif x[2] == "A":
                     self.main = main_admin()
                     self.main
                     self.close()

             else:
                 msg = QMessageBox()
                 msg.setWindowTitle("INVALID ENTRY!!!")
                 msg.setText("wrong username or password ")
                 msg.setIcon(QMessageBox.Critical)
                 msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                 msg.buttonClicked.connect(self.popup)
                 x = msg.exec_()
     def popup(self, i):
         if i.text() == "Close":
             self.close()
         elif i.text() == "Retry":
             self.ui.lineEdit.clear()
             self.ui.lineEdit_2.clear()
class printing(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_print()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.ui.comboBox.setEnabled(False)
        self.ui.dateEdit.setEnabled(False)
        self.ui.lineEdit_17.setEnabled(False)
        self.ui.lineEdit_18.setEnabled(False)
        self.ui.lineEdit_15.returnPressed.connect(self.onPressed)
        self.ui.lineEdit_17.returnPressed.connect(self.amtPressed)
        self.ui.pushButton_5.clicked.connect(self.btnPress)
        self.ui.pushButton_23.clicked.connect(self.clearDetails)

    def onPressed(self):
        sql = sq.connect(host="localhost",
                         user="root",
                         password="sairam",
                         database="cashless")
        cursor = sql.cursor()
        self.id = self.ui.lineEdit_15.text()
        if len(self.id)<5:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Enter a valid User ID")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
            msg.buttonClicked.connect(self.popup)
            x = msg.exec_()
            self.ui.lineEdit_15.clear()

        cursor.execute("SELECT name,id,password,balance FROM STUDENT_INFO WHERE id=%s", (int(self.id),))

        for x in cursor:
            print(x[2])
            global passw
            passw = str(x[2])
            global balance
            balance = x[3]
            global id
            id = x[1]
            if x != []:
                self.ui.lineEdit_16.setText(x[0])
                self.ui.lineEdit_15.setReadOnly(True)
                pixmap = QtGui.QPixmap('/Users/Admin/Desktop/GUI/Student pics/16001.png')
                self.ui.label_4.setPixmap(pixmap)
                self.ui.label_4.show()
                date = datetime.date.today()
                self.ui.dateEdit.setDate(date)
                self.ui.comboBox.setEnabled(True)
                self.ui.dateEdit.setEnabled(True)
                self.ui.lineEdit_17.setEnabled(True)
                self.ui.lineEdit_18.setEnabled(True)
                self.ui.lineEdit_18.setReadOnly(True)

            elif int(x) != int(x[1]):
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Enter a valid User ID")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                msg.buttonClicked.connect(self.popup)
                x = msg.exec_()
                self.ui.lineEdit_15.clear()
    def amtPressed(self):
        self.ui.lineEdit_17.returnPressed.connect(self.amtPressed)
        print("amt check")
        amt = self.ui.lineEdit_17.text()
        sides = self.ui.comboBox.currentText()
        if sides == "Single Sided":
            global tynx_amt
            tynx_amt = str(1 * int(amt))
            self.ui.lineEdit_18.setText(str(1 * int(amt)))
            self.ui.lineEdit_18.setReadOnly(True)
        elif sides == "Double sided":
            tynx_amt = str(2 * int(amt))
            self.ui.lineEdit_18.setText(str(2 * int(amt)))
            self.ui.lineEdit_18.setReadOnly(True)

    def popup(self, i):
        if i.text() == "Close":
            self.close()
        elif i.text() == "Retry":
            print("retry")
    def btnPress(self):
        text = self.ui.lineEdit_18.text()
        if len(text)>=1:
            if (int(balance)-int(tynx_amt))>=0:
                global dept
                dept = "P"
                self.ui.comboBox.setEnabled(False)
                self.ui.dateEdit.setEnabled(False)
                self.ui.lineEdit_17.setEnabled(False)
                self.ui.lineEdit_18.setEnabled(False)
                self.main = pin_check()
                self.main
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("You have insufficient balance")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                msg.buttonClicked.connect(self.popup)
                x = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please fill in all the details")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
            msg.buttonClicked.connect(self.popup)
            x = msg.exec_()

    def clearDetails(self):
        self.ui.lineEdit_15.clear()
        self.ui.lineEdit_16.clear()
        self.ui.lineEdit_17.clear()
        self.ui.lineEdit_18.clear()
        self.ui.label_4.clear()
        self.ui.dateEdit.clear()
        self.ui.lineEdit_15.setReadOnly(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.dateEdit.setEnabled(False)
        self.ui.lineEdit_17.setEnabled(False)
        self.ui.lineEdit_18.setEnabled(False)
class telecomm(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_telecomm()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.ui.lineEdit_17.setEnabled(False)
        self.ui.lineEdit_18.setEnabled(False)
        self.ui.lineEdit_19.setEnabled(False)
        self.ui.lineEdit_20.setEnabled(False)
        self.ui.lineEdit_15.returnPressed.connect(self.onPressed)
        self.ui.pushButton_5.clicked.connect(self.btnPress)
        self.ui.pushButton_23.clicked.connect(self.clearDetails)

    def onPressed(self):
        sql = sq.connect(host="localhost",
                         user="root",
                         password="sairam",
                         database="cashless")
        cursor = sql.cursor()
        self.id = self.ui.lineEdit_15.text()
        if len(self.id)<5:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Enter a valid User ID")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
            msg.buttonClicked.connect(self.popup)
            x = msg.exec_()
            self.ui.lineEdit_15.clear()

        cursor.execute("SELECT user_id,tele_pass,balance,name, tele_id FROM TELEPHONE WHERE user_id=%s", (int(self.id),))
        for x in cursor:
            global passw
            passw = x
            uid = int(self.ui.lineEdit_15.text())
            if uid not in x:
                print("false")
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Enter a valid User ID")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                msg.buttonClicked.connect(self.popup)
                x = msg.exec_()
                self.ui.lineEdit_15.clear()

            if str(x[0]) == str(self.ui.lineEdit_15.text()):
                print("true")
                self.ui.lineEdit_16.setText(str(x[3]))
                self.ui.lineEdit_19.setText(str(x[4]))
                self.ui.lineEdit_20.setText(str(x[1]))
                self.ui.lineEdit_17.setText(str(x[2]))
                self.ui.lineEdit_15.setReadOnly(True)
                self.ui.lineEdit_16.setReadOnly(True)
                self.ui.lineEdit_17.setReadOnly(True)
                self.ui.lineEdit_20.setReadOnly(True)
                self.ui.lineEdit_19.setReadOnly(True)
                pixmap = QtGui.QPixmap('/Users/Admin/Desktop/GUI/Student pics/16001.png')
                self.ui.label_4.setPixmap(pixmap)
                self.ui.label_4.show()
                date = datetime.date.today()
                self.ui.lineEdit_17.setEnabled(True)
                self.ui.lineEdit_18.setEnabled(True)
                self.ui.lineEdit_19.setEnabled(True)
                self.ui.lineEdit_20.setEnabled(True)
                self.ui.lineEdit_20.setReadOnly(True)
                self.ui.lineEdit_17.setReadOnly(True)

    def popup(self, i):
        if i.text() == "Close":
            self.close()
        elif i.text() == "Retry":
            print("retry")
    def btnPress(self):
        user_id = passw[0]
        sql = sq.connect(host="localhost",
                         user="root",
                         password="sairam",
                         database="cashless")
        cursor = sql.cursor()
        cursor.execute("SELECT balance FROM STUDENT_INFO WHERE id=%s", (user_id,))
        sq_data = cursor.fetchone()
        text = self.ui.lineEdit_18.text()
        if len(text)>=2:
            if (int(sq_data[0]) - int(text))>0:
                global tynx_amt
                global dept
                dept = "T"
                tynx_amt = int(self.ui.lineEdit_18.text())
                self.ui.lineEdit_17.setEnabled(False)
                self.ui.lineEdit_18.setEnabled(False)
                self.ui.lineEdit_20.setEnabled(False)
                self.ui.lineEdit_19.setEnabled(False)

                self.main = pin_check()
                self.main
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Insufficient balance")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                msg.buttonClicked.connect(self.popup)
                x = msg.exec_()
                self.ui.lineEdit_18.clear()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please fill in all the details")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
            msg.buttonClicked.connect(self.popup)
            x = msg.exec_()

    def clearDetails(self):
        self.ui.lineEdit_15.clear()
        self.ui.lineEdit_16.clear()
        self.ui.lineEdit_17.clear()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        self.ui.lineEdit_20.clear()
        self.ui.label_4.clear()
        self.ui.lineEdit_15.setReadOnly(False)
        self.ui.lineEdit_17.setEnabled(False)
        self.ui.lineEdit_18.setEnabled(False)
        self.ui.lineEdit_19.setEnabled(False)
        self.ui.lineEdit_20.setEnabled(False)
class pin_check(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_pinCheck()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(10)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.dropshadow.setGraphicsEffect(self.shadow)
        self.show()

        self.ui.label_tagline.setText("Your transaction amount is Rs."+str(tynx_amt))
        self.ui.pushButton.clicked.connect(self.btn_press)

    def btn_press(self):
        text = self.ui.lineEdit.text()
        if dept == "T":
            if text == str(passw[1]):
                sql = sq.connect(host="localhost",
                                 user="root",
                                 password="sairam",
                                 database="cashless")
                cursor = sql.cursor()
                user_id = (int(passw[0]),)
                cursor.execute("SELECT balance FROM STUDENT_INFO WHERE id=%s", user_id )
                sq_data = cursor.fetchall()
                print(sq_data)
                cur_bal = int(sq_data[0][0])
                user_id = int(user_id[0])
                updated_bal = cur_bal - int(tynx_amt)
                if updated_bal>=0:
                    # deduct balance
                    print(user_id, updated_bal,type(updated_bal), type(user_id))
                    cursor.execute("UPDATE STUDENT_INFO SET BALANCE=%s where id=%s ", (updated_bal,user_id))

                    #update telephone balance
                    cursor.execute("SELECT balance FROM telephone WHERE user_id=%s", (user_id,) )
                    sq_data = cursor.fetchall()
                    cur_bal = int(sq_data[0][0])
                    updated_bal = cur_bal+int(tynx_amt)
                    print(cur_bal, tynx_amt, updated_bal,user_id, type(user_id))
                    cursor.execute("UPDATE TELEPHONE SET BALANCE=%s where user_id=%s ",(updated_bal,user_id))
                    sql.commit()
                    cursor.close()
                    self.ui = telecomm()
                    self.show()
                    self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Wrong Password")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                msg.buttonClicked.connect(self.popup)
                x = msg.exec_()
                self.ui.lineEdit.clear()

        elif dept == "P":
            if str(text) == str(passw):
                sql = sq.connect(host="localhost",
                                 user="root",
                                 password="sairam",
                                 database="cashless")
                cursor = sql.cursor()
                updated_bal = (int(balance)-int(tynx_amt))
                Uid = int(id)
                data = (updated_bal,Uid)
                print(Uid,updated_bal)
                cursor.execute("UPDATE STUDENT_INFO SET BALANCE=%s where id=%s ",data)
                sql.commit()
                cursor.close()
                self.ui = printing()
                self.show()
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Wrong Password")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
                msg.buttonClicked.connect(self.popup)
                x = msg.exec_()
                self.ui.lineEdit.clear()
    def popup(self, i):
        if i.text() == "Close":
            self.close()
        elif i.text() == "Retry":
            print("retry")
class main_admin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_adminCtr()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.ui.pushButton_5.clicked.connect(self.deposit)

    def deposit(self):
        self.main = deposit()
        self.main
        self.close()
class deposit(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_deposit()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.ui.pushButton_23.clicked.connect(self.update_chrgs)

    def update_chrgs(self):
        self.main = updateChrgs()
        self.main
        self.close()

    def newUser(self):
        self.main = ui_newUser()
        self.main
        self.close()

class new_user(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_newUser()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

class update_user(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_updateAcc()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

if __name__=="__main__":
     app = QApplication(sys.argv)
     window = loginpage()
     sys.exit(app.exec_())