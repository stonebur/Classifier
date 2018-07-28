'''
First Window is called and is for choosing sexual preference
in the button listeners for each of the preferences, a new picture viewing window is made
'''
import sys
import os
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import shutil
import subprocess
#this is for sexual preference selection
class FirstWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Sexual Preference'
		self.left = 10
		self.top = 10
		self.width = 300
		self.height = 100
		self.YesOrNo = None
		self.initUI()

	def centerOnScreen (self):
		resolution = QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.centerOnScreen()
		ButtonFemale=QPushButton("Female", self)
		ButtonFemale.move(50,50)						#reposition the buttons here
		ButtonFemale.clicked.connect(self.ClickFemale)
		
		ButtonMale=QPushButton("Male", self)
		ButtonMale.move(210,50)
		ButtonMale.clicked.connect(self.ClickMale)
		self.show()
		#action events for each button
	def ClickFemale(self):
		global Preference
		Preference="Female"
		self.ex=Window()
		self.hide()
		self.ex.show()
		
		
	def ClickMale(self):
		global Preference
		Preference="Male"
		self.ex = Window()
		self.hide()
		self.ex.show()
		
		#Picture viewing window
class Window(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Fuego'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.YesOrNo = None
		self.noCounter = 195
		self.yesCounter = 195
		self.initUI()
		
	def centerOnScreen (self):
		resolution = QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.centerOnScreen()
		self.pic = QLabel(self)
		self.pic.setPixmap(QPixmap("what.jpg"))		#loads this image just to set the size of the window
		self.pic.show()								#this image isnt even viewed since it is displayed so briefly
													#something ill fix sometime
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
		#the main body of the picture selection
	def function(self):
		print(os.getcwd())
		os.chdir("../tf_files/dataset")		#..//tf_files/catvdog/ is what it should be
		both=False					#will add in support for both later

		if Preference=="Female":
			os.chdir("Female")
		elif Preference=="Male":                        
			os.chdir("Male")
		else:						#need to implement fully
			#both=True
			pass
		self.pictures= {}                #new dictionary created
		counter=0
								#assign each file in dicectory to a dictionary
		for x in os.listdir("."):
			self.pictures[counter]=x
			counter+=1
		
		counter=0
		self.length=(len(os.listdir("."))-1)       #get number of files in directory
													#this is for displaying the first image
													
		index=random.choice(list(self.pictures))	#index stores a random key from the pictures dictionary
		
		self.temp=self.pictures.pop(index) #delete the image from the dictionary so it doesn't come up again
											#temp is created which stores filenames
									
		self.picchange(self.temp)			#changes the image
		self.length=len(self.pictures)		#recalculates how many images are now there -1
		#a function made for displaying images
	def picchange(self,string):
		pixmap=QPixmap(string)												#make a picture map from the filename
		pixmap=pixmap.scaled(self.width,self.height, Qt.KeepAspectRatio)	#scales and resizes the image
		self.pic.setPixmap(pixmap)											#assign picture mape to qlabel created in init
		self.pic.show()														#display image
		self.show()															#update window

	@pyqtSlot()
	def on_clickYes(self):
		self.yesCounter += 1
		shutil.move(self.temp,"../../catvdog/Like")				#add to liked
		index=random.choice(list(self.pictures))					#get next image
		if len(self.pictures)==0:									#if there are no pictures then quit
			QCoreApplication.quit()
		self.temp=(self.pictures[index])							#get next image
		self.picchange(self.temp)									#change to the image
		self.pictures.pop(index)									#delete the image filename from dictionary
		self.trainAndSelect()
		
		
	def on_clickNo(self):
		self.noCounter += 1
		shutil.move(self.temp,"../../catvdog/Dislike")
		index=random.choice(list(self.pictures))
		if len(self.pictures)==0:
			QCoreApplication.quit()
		self.temp=(self.pictures[index])
		self.picchange(self.temp)
		self.pictures.pop(index)
		self.trainAndSelect()

	def trainAndSelect(self):
		if (self.yesCounter >= 200 and self.noCounter >= 200):
				self.pics = {}
				counter = 0
				os.chdir("../../../")
				os.system("./train.sh")
				for x in os.listdir("./tf_files/dataset/" + Preference):
					os.system("python -m scripts.label_image --graph=tf_files/retrained_graph.pb	\
						--image=tf_files/dataset/" + Preference + "/" + x)
				scores = {}
				with open("likeScores") as f:
					for line in f:
						(val, key) = line.split()
						scores[key] = val
				perfMatch = max(scores, key=scores.get)
				open('likeScores', 'w').close()
				self.picchange(perfMatch)
				self.yesCounter = 195
				self.noCounter = 195
				os.chdir("tf_files/dataset/" + Preference)
				


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex2=FirstWindow()
	sys.exit(app.exec_())