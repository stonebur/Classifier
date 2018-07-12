import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


class Window(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'Tinder Sucks'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.YesOrNo = None
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        pic = QLabel(self)
        pic.setPixmap(QPixmap("bird.jpg"))
        pic.show()
        
        buttonYes = QPushButton('Theyre Spicy', self)
       	buttonYes.move(100,400)
        buttonYes.resize(120, 50)
        buttonYes.clicked.connect(self.on_clickYes)

        buttonYes = QPushButton('Absoluely Not', self)
       	buttonYes.move(420,400)
        buttonYes.resize(120, 50)
        buttonYes.clicked.connect(self.on_clickNo)

        self.show()
 
    @pyqtSlot()
    def on_clickYes(self):
        self.YesOrNo = True
    def on_clickNo(self):
    	self.YesOrNo = False

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())