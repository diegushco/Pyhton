# .*. coding: utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
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
        self.accionSalir.setIcon(QIcon("salir.png"))
        self.accionSalir.setShortcut("Ctrl+Q")
        self.accionSalir.setStatusTip(self.trUtf8("Salir de la aplicación"))


        self.accionNuevo = QAction("Nuevo", self)
        self.accionNuevo.setIcon(QIcon("nuevo.png"))
        self.accionNuevo.setShortcut("Ctrl+N")
        self.accionNuevo.setStatusTip(self.trUtf8("Nuevo"))

        #Barra de herramientas o toolbar
        self.toolbar = QToolBar(self)
        self.toolbar.addAction(self.accionNuevo)
        self.toolbar.addAction(self.accionSalir)
        self.addToolBar(Qt.RightToolBarArea, self.toolbar)

        #Barra de estado
        self.setStatusBar(QStatusBar())

        #Menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Archivo")
        menu_archivo.addAction(self.accionNuevo)
        menu_archivo.addAction(self.accionSalir)


app = QApplication(sys.argv)
w = MainWindow()
w.show()

sys.exit(app.exec_())