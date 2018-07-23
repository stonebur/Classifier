import sys
import os
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import shutil


class Window(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Fuego'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.YesOrNo = None
		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.pic = QLabel(self)
		self.pic.setPixmap(QPixmap("what.jpg"))
		self.pic.show()
        
		buttonYes = QPushButton('Theyre Spicy', self)
		buttonYes.move(100,400)
		buttonYes.resize(120, 50)
		buttonYes.clicked.connect(self.on_clickYes)

		buttonYes = QPushButton('Absoluely Not', self)
		buttonYes.move(420,400)
		buttonYes.resize(120, 50)
		buttonYes.clicked.connect(self.on_clickNo)

		self.show()
		self.function()
		
	def function(self):
		os.chdir("Pictures")		#..//tf_files/catvdog/ is what it should be
		Preference="Whatever the user chooses as a sexual preference"
		both=False

		if Preference=="Female":
			os.chdir("Female")
		else:                        #Preference=="Male":
			os.chdir("Male")
		#else:						need to implement fully
			#both=True
		self.pictures= {}                #new dictionary created
		counter=0
								#assign each file in dicectory to a dictionary
		for x in os.listdir("."):
			self.pictures[counter]=x
			counter+=1
		
		counter=0
		self.length=(len(os.listdir("."))-1)       #get number of files in directory
		index=random.choice(list(self.pictures))
		self.temp=self.pictures.pop(index)
		self.picchange(self.temp)
		self.length=len(self.pictures)
			
	def picchange(self,string):
		self.pic.setPixmap(QPixmap(string))
		self.pic.show()
		self.show()

	@pyqtSlot()
	def on_clickYes(self):
		shutil.move(self.temp,"../Liked/"+self.temp)
		index=random.choice(list(self.pictures))
		if len(self.pictures)==0:
			QCoreApplication.quit()
		self.temp=(self.pictures[index])
		self.picchange(self.temp)
		self.pictures.pop(index)

		
		
	def on_clickNo(self):
		shutil.move(self.temp,"../Disliked/"+self.temp)
		index=random.randint(0,self.length)
		if len(self.pictures)==0:
			QCoreApplication.quit()
		self.temp=(self.pictures[index])
		self.picchange(temp)
		self.pictures.pop(index)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())