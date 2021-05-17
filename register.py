#register.py

#Importing modules required for the Gui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import PyQt5.QtCore
import urllib.request
import requests
import datetime
import sqlite3
import sys



    
#Creating a main function for program execution
def main():

    #specifying window parameters
    program = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(375,200)
    widget.setWindowTitle("register.py")
    widget.show()

    #writing label to window
    label = QLabel(widget)
    label.setFont(QFont("Arial Font", 9.5))
    label.move(50,30)
    label.setText("Please Register with a username and password.")
    label.show()

    #username labels

    label_2 = QLabel(widget)
    label_2.setFont(QFont("Arial Font", 9.5))
    label_2.move(50,67.5)
    label_2.setText("Username ")
    label_2.show()

    #password labels

    label_3 = QLabel(widget)
    label_3.setFont(QFont("Arial Font", 9.5))
    label_3.move(50,97.5)
    label_3.setText("Password ")
    label_3.show()
    

    #wiring lineEdit to screen
    ent = QLineEdit(widget)
    ent.setGeometry(100, 200, 175, 20)
    ent.move(125,67.5)
    ent.show()

    
    #wiring second lineEdit to screen
    ent_2 = QLineEdit(widget)
    ent_2.setEchoMode(QLineEdit.Password)
    ent_2.setGeometry(100, 200, 175, 20)
    ent_2.move(125, 97.5)
    ent_2.show()

    #Register button
    btn = QPushButton(widget)
    btn.setText("Register...")
    btn.setGeometry(100, 200, 100,25)
    btn.move(150, 127.5)
    btn.show()

    #clicked button function
    def btn_clicked():
        print(ent.text())
        print(ent_2.text())
        if ent.text() == "":
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Enter a Username")
            msg.setWindowTitle("Warning")
            msg.exec_()
            
            
        elif ent_2.text() == "":
            
            msg_2 = QMessageBox()
            msg_2.setIcon(QMessageBox.Warning)
            msg_2.setText("Enter a Password")
            msg_2.setWindowTitle("Warning")
            msg_2.exec_()
            
        elif len(ent.text()) < 4:
            
            msg_3 = QMessageBox()
            msg_3.setIcon(QMessageBox.Warning)
            msg_3.setText("Username is less than 4 characters")
            msg_3.setWindowTitle("Warning")
            msg_3.exec_()
            
        elif len(ent.text()) > 16:
            
            msg_4 = QMessageBox()
            msg_4.setIcon(QMessageBox.Warning)
            msg_4.setText("Username is more than 16 characters")
            msg_4.setWindowTitle("Warning")
            msg_4.exec_()
            
        elif len(ent_2.text()) < 4:
            
            msg_5 = QMessageBox()
            msg_5.setIcon(QMessageBox.Warning)
            msg_5.setText("Password is less than 4 characters")
            msg_5.setWindowTitle("Warning")
            msg_5.exec_()
            
        elif len(ent_2.text()) > 16:
            
            msg_6 = QMessageBox()
            msg_6.setIcon(QMessageBox.Warning)
            msg_6.setText("Password is more than 16 characters")
            msg_6.setWindowTitle("Warning")
            msg_6.exec_()
            
        else:
            
            msg_7 = QMessageBox()
            msg_7.setIcon(QMessageBox.Information)
            msg_7.setText("Registration success!")
            msg_7.setWindowTitle("Information")
            msg_7.exec_()
            
            #storage of credentials

            #sourcing client ip for location storage
            client_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

            print(client_ip)

            req = requests.get("http://ip-api.com/json/"+client_ip+"?fields=countryCode")

            print(req.text)

            #sourcing the date for account creation storage

            cur_date=datetime.datetime.now()

            cur_day = cur_date.strftime("%d")
            cur_mnth = cur_date.strftime("%m")
            cur_yr = cur_date.strftime("%G")

            cur_add = cur_day+cur_mnth+cur_yr

            print(cur_add)


            

            #inputting data into database

            
               
            db_con = sqlite3.connect(r"\\canonschool.internal\ud$\Students\Work\2015\mathew.john15\Downloads\nea_db.db")
    
            nav = db_con.cursor()
    
            sql = ('INSERT INTO Users(Username, Password, Creation_Locale, Creation_date) VALUES(%s, %s, %d, %d );')

            val = (ent,ent_2,req.text,cur_add)

            nav.execute(sql, val)
            

            db_con.commit()

            nav.close()

            db_con.close()
            
            
        



    btn.clicked.connect(btn_clicked)
    
    program.setStyle("fusion")
    
    sys.exit(program.exec_())

#Executing program
if __name__ == "__main__":
    main()  
