import sys
from PyQt4.QtGui import *

from tictac import *


class Slot(QLineEdit):
    def __init__(self, x, y):
        super(QLineEdit, self).__init__()
        self.x = x
        self.y = y
        self.xPlacement = x + 1
        self.yPlacement = y + 1
        self.textChanged.connect(lambda i: self.textchanged(self.text(), self.x, self.y))

    def textchanged(self, text, x, y):
        tictac[x][y] = text
        validate_winner(tictac)

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    topLeft = Slot(0, 0)
    grid.addWidget(topLeft, topLeft.xPlacement, topLeft.yPlacement)

    topMiddle = Slot(0, 1)
    grid.addWidget(topMiddle, topMiddle.xPlacement, topMiddle.yPlacement)

    topRight = Slot(0, 2)
    grid.addWidget(topRight, topRight.xPlacement, topRight.yPlacement)

    middleLeft = Slot(1, 0)
    grid.addWidget(middleLeft, middleLeft.xPlacement, middleLeft.yPlacement)

    middleMiddle = Slot(1, 1,)
    grid.addWidget(middleMiddle, middleMiddle.xPlacement, middleMiddle.yPlacement)

    middleRight = Slot(1, 2)
    grid.addWidget(middleRight, middleRight.xPlacement, middleRight.yPlacement)

    bottomLeft = Slot(2, 0,)
    grid.addWidget(bottomLeft, bottomLeft.xPlacement, bottomLeft.yPlacement)

    bottomMiddle = Slot(2, 1)
    grid.addWidget(bottomMiddle, bottomMiddle.xPlacement, bottomMiddle.yPlacement)

    bottomRight = Slot(2, 2)
    grid.addWidget(bottomRight, bottomRight.xPlacement, bottomRight.yPlacement)

    win.setLayout(grid)
    win.setWindowTitle("TicTac")
    win.show()

    sys.exit(app.exec_())





if __name__ == '__main__':
    window()