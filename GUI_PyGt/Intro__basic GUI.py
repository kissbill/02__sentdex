import sys
from PyQt4 import QtCore,QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()

window.setGeometry(1000, 1000, 500, 300) #hol, x y ,szeles, magas
window.setWindowTitle("PyQT Tuts!")

window.show()