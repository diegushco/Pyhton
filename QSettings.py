# .*. coding: utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class Widget(QDialog):

    def __init__(self):
        super(Widget, self).__init__()
        self.setWindowTitle("QSettings")

        vbox = QVBoxLayout(self)

        hbox = QHBoxLayout()
        botonGuardar = QPushButton("Guardar")
        botonCargar = QPushButton("Cargar")
        hbox.addWidget(botonGuardar)
        hbox.addWidget(botonCargar)

        hhbox = QHBoxLayout()
        self.check = QCheckBox("check")
        self.spin = QSpinBox()
        hhbox.addWidget(self.check)
        hhbox.addWidget(self.spin)

        vbox.addLayout(hhbox)
        vbox.addLayout(hbox)

        self.cargar()

        self.connect(botonGuardar, SIGNAL("clicked()"), self.guardar)
        self.connect(botonCargar, SIGNAL("clicked()"), self.cargar)

    def guardar(self):
        #settings = QSettings("Organizacion", "ejemplo")
        settings = QSettings("config.ini", QSettings.IniFormat)
        settings.beginGroup("Ventana")
        settings.setValue("dimension", self.geometry())

        settings.setValue("spin", self.spin.value())
        print(self.geometry())
        settings.endGroup
    def cargar(self):
        #settings = QSettings("Organizacion", "ejemplo")
        settings = QSettings("config.ini", QSettings.IniFormat)
        settings.beginGroup("Ventana")
        dimensiones = settings.value("dimension").toRect()
        self.setGeometry(dimensiones)

        spin = settings.value("spin").toInt()[0]
        print spin
        self.spin.setValue(spin)

        settings.endGroup


app = QApplication(sys.argv)
w = Widget()
w.show()

sys.exit(app.exec_())