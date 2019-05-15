import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DemoIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400,100)
        self.move(300, 300)
        self.setWindowTitle('Tugas Menyisipkan Icon')
        self.label = QLabel('<b>Bahasa Pemrograman Favorit Anda')

        icon1 = QIcon('python.png')
        self.button1 = QPushButton('\tPython')
        self.button1.setIcon(icon1)

        icon2 = QIcon('java.png')
        self.button2 = QPushButton('\tJava')
        self.button2.setIcon(icon2)

        icon3 = QIcon('php.png')
        self.button3 = QPushButton('\tPHP')
        self.button3.setIcon(icon3)

        icon4 = QIcon('c-plus-plus.png')
        self.button4 = QPushButton('\tC/C++')
        self.button4.setIcon(icon4)

        grid = QGridLayout()
        grid.addWidget(self.button1, 1,0)
        grid.addWidget(self.button2, 1,1)
        grid.addWidget(self.button3, 2,0)
        grid.addWidget(self.button4, 2,1)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(grid)
        self.setLayout(layout)

if __name__ == '__main__':
        a = QApplication(sys.argv)
        form = DemoIcon()
        form.show()
        a.exec_()
