import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__() ##superrel atadjuk a parent objektet -->QMainWindow -ot
        self.setGeometry(50, 50, 500, 300) #itt lehet hivatkozni a window-ra mint sajat maga -->self-->window
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pyLogo.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())