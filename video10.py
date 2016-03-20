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
        #crear layout vertical
        vbox = QVBoxLayout(self)
        self.setWindowTitle("Signals and Slots")
        self.move(400, 200)

        #widgets
        self.saludarB = QPushButton("Saludar")
        self.salirB = QPushButton("Salir")
        self.label = QLabel("")
        self.label.hide()

        #agregamos widget's
        vbox.addWidget(self.saludarB)
        vbox.addWidget(self.salirB)
        vbox.addWidget(self.label)

        #layout
        self.setLayout(vbox)

        #conexiones
        self.salirB.clicked.connect(self.close)
        self.saludarB.clicked.connect(self.saludar)

    def saludar(self):
            print "Hola mundo!"
            self.label.setText("<h1>Hola Mundo!</h1>")
            self.label.show()


app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

#MainLoop que manti0ene viva la aplicaicon
sys.exit(app.exec_())