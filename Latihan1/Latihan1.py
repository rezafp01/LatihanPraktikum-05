import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DemoGambar(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 600)
        self.move(300, 300)
        self.setWindowTitle('Tugas Praktikum Menyisipkan Gambar')
        self.label1 = QLabel('<h1><font color=purple> Logo FTII :</font></h1>')
        self.label2 = QLabel('<img src="ftii.png">')
        self.label3 = QLabel('<h1><font color=red> Logo FTTE :</font></h1>')
        self.label4 = QLabel('<img src="ftte.png">')


        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        self.setLayout(layout)

if __name__ == '__main__':
        a = QApplication(sys.argv)
        form = DemoGambar()
        form.show()
        a.exec_()
