import sys

import easygui
from PyQt6 import uic, QtCore
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QGridLayout, QWidget, QLabel, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap

from Gui_Signature.back import libFunctions

Form, _ = uic.loadUiType(r"C:\Users\bulyn\PycharmProjects\pythonProject1\Gui_Signature\1.ui")


class Ui(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.orig_sign_button.clicked.connect(self.open_true_sign)
        self.check_sign_button.clicked.connect(self.open_sign)
        self.hbox1 = QHBoxLayout(self.frame)
        self.hbox2 = QHBoxLayout(self.frame_2)
        self.lbl1 = QLabel(self.centralwidget)
        self.lbl2 = QLabel(self.centralwidget)

    def open_true_sign(self):
        self.lbl1.clear()
        input_file=QtWidgets.QFileDialog.getOpenFileName(self,"","","*.png")
        pixmap = QPixmap(input_file[0]).scaled(200,200)

        lbl = self.lbl1
        lbl.setPixmap(pixmap)

        self.hbox1.addWidget(lbl)
        self.frame.setLayout(self.hbox1)

    def open_sign(self):
        self.lbl2.clear()
        input_file = QtWidgets.QFileDialog.getOpenFileName(self, "", "", "*.png")
        pixmap = QPixmap(input_file[0]).scaled(200,200)

        lbl = self.lbl2
        lbl.setPixmap(pixmap)

        self.hbox2.addWidget(lbl)
        self.frame_2.setLayout(self.hbox2)

app = QApplication(sys.argv)
w = Ui()
w.show()
sys.exit(app.exec())
