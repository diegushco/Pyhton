"""
tutorial
"""
from PyQt4.QtGui import *  # contiene los Widgets
import sys

class Ventana(QWidget):

    def __init__(self):
        super(Ventana, self).__init__()
        #cambia el titulo de la ventana
        self.setWindowTitle("probando python qt")

        # Redimensionar la ventana
        self.resize(800, 600)

        # Mover ventana
        self.move(100, 100)

        #cambiar icono
        self.setWindowIcon(QIcon("goku.jpg"))

        #Botones
        boton = QPushButton("Boton 1", self)
        boton.setGeometry(0, 0, 90, 40)
        boton2 = QPushButton("Boton 2", self)
        boton2.move(100, 0)

        #Etiquetas o labels
        label = QLabel("<h2>Esto es una etiqueta</h2>", self)
        label.move(300, 0)

        #Layouts
        layout_horizontal = QHBoxLayout(self)
        layout_horizontal.addWidget(boton)
        layout_horizontal.addWidget(boton2)
        layout_horizontal.addWidget(label)
        self.setLayout(layout_horizontal)

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

#MainLoop que mantiene viva la aplicaicon
sys.exit(app.exec_())