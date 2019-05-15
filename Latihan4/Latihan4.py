import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class FormHitung(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Tugas QRadioButton')

        self.label1 = QLabel()
        self.label1.setText('Bilangan pertama')
        self.bilPetama = QLineEdit()
        self.bilPetama.setValidator(QIntValidator())


        self.label2 = QLabel()
        self.label2.setText('Bilangan kedua')
        self.bilKedua = QLineEdit()
        self.bilKedua.setValidator(QIntValidator())

        grid = QGridLayout()
        grid.addWidget(self.label1,0,0)
        grid.addWidget(self.bilPetama,0,1)
        grid.addWidget(self.label2,1,0)
        grid.addWidget(self.bilKedua,1,1)


        self.cekTambah = QRadioButton('&Tambah')
        self.cekTambah.setChecked(True)
        self.cekKurang = QRadioButton('&Kurang')
        self.cekKali = QRadioButton('&Kali')
        self.cekBagi = QRadioButton('&Bagi')

        hbox = QHBoxLayout()
        hbox.addWidget(self.cekTambah)
        hbox.addWidget(self.cekKurang)
        hbox.addWidget(self.cekKali)
        hbox.addWidget(self.cekBagi)

        self.resultLabel = QLabel('<b>Hasil: </b>')
        self.checkButton = QPushButton('Hitung')

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        horizontalLine = QFrame();
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(horizontalLine)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.checkButton)
        layout.addStretch()

        self.setLayout(layout)
        self.checkButton.clicked.connect(self.checkButtonClick)

    def checkButtonClick(self):
        one = int(self.bilPetama.text())
        two = int(self.bilKedua.text())
        if self.cekTambah.isChecked():
            res = one+two
            self.resultLabel.setText('<b>Hasil Pertambahan : </b>'+str(res))
        elif self.cekKurang.isChecked():
            res = one - two
            self.resultLabel.setText('<b>Hasil Pengurangan : </b>'+str(res))
        elif self.cekKali.isChecked():
            res = one * two
            self.resultLabel.setText('<b>Hasil Perkalian : </b>'+str(res))
        else:
            res = one / two
            self.resultLabel.setText('<b>Hasil Pembagian : </b>'+str(res))


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = FormHitung()
    form.show()
    a.exec_()
