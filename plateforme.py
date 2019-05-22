import datetime
import signal
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

signal.signal(signal.SIGINT, signal.SIG_DFL)

class Animated_window(QtWidgets.QWidget) :

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
        self.setWindowTitle("ISN: example")
        self.resize(800, 600)

    def create_game(self):
        self.platform = [
         [1,0,0],
         [0,0,1],
         [1,0,0],
        ]
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
            for y in range (0, 3) :
                for x in range (0, 3) :
                    if self.platform[y][x] == 1 :
                        path = QtGui.QPainterPath()
                        path.addRect(x*10, y*10, 10, 10)
                        qp.fillPath(path, QtGui.QColor(255, 0, 0))

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
    sys.exit(app.exec_())

input('Appuyez sur ENTREE pour quitter')

main() 
