
import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

class QButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.button = QtGui.QPushButton('Button', self)
        self.name='me'
        self.button.clicked.connect(self.calluser)
    def calluser(self):
        print(self.name)

def demo_QButton():
    app = QtGui.QApplication(sys.argv)
    tb = QButton()
    tb.show()
    app.exec_()

if __name__=='__main__':
    demo_QButton()