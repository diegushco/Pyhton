# .*. coding: utf-8
from PyQt4.QtGui import (
    QMainWindow,
    QAction
    )

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.tr("Editor - PyQt4"))
        self.setMinimumSize(700,500)

        menu = self.menuBar()
        self.__crear_acciones()
        self.__crear_menu(menu)

    def __crear_acciones(self):
        self.nuevo = QAction("Nuevo", self)
        self.abrir = QAction("Abrir", self)

    def __crear_menu(self, menu_bar):
        menu_archivo = menu_bar.addMenu("&Archivo")
        menu_archivo.addAction(self.nuevo)
        menu_archivo.addAction(self.abrir)
        menu_editar = menu_bar.addMenu("&Editar")
        menu_ayuda = menu_bar.addMenu("&Ayuda")