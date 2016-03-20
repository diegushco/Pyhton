# .*. coding: utf-8

from PyQt4.QtGui import *
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MainWindow")
        self.setMinimumSize(400, 300)

        #CentralWidget
        widget = QTextEdit()
        self.setCentralWidget(widget)

        #QAction
        self.accionSalir = QAction("Salir", self)
        self.accionSalir.setShortcut("Ctrl+Q")
        self.accionSalir.setStatusTip(self.trUtf8("Salir de la aplicación"))

        #Barra de estado
        self.setStatusBar(QStatusBar())

        #Menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Archivo")
        menu_archivo.addAction(self.accionSalir)


app = QApplication(sys.argv)
w = MainWindow()
w.show()

sys.exit(app.exec_())