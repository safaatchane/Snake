import datetime
import math
import signal
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

signal.signal(signal.SIGINT, signal.SIG_DFL)

class Animated_window(QtWidgets.QWidget) :

    def __init__(self) :
        super().__init__()
        self.create_contents()
        self.show()
        framerate = 10
        self.animation_start = datetime.datetime.now()
        self.animation_timer = QtCore.QTimer()
        self.animation_timer.timeout.connect(self.animation_step)
        self.animation_timer.start(1000 / framerate)

    def create_contents(self) :
        self.time = 0
        self.speed = 0.1
        self.setWindowTitle("ISN: example")
        self.resize(800, 600)
        #box = QtWidgets.QVBoxLayout(self)
        #box.setContentsMargins(0, 0, 0, 0)
        #self.button = QtWidgets.QPushButton()
        #box.addWidget(self.draw)

    def animation_step(self) :
        time = datetime.datetime.now() - self.animation_start
        self.time = time.total_seconds()
        self.update()

    def paintEvent(self, event) :
        size = self.size()
        w = size.width()
        h = size.height()
        a = 2 * math.pi * self.speed * self.time
        x = w * (math.cos(a) + 1) / 2
        y = h * (math.sin(a) + 1) / 2
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHints(QtGui.QPainter.Antialiasing, 1)
        #pen = QtGui.QPen(QtGui.QColor(255, 128, 0))
        #qp.setPen(pen)
        path = QtGui.QPainterPath()
        path.moveTo(x + 50, y)
        path.lineTo(x, y + 50)
        path.lineTo(x - 50, y)
        path.lineTo(x, y - 50)
        path.closeSubpath()
        qp.fillPath(path, QtGui.QColor(255, 128, 0))
        #qp.drawPath(path)
        qp.end()

    def keyPressEvent(self, event):
        key = event.key()
        #print(key)
        if key == QtCore.Qt.Key_Q :
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

main()
