# .*. coding: utf-8
#Contador de lineas
from PyQt4.QtGui import *
import sys

LINEA = 0
#abrir archivo
#with open('video10.py','r') as f:
    #for l in f:
        #LINEA += 1
    #print LINEA

class CuentaL(QDialog):

    def __init__(self):
        super(CuentaL, self).__init__()
        self.lineas = 0

        self.setWindowTitle("Cuenta Lineas")

        vbox = QVBoxLayout(self)

        self.boton = QPushButton("Abrir archivo")
        self.label = QLabel("")
        self.label.hide()

        vbox.addWidget(self.boton)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.boton.clicked.connect(self.dialogo)

    def dialogo(self):
        #estas dos lineas que vienen son opcionales
        direc = "/home/diego"
        extension = "(*.jpg)"

        nombre = QFileDialog.getOpenFileName(self,"Abrir archivo", direc, extension)
        if nombre:
            self.abrir_archivo(nombre)
    def abrir_archivo(self, nombre):
        with open(nombre, 'r') as f:
            for l in f:
                self.lineas += 1
            self.mostrar(self.lineas)

    def mostrar(self, lineas):
        self.label.setText("El archivo tiene <b>%s</b> lineas" % str(lineas))
        self.label.show()



app = QApplication(sys.argv)
w = CuentaL()
w.show()

sys.exit(app.exec_())