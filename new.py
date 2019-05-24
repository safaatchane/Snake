import datetime
import signal
import math
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

signal.signal(signal.SIGINT, signal.SIG_DFL)


    
class Animated_window(QtWidgets.QWidget) :
    

        
     def create_game(self):
        self.platform.resize(800,600)
        self.platform = [
         [6,2], 
         [5,2],
         [5.3],     
        ]
        self.bodysnake =[]
        self.bodysnake.append((6,2))
        self.bodysnake.append((5,2))
        self.bodysnake.append((5,3))
        self.bodysnake.append((5,4))
        self.bodysnake.append((5,5))
        self.bodysnake.append((4,5))
        self.bodysnake.append((3,5))
        
        
    def __init__(self) :
        super().__init__()
        self.create_game()
        self.create_contents()
        self.show()
        framerate = 60
        self.animation_start = datetime.datetime.now()
        self.animation_timer = QtCore.QTimer()
        self.animation_timer.timeout.connect(self.animation_step)
        self.animation_timer.start(1000 / framerate)

    def create_contents(self) :
        self.time = 0
        self.speed = 0.1
        self.setWindowTitle("ISN: example")
        self.resize(800, 600)
        
     
    def animation_step(self) :
        time = datetime.datetime.now() - self.animation_start
        self.time = time.total_seconds()
        self.update()

    def paintEvent(self, event) :
        try :
            qp = QtGui.QPainter()
            qp.begin(self)
            qp.setRenderHints(QtGui.QPainter.Antialiasing, 1)
            path = QtGui.QPainterPath()
            path.addRect(10, 10, 780, 580)
            qp.fillPath(path, QtGui.QColor(255, 255, 255))
            #qp.drawPath(path)
            print(self.platform[0][0])
            for y in range (0, len(self.platform)) :
                for x in range (0, len(self.platform)) :
                    if self.platform[y][x] == 1 :
                        path = QtGui.QPainterPath()
                        path.addRect(x*10, y*10, 10, 10)
                        qp.fillPath(path, QtGui.QColor(0, 0, 0))

        except Exception as e :
            print("Erreur:", e)



    def keyPressEvent(self, event):
        key = event.key()
        #print(key)
        if key == QtCore.Qt.Key_Q:
            self.close()
        elif key == QtCore.Qt.Key_Plus :
            self.speed = self.speed + 0.01
        elif key == QtCore.Qt.Key_Minus :
            self.speed = self.speed - 0.01

    def keyReleaseEvent(self, event):
        return

def main() :
    app = QtWidgets.QApplication(sys.argv)
    clock = Animated_window()
    sys.exit(app.exec_())
       

main() 
