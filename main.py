from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        print('a')
        circle = QPainter(self)
        #r = randint(0, 250)
        circle.setPen(QPen(Qt.green, 8, Qt.SolidLine))
        #circle.drawEllipse(randint(0, 400 - r), randint(0, 300 - r), r, r)
        circle.drawEllipse(0, 0, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())
