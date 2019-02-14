import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
 
# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Textbox example @pythonspot.com')
 
# Create textbox
textbox = QLineEdit(w)
textbox.move(200, 200)
textbox.resize(480,400)
 
# Set window size.
w.resize(820, 850)
 
# Create a button in the window
button = QPushButton('Click me', w)
button.move(20,80)

def createfile():
    var = """
Eredeti doksiban ezen sor : 325 

	-budapest base plus minihil infok
		-Attila
	-Git workflow --> pull rebase --> pull pedig mindenki a sajat gepen
	- X:\TestTeamTasks\VW\HIL
		-fel lett mountolva 
          """
    return var

v = createfile()


# Create the actions
@pyqtSlot()
def on_click():
	
    textbox.setText(v)
 
# connect the signals to the slots
button.clicked.connect(on_click)
 
# Show the window and run the app
w.show()
app.exec_()