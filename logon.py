#logon.py
#1st error wrong import because QApplication was not found.
#2nd error is simmilar to first as didn't import QWidget.


#Importing modules required for the Gui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
import PyQt5.QtCore
import sys

#Creating a main function for program execution
def main():

    #specifying window parameters
    program = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(600,400)
    widget.setWindowTitle("logon.py")
    widget.show()

    #writing label to window
    label = QLabel(widget)
    label.setFont(QFont("Arial Font", 10))
    label.move(170,75)
    label.setText("Hello, would you like to login or register")
    label.show()

    #wiring buttons to screen
    btn = QPushButton(widget)
    btn.setFont(QFont("Arial Font", 15))
    btn.setText("Register")
    btn.setGeometry(100, 200, 190, 40)
    btn.move(200,200)
    btn.show()

    #wiring second buttons to screen
    btn_2 = QPushButton(widget)
    btn_2.setFont(QFont("Arial Font", 15))
    btn_2.setText("Login")
    btn_2.setGeometry(100, 200, 190, 40)
    btn_2.move(200,250)
    btn_2.show()
    
    def btn_login():
        pass
        
    def btn_regist():
        pass
        
    btn.clicked.connect(btn_login)
    
    btn_2.clicked.connect(btn_regist)


    sys.exit(program.exec_())

#Executing program
if __name__ == "__main__":
    main()  
    
