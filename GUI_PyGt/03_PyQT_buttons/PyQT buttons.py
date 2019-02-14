import sys
from PyQt4 import QtGui, QtCore #Event is lehessen a gombra

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__() ##superrel atadjuk a parent objektet -->QMainWindow -ot
        self.setGeometry(50, 50, 500, 300) #itt lehet hivatkozni a window-ra mint sajat maga -->self-->window
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pyLogo.png'))
        self.home()
        
    def home(self):
    	btn = QtGui.QPushButton("Quit" ,self) #ez legyen a neve aztan kuldje el a Window-ot
    	btn.clicked.connect(QtCore.QCoreApplication.instance().quit) #Connect megmondja, mit csinaljon a gomb, ha raboknek
    	btn.resize(100,100)
    	btn.move(100,100)    	
    	self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
