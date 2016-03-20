# .*. coding: utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL
import sys


class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Creando un menu")

        accionSaludar = QAction("saludar", self)
        accionSaludar.setShortcut("Ctrl+N")
        accionSaludar.setIcon(QIcon("goku.jpg"))



        vbox = QVBoxLayout(self)
        menu = QMenuBar()

        self.archivo = menu.addMenu("&Archivo")
        self.archivo.addAction(accionSaludar)
        self.editar = menu.addMenu("&Editar")

        self.label = QLabel("")
        self.boton = QPushButton("Saludar")
        self.borrar_ = QPushButton("Borrar")

        vbox.addWidget(menu)
        vbox.addWidget(self.boton)
        vbox.addWidget(self.borrar_)
        vbox.addWidget(self.label)
        self.connect(self.boton, SIGNAL("clicked()"), self.saludar)

        self.connect(self.borrar_, SIGNAL("clicked()"), self.limpiar)

        self.connect(accionSaludar, SIGNAL("triggered()"), self.saludar)
    def saludar(self):
        self.label.setText("Saludando")
    def limpiar(self):
        self.label.setText("")

app = QApplication(sys.argv)
w = Widget()
w.show()

sys.exit(app.exec_())