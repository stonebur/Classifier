import sys
import os
import random
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


class Window(QWidget):


	def __init__(self):
		super().__init__()
		self.title = 'Image Classifier'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.YesOrNo = None						#contains the answer from the button
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		buttonYes = QPushButton("They're Spicy", self)			#you like this person
		buttonYes.move(100,400)
		buttonYes.resize(120, 50)
		buttonYes.clicked.connect(self.on_clickYes)

		buttonYes = QPushButton('Absoluely Not', self)			#you don't like this person
		buttonYes.move(420,400)
		buttonYes.resize(120, 50)
		buttonYes.clicked.connect(self.on_clickNo)
		self.pic=QLabel(self)
		
		self.show()
		self.function()
    
	def PictureChanger(self, picture):							#function used to change the picture
		pixmap=QtGui.QPixmap(picture)
		pixmap=pixmap.scaled(500,500, Qt.KeepAspectRatio)		#these numbers set the dimensions of the picture
		self.pic.setPixmap(pixmap)
		self.show()
		self.pic.show()
 
	@pyqtSlot()
	def on_clickYes(self):									#function that executes when you like te person
		self.YesOrNo = 1
	def on_clickNo(self):									#when the person is not liked
		self.YesOrNo = 2
		
		
		#This function is used as a main
		#but isn't actually in main due to thread conflicts
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
		pictures= {}                #new dictionary created
		counter=0
								#assign each file in dicectory to a dictionary
		for x in os.listdir("."):
			pictures[counter]=x
			counter+=1
		
		counter=0
		length=(len(os.listdir("."))-1)       #get number of files in directory
	
		while counter<100:                  #until 100 matches is reached
			index=random.randint(0,length)	#get a random index (aka choosing a random file from the male or female folder
			temp=(pictures[index])   #match at random
			self.PictureChanger(temp)
			app.exec()
			counter=+1
			while True:

				if self.YesOrNo==1:            #if you like the picture
					shutil.move(temp,"../Liked/"+temp)		
					self.YesOrNo==None		#return to none for next loop
					pictures.pop(index)		#delete the picture from the dictionary
					break
				elif self.YesOrNo==2:       #if you do not like the picture
					shutil.move(temp, "../Disliked/"+temp)
					self.YesOrNo==None		#return to none for next loop
					pictures.pop(index)		#delete the picture from the dictionary
					break
					
			length=length-1					#decrease length by one when a picture is selected
			
			if length == 0:					# if all pictures have been looked at, end
				break
				
				
		self.close()
 
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Window()	
	app.exec_()
