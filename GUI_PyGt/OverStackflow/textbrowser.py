import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *


class gameWindow(QtGui.QMainWindow):
     def __init__(self, parent=None):
         super(gameWindow, self).__init__(parent)
         QtGui.QMainWindow.__init__(self)
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)

         buttonHarvest = QPushButton("Harvest") #Create the harvest button -
                                                # but QT Designer made it?
         buttonMining = QPushButton("Mining") # Create the mining button -
                                              # but QT Designer made it?



         self.label = QLabel("Example") # Set the empty label that's not
                                        # showing

         self.connect(buttonHarvest, SIGNAL("clicked()"), self.skillHarvest)

         self.connect(buttonMining, SIGNAL("clicked()"), self.skillMining)



     def on_buttonHarvest_clicked(self):
         harvest = "You find some roots."
         self.label.setText(harvest)

     def on_buttonMining_clicked(self):
         mining = "You found some gold."
         self.label.setText(mining)