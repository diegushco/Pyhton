# .*. coding: utf-8

from PyQt4.QtGui import *
import sys


class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Creando un menu")

        vbox = QVBoxLayout(self)
        menu = QMenuBar()

        self.archivo = menu.addMenu("&Archivo")
        self.editar = menu.addMenu("&Editar")

        vbox.addWidget(menu)


app = QApplication(sys.argv)
w = Widget()
w.show()

sys.exit(app.exec_())