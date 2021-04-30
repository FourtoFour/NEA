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
    label.setText("Hello, would you like to login or register")
    label.show()

    #wiring buttons to screen
    btn = QPushButton(widget)
    btn.setFont(QFont("Arial Font", 5))
    btn.setText("Login")
    btn.setGeometry(200, 150, 100, 40)
    btn.move(200,200)
    btn.show()


    sys.exit(program.exec_())

#Executing program
if __name__ == "__main__":
    main()  
    
