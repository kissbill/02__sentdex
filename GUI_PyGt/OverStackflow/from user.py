import sys ,re
from PyQt4 import QtGui ,QtCore

string = []
regex_words = ''
finding = []

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.setGeometry(0, 400, 1200, 300)
        self.setWindowTitle("Hash Tagging")

        self.button = QtGui.QPushButton('')
        self.textedit = QtGui.QTextEdit()
        self.textedit.setReadOnly(True)
        layout.addWidget(self.textedit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.searching)

        btn = QtGui.QPushButton("Search" ,self)
        btn.clicked.connect(self.searching)
        btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(700,200)

        btn = QtGui.QPushButton("List" ,self)
        btn.clicked.connect(self.print_out)
        btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(780,200)

        # Projects 2 db
        project_y = 10
        checkBox = QtGui.QCheckBox('Base +',self)
        checkBox.move(700,project_y)
        checkBox.stateChanged.connect(self.tick_1)

        checkBox = QtGui.QCheckBox('Base -',self)
        checkBox.move(760,project_y)
        checkBox.stateChanged.connect(self.tick_2)
        # Tools
        tool_y = 35
        checkBox = QtGui.QCheckBox('CANape',self)
        checkBox.move(700,tool_y)
        checkBox.stateChanged.connect(self.tick_3)

        checkBox = QtGui.QCheckBox('CANoe',self)
        checkBox.move(765,tool_y)
        checkBox.stateChanged.connect(self.tick_4)

        checkBox = QtGui.QCheckBox('ECUtest',self)
        checkBox.move(820,tool_y)
        checkBox.stateChanged.connect(self.tick_5)

        checkBox = QtGui.QCheckBox('Trace',self)
        checkBox.move(880,tool_y)
        checkBox.stateChanged.connect(self.tick_6)

        # Infrastructs
        infrastuct_y = 60

        checkBox = QtGui.QCheckBox('Git',self)
        checkBox.move(700,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_7)

        checkBox = QtGui.QCheckBox('Polarion',self)
        checkBox.move(745,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_8)

        checkBox = QtGui.QCheckBox('Jenkins',self)
        checkBox.move(820,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_9)

        checkBox = QtGui.QCheckBox('MiniHIL',self)
        checkBox.move(880,infrastuct_y)
        checkBox.stateChanged.connect(self.tick_10)
        # Topics
        topics_y = 80
        checkBox = QtGui.QCheckBox('ModeManager',self)
        checkBox.move(700,topics_y)
        checkBox.stateChanged.connect(self.tick_11)

        checkBox = QtGui.QCheckBox('ActiveDischarge',self)
        checkBox.move(790,topics_y)
        checkBox.stateChanged.connect(self.tick_12)

        # Works
        work_y = 105
        checkBox = QtGui.QCheckBox('ToDo',self)
        checkBox.move(700,work_y)
        checkBox.stateChanged.connect(self.tick_13)

        checkBox = QtGui.QCheckBox('Automat',self)
        checkBox.move(750,work_y)
        checkBox.stateChanged.connect(self.tick_14)

        checkBox = QtGui.QCheckBox('Defect',self)
        checkBox.move(820,work_y)
        checkBox.stateChanged.connect(self.tick_15)

        checkBox = QtGui.QCheckBox('Meeting',self)
        checkBox.move(890,work_y)
        checkBox.stateChanged.connect(self.tick_16)

        checkBox = QtGui.QCheckBox('Regession',self)
        checkBox.move(950,work_y)
        checkBox.stateChanged.connect(self.tick_17)

        checkBox = QtGui.QCheckBox('Review',self)
        checkBox.move(1020,work_y)
        checkBox.stateChanged.connect(self.tick_18)


        #Miscs
        misc_y = 135
        checkBox = QtGui.QCheckBox('AddWorkFlow',self)
        checkBox.move(700,misc_y)
        checkBox.stateChanged.connect(self.tick_19)

        checkBox = QtGui.QCheckBox('KnowHow',self)
        checkBox.move(790,misc_y)
        checkBox.stateChanged.connect(self.tick_20)

        checkBox = QtGui.QCheckBox('Directiva',self)
        checkBox.move(860,misc_y)
        checkBox.stateChanged.connect(self.tick_21)

        checkBox = QtGui.QCheckBox('Xlsx',self)
        checkBox.move(930,misc_y)
        checkBox.stateChanged.connect(self.tick_22)

        checkBox = QtGui.QCheckBox('Letter',self)
        checkBox.move(975,misc_y)
        checkBox.stateChanged.connect(self.tick_23)

        checkBox = QtGui.QCheckBox('Link',self)
        checkBox.move(1030,misc_y)
        checkBox.stateChanged.connect(self.tick_24)



        

    def print_out(self):
        finding_ = "".join(str(x) for x in finding)
        self.textedit.append(finding_)
        self.textedit.append('')


    def tick_1(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'BasePlus' +')')            
         else:
            string.remove('(?=.*#'+ 'BasePlus' +')')            
    def tick_2(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'BaseMinus' +')')            
        else:
            string.remove('(?=.*#'+ 'BaseMinus' +')') 
    def tick_3(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'CANape' +')')            
         else:
            string.remove('(?=.*#'+ 'CANape' +')')            
    def tick_4(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'CANoe' +')')            
        else:
            string.remove('(?=.*#'+ 'CANoe' +')')
    def tick_5(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ECUtest' +')')            
         else:
            string.remove('(?=.*#'+ 'ECUtest' +')')            
    def tick_6(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Trace' +')')            
        else:
            string.remove('(?=.*#'+ 'Trace' +')')
    def tick_7(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Polarion' +')')            
         else:
            string.remove('(?=.*#'+ 'Polarion' +')')            
    def tick_8(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Jenkins' +')')            
        else:
            string.remove('(?=.*#'+ 'Jenkins' +')')
    def tick_9(self, state):        
         if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'MiniHIL' +')')            
         else:
            string.remove('(?=.*#'+ 'MiniHIL' +')')            
    def tick_10(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'MiniHIL' +')')            
        else:
            string.remove('(?=.*#'+ 'MiniHIL' +')')
    def tick_11(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ModeManager' +')')            
        else:
            string.remove('(?=.*#'+ 'ModeManager' +')')
    def tick_12(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ActiveDischarge' +')')            
        else:
            string.remove('(?=.*#'+ 'ActiveDischarge' +')')
    def tick_13(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'ToDo' +')')            
        else:
            string.remove('(?=.*#'+ 'ToDo' +')')
    def tick_14(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Automat' +')')            
        else:
            string.remove('(?=.*#'+ 'Automat' +')')
    def tick_15(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Defect' +')')            
        else:
            string.remove('(?=.*#'+ 'Defect' +')')
    def tick_16(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Meeting' +')')            
        else:
            string.remove('(?=.*#'+ 'Meeting' +')')
    def tick_17(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Regession' +')')            
        else:
            string.remove('(?=.*#'+ 'Regession' +')')
    def tick_18(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Review' +')')            
        else:
            string.remove('(?=.*#'+ 'Review' +')')    
    def tick_19(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'AddWorkFlow' +')')            
        else:
            string.remove('(?=.*#'+ 'AddWorkFlow' +')')
    def tick_20(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'KnowHow' +')')            
        else:
            string.remove('(?=.*#'+ 'KnowHow' +')')
    def tick_21(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Directiva' +')')            
        else:
            string.remove('(?=.*#'+ 'Directiva' +')')
    def tick_22(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Xlsx' +')')            
        else:
            string.remove('(?=.*#'+ 'Xlsx' +')')
    def tick_23(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Letter' +')')            
        else:
            string.remove('(?=.*#'+ 'Letter' +')')
    def tick_24(self, state):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#'+ 'Link' +')')            
        else:
            string.remove('(?=.*#'+ 'Link' +')')





    def searching(self):
        # Init
        text = []
        sorban_end = []
        kulcs_szo_sora = []
        regex_words = "".join(str(x) for x in string)
        kulcsSzo = r"(?=.*)" + regex_words
       
        #print(kulcsSzo)
       
        ending = '\\+'
        pattern_keyword = re.compile( kulcsSzo )
        pattern_end = re.compile( ending )

        # Loop through text
        for i, line in enumerate(open('log_VW_FEB.txt')):
            text.append(line)
            #Kulcs szo
            for match in re.finditer(pattern_keyword, line):
                kulcs_szo_sora.append( i + 1 ) #talalt sor lementese
                break
            # Kereszt lezarasok keresese
            for match in re.finditer(pattern_end, line):
                sorban_end.append( i + 1 ) #talalt kereszt sor lementese

        # Lezaro kereszt elemek tombjenek hossza
        #hossz = len(sorban_end)
        for hits in kulcs_szo_sora:
            print('Eredeti doksiban ezen sor : %s ' % hits)
            print()

            for lezaro in sorban_end[0:len(sorban_end)]:
                if hits < lezaro:
                    #print(hits)
                    #print(lezaro)
                    break

            for megVagy in text[hits-1:lezaro-1]:
                finding.append( megVagy )
            
        print('----------------------------------oo------------------------------------')
        

    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


#Hetfo Kedd Szerda Csutortok Pentek  
#BaseMinus BasePlus
#CANape CANoe ECUtest Trace Git Polarion Jenkins MiniHIL
#ToDo Defect Meeting
#Review  Regession
#Offset  ModeManager ActiveDischarge Automat
#AddWorkFlow KnowHow Directiva
#   Xlsx   
#Letter  Link    