# .*. coding: utf-8
from PyQt4.QtGui import QPlainTextEdit

class Editor(QPlainTextEdit):

    def __init__(self):
        super(Editor, self).__init__()
        self.minimapa = MiniMapa(self)
        self.es_nuevo = True
        self.nombre = "Nuevo_archivo"
        self.modificado = False

        self.textChanged.connect(self._actualizar_minimapa)

    def _actualizar_minimapa(self):
        #envia el texto al minimapa
        texto = self.toPlainText()
        self.minimapa.setPlainText(texto)


    def resizeEvent(self, event):
        super(Editor, self).resizeEvent(event)
        self.minimapa.actualizar_area()

class MiniMapa(QPlainTextEdit):

    def __init__(self, editor):
        super(MiniMapa, self).__init__(editor)
        self.editor = editor
        self.setReadOnly(True)
        self.setStyleSheet("background: transparent; border-radius: 0px;")
    def actualizar_area(self):
        x = self.editor.width() - self.width()
        altura = self.editor.height()
        self.setFixedHeight(altura)
        self.move(x, 0)

        #actualizar tamaño de la fuente
        font = self.document().defaultFont()
        font.setPointSize(3)
        self.setFont(font)