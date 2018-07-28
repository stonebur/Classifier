#!/usr/bin/python3
import os
import random
import shutil

os.chdir("Pictures")

Preference="Whatever the user chooses as a sexual preference"
both=False

if Preference=="Female":
    os.chdir("..//tf_files/catvdog/Female")
elif:                        #Preference=="Male":
    os.chdir("..//tf_files/catvdog/Male")
else:
    both=True

pictures= {}                #new dictionary created
counter=0
                            #assign each file in dicectory to a dictionary
for x in os.listdir("."):
    pictures[counter]=x
    counter+=1

counter=0
length=len(os.listdir("."))-1       #get number of files in directory
while(counter<100)                  #until 100 matches is reached
    temp=(pictures[random.randint(0,length)])   #match at random
    counter=+1

    flag=0                      #user response will be stored here

    if flag=="like":            #if you like the picture
        shutil.move(temp,"Where it needs to be places"+temp)        
    elif flag=="dislike":       #if you do not like the picture
        shutil.move(temp, "Where it needs to be placed"+temp)
