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

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

#MainLoop que mantiene viva la aplicaicon
sys.exit(app.exec_())