"""
tutorial
"""
from PyQt4 import QtGui  # contiene los Widgets
import sys
app = QtGui.QApplication(sys.argv)
ventana = QtGui.QWidget()
ventana.show()

#MainLoop que mantiene viva la aplicaicon
sys.exit(app.exec_())