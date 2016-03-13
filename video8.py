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
        self.resize(300, 300)

        # Mover ventana
        self.move(100, 100)

        #cambiar icono
        self.setWindowIcon(QIcon("goku.jpg"))

        btn_1 = QPushButton("1",self)
        btn_2 = QPushButton("2",self)
        btn_3 = QPushButton("3",self)
        btn_4 = QPushButton("4",self)

        grilla = QGridLayout(self)
        grilla.addWidget(btn_1, 0, 0)
        grilla.addWidget(btn_2, 0, 1)
        grilla.addWidget(btn_3, 1, 0)
        grilla.addWidget(btn_4, 1, 1)


app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

#MainLoop que mantiene viva la aplicaicon
sys.exit(app.exec_())