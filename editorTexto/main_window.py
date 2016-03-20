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
        self.nuevo.setShortcut("Ctrl+N")
        self.abrir = QAction("Abrir", self)
        self.abrir.setShortcut("Ctrl+O")
        self.guardar = QAction("Guardar", self)
        self.guardar.setShortcut("Ctrl+S")
        self.guardar_como = QAction("Guardar Como", self)
        self.salir = QAction("Salir", self)
        self.deshacer = QAction("Deshacer", self)
        self.deshacer.setShortcut("Ctrl+Z")
        self.rehacer = QAction("Rehacer", self)
        self.rehacer.setShortcut("Ctrl+Y")
        self.cortar = QAction("Cortar", self)
        self.cortar.setShortcut("Ctrl+X")
        self.copiar = QAction("Copiar", self)
        self.copiar.setShortcut("Ctrl+C")
        self.pegar = QAction("Pegar", self)
        self.pegar.setShortcut("Ctrl+V")
        self.acerca_de = QAction("Acerca de", self)


    def __crear_menu(self, menu_bar):
        menu_archivo = menu_bar.addMenu("&Archivo")
        menu_archivo.addAction(self.nuevo)
        menu_archivo.addAction(self.abrir)
        menu_archivo.addAction(self.guardar)
        menu_archivo.addAction(self.guardar_como)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.salir)
        menu_editar = menu_bar.addMenu("&Editar")
        menu_editar.addAction(self.deshacer)
        menu_editar.addAction(self.rehacer)
        menu_editar.addSeparator()
        menu_editar.addAction(self.cortar)
        menu_editar.addAction(self.copiar)
        menu_editar.addAction(self.pegar)
        menu_ayuda = menu_bar.addMenu("A&yuda")
        menu_ayuda.addAction(self.acerca_de)