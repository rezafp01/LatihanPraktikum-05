import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Penggunaan QTextEdit')

        vbox1 = QVBoxLayout()
        self.label1 = QLabel('Dari')
        self.phoneEdit1 = QLineEdit()
        self.label2 = QLabel('Untuk')
        self.phoneEdit2 = QLineEdit()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.phoneEdit1)
        vbox1.addWidget(self.label2)
        vbox1.addWidget(self.phoneEdit2)

        horizontalLine1 = QFrame();
        horizontalLine1.setFrameShape(QFrame.HLine)
        horizontalLine1.setFrameShadow(QFrame.Sunken)

        self.label3 = QLabel('')
        self.messageEdit = QTextEdit()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label3)
        vbox2.addWidget(self.messageEdit)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(vbox1)
        vbox3.addWidget(horizontalLine1)
        vbox3.addLayout(vbox2)

        horizontalLine = QFrame();
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)

        self.sendButton = QPushButton('&Kirim SMS')
        self.cancelButton = QPushButton('&Batal')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.sendButton)
        hbox.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addLayout(vbox3)
        layout.addWidget(horizontalLine)
        layout.addLayout(hbox)
        self.setLayout(layout)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
