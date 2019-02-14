import sys
from PyQt4 import QtGui, QtCore


string = []
class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(700, 700, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)

        checkBox = QtGui.QCheckBox('A',self)
        checkBox.move(50,50)
        
        #checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        checkBox = QtGui.QCheckBox('B',self)
        checkBox.move(0,25)
        
        #checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)


        self.show()
        

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()

    def enlarge_window(self, state):        
         if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
            string.append('h')
            print(string)
         else:
            self.setGeometry(50, 50, 500, 300)
            string.pop(0)
            print(string)
    

    
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    print(string)
    sys.exit(app.exec_())



run()