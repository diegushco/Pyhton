# .*. coding: utf-8

from PyQt4.QtGui import *
import sys


class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Video 12")

        #Widget
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()

        self.combo = QComboBox()
        lista = ['item 1','item 2', 'item 3']
        for item in lista:
            self.combo.addItem(item)

        self.line = QLineEdit()
        self.labelCombo = QLabel("")
        self.labeLine = QLabel("")

        hbox.addWidget(self.labelCombo)
        hbox.addWidget(self.labeLine)

        vbox.addWidget(self.combo)
        vbox.addWidget(self.line)
        vbox.addLayout(hbox)

        #conexion
        self.combo.currentIndexChanged.connect(self.slot_1)
        self.line.textChanged.connect(self.slot_2)

    def slot_1(self):
        self.labelCombo.setText(self.combo.currentText())
    def slot_2(self):
        self.labeLine.setText(self.line.text())



app = QApplication(sys.argv)
w = Widget()
w.show()

sys.exit(app.exec_())