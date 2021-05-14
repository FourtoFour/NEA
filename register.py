#register.py

#Importing modules required for the Gui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
import PyQt5.QtCore
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

    

    program.setStyle("fusion")
    sys.exit(program.exec_())

#Executing program
if __name__ == "__main__":
    main()  
