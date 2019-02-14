from PyQt4 import QtGui, QtCore

class MyWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)

        ...
        self.txt_list = QtGui.QTextEdit(self)
        self.txt_list.resize(580,400)
        self.txt_list.move(50, 50)
        self.txt_list.setReadOnly(1)
        self.txt_list.setFont(font_consolas)
        ...
        self.monitor = Monitor()
        self.monitor.updateText.connect(self._handleTextUpdate)
        self.monitor.update_list()

    def _handleTextUpdate(self, txt):
        self.txt_list.clear()
        self.txt_list.setText(txt)


class Monitor(QtCore.QObject):

    updateText = QtCore.pyqtSignal(str)

    def update_list(self):
        t_monitor = Thread(self.monitor_vector, parent=self)
        t_monitor.daemon = True
        t_monitor.setName('monitor')
        t_monitor.start()

    def monitor_vector(self):
        ...
        self.updateText.emit('updated list')


class Thread(QtCore.QThread):

    def __init__(self, fn, args, kwargs, parent=None):
        super(Thread, self).__init__(parent)
        self._fn = fn 
        self._args = args 
        self._kwargs = kwargs 

    def run(self):
        self._fn(*self._args, **self._kwargs)