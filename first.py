from design import Ui_Form
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor

class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = 0
        self.y = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.pushButton.clicked.connect(self.generate)

    def paintEvent(self, d):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(self.r, self.g, self.b))
        self.randomize()
        radius = random.randint(40, 120)
        qp.drawEllipse(self.x, self.y, radius, radius)

    def randomize(self):
        self.x = random.randint(0, 590)
        self.y = random.randint(0, 457)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def generate(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = Widget()
    wid.show()
    sys.exit(app.exec())