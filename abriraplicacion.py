# .*. coding: utf-8

from PyQt4.QtGui import *
from subprocess import Popen
import sys


class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Video de terminales")

        #Widget
        vbox = QVBoxLayout(self)


        self.combo = QComboBox()
        boton = QPushButton("Run!")
        terminales = ['xterm','gnome-terminal', 'terminator', 'lxterminal', 'x-terminal-emulator']
        for terminal in terminales:
            self.combo.addItem(terminal)


        vbox.addWidget(self.combo)
        vbox.addWidget(boton)


        #conexion
        boton.clicked.connect(self.run)

    def run(self):
        comando = str(self.combo.currentText())
        try:
            Popen(comando)
        except:
            QMessageBox.information(self, "Error!",
                "{0} no esta instalado".format(comando))



app = QApplication(sys.argv)
w = Widget()
w.show()

sys.exit(app.exec_())