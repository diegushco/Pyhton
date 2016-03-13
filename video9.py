# .*. coding: utf-8
"""
tutorial
Señal -> emitida por un widget
un widget determinado emite una señal determinada
por ejemplo boton->click

Un slot es una funcion o metodo en python
ejemplo (saludar)

el slot se conecta a la señal

widget -> señal -> conectada -> slot
boton -> click -> conectado -> saludar
"""
from PyQt4.QtGui import *  # contiene los Widgets
from PyQt4 import QtCore
import sys


class Ventana(QWidget):

    def __init__(self):
        super(Ventana, self).__init__()

        self.setWindowTitle("Signals and Slots")
        self.resize(200, 200)
        self.move(400, 200)

        #boton -> click -> conectado -> saludar
        boton  = QPushButton("Saludar", self)
        salir = QPushButton("Salir", self)
        salir.move(100, 100)
        #Conexion
        #Forma 1: estilo C++
        #self.connect(boton, QtCore.SIGNAL("clicked()"), self.saludar)

        #Forma2: Pythonica //no hace falta importar qtcore
        boton.clicked.connect(self.saludar)
        salir.clicked.connect(self.close)
    def saludar(self):
            print "Hola mundo!"


app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

#MainLoop que manti0ene viva la aplicaicon
sys.exit(app.exec_())