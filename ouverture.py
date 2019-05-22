import sys 
from PyQt5 import QtGui, QtWidgets

def on_va_voir():
    global click_count
    click_count = click_count + 1
    print("on a vu", click_count, "fois" )
    
def main() : 
    
    def create_button(x, y, t, cb) :
        button = QtWidgets.QPushButton("Play" , window)
        button.move(230 + 0*x, 250+ 0*y ) 
        button.resize(150, 100)
        button.clicked.connect(on_va_voir)
        
    global click_count
    click_count = 0
    global window
    global button
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.resize(600, 600)
    
    create_button (0, 0, "C",   on_va_voir)
    
    
    window.show()
    sys.exit(app.exec_())


main()
