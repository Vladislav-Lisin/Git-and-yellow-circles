import sys
import random as rd

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.Button.clicked.connect(self.paintcircle)
        self.should_paint_circle = False

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            qp = QPainter(self)
            qp.begin(self)

            self.draw_flag(qp)
            qp.end()

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()

    def draw_flag(self, qp):
        for i in range(10):
            rs = rd.randint(50, 150)
            x = rd.randint(10, 500)
            y = rd.randint(10, 500)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, rs, rs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
