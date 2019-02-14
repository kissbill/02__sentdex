import sys
from PyQt4 import QtGui, QtCore


string = []
regex_words = ''
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


        btn = QtGui.QPushButton("tomb", self)
        btn.clicked.connect(self.make_search_string)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,70)

        checkBox = QtGui.QCheckBox('A',self)
        checkBox.move(50,50)
        checkBox.stateChanged.connect(self.tick_1)

        checkBox = QtGui.QCheckBox('B',self)
        checkBox.move(0,25)
        checkBox.stateChanged.connect(self.tick_2)


        self.show()
        

    def tick_1(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ModeManager' +')')            
         else:
            string.pop(0)
            

    def tick_2(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ToDo' +')')            
         else:
            string.pop(0)
            

    def make_search_string(self):
        for words in string:
            print(words)
        regex_words = "".join(str(x) for x in string)
        print ( regex_words )

        

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()

    
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())



run()