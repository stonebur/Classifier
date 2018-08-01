Image Dragons group project for CIS4930 by: Harrison Scott, Nate Stoneburner, Christian Barth and Chad Willis

Goal: The goal of this project simply started with wanting to build an application that could use image recognition to classify images using
unsupervised learning. This portion was tricky however with modern tools and tutorials based off of tensorflow, this was very doable.
After doing some research and leg work we determined that an image classifier would be too simple and wanted to add an application to it.
For this application we decided it would be very cool to try to get this image classifier to classify people as attractive or unattractive
solely based off of facial features due to this being a very common trend in modern millenial superficial dating apps. This changed the
scope of artificial intelligence being used from unsupervised learning to supervised learning where a person labels what is attractive and
what is not as the application uses a neural network to find patterns and can later determine what pictures that said person would find attractive.

Parts of this project: To start, Harrison did some research and learned how to make tensorflow integrate into the most simple of image
classifiers. Though there were obstacles and all sorts of system requirements, the backend of automating this classifiers to clarify
and update the tools was done by him. After this point, a working image classifier that automated all of the parts to run a python 2 based
classifier using the 'Tensorflow for poets" tutorial could be ran by simply running shell script which called multiple python scripts.
After this point, the group started to determine what this application that works with amazing accuracy could be used for and we all
determined that a simplified dating app would be interesting as it could be the future. From this point, we determined it would be easiest to
start with a very simple GUI and we just happened to be going over PyQt in class at this point. The front end for this portion was handled by
Christian and Chad who worked together to build a simple but powerful gui. Simplicity was the goal here however it still started to get 
complex when integration needed to happen, but they both did a great job with getting the front end functional. After this, the big challenge
came which was handled by mainly Nate but also Harrison and Christian who all determined how to bridge the front and back end. The way this
application works is by selecting files in /tf_files/dataset into 2 files which were male and female folders. It then needs to move these
pictures to /tf_files/bottlenecks/like or dislike based on what the user thinks. The user chooses their preference of male or female as
soon as they start the application. After sifting through photos and the photos getting sorted into like or dislike, the script that
classifies images. It then writes to a text file the outcome which is a number between 0-1 based on which category each picture in the 
dataset would fall into. A pitfall is that this can take a lot of processing power and be rather slow but on a small scale this works.
Nate was the main person behind this portion assembling the code to move but also delete pictures from the dataset and then call the scripts
which Harrison wrote behind the scenes of the GUI. Harrison was responsible for the file structure and making the backend compatible with
the given directories and helped plan with Nate. Christian was a great help with bridging the front and middle end by explaining how parts
of the gui trigger all of the things that happen behind the scene. Chad worked on making the GUI more user friendly and fixing some bugs.
After this happened we needed pictures to test for our dataset. We started by using an image scraper that scrapes images off of bing written
in python by Nate and then determined an appropriate dataset size and a trigger threshold for when the classify script should be called.
After this we ran into numerous bugs which we all sat down for hours trying to figure out and debug, however once we finally figured it out
it was working very nicely.

Issues:  As a group everybody was very involved and knew what was going on. We did notice that some of use Like Harrison and Nate were more
back end inclined and Christian and Chad were more front end inclined which worked out very well. Everybody did what was asked of them and
all ideas were considered by every member of the group. We did at first want to make this a webapp however we wanted to get this basic
local version working first before we attached a database to it. Though simplicity was our goal things got complicated quickly. Additionally
writing an application that determines attractiveness is a very tough thing to do in an efficient amount of time using basic computers, which
means that a lot of the time the data does not determine attractiveness extremely well because of small datasets. However, while testing this
on a lot of pictures and manually moving files around it was apparent that this is indeed possible to predict with some accuracy.

Libraries used: Tensorflow, urllib, numpy, sys, re, tarfile, random, os, hashlib, datetime, collections, argparse, __future__,(all for backend image classifier)
for image scraper: requests, and previously mentioned libraries
for front end: pyqt5, shutil, subprocess and previously mentioned.

For use simply load pictures into the male and female dataset in tf_files/dataset and call the Start_Project shell script and then get to swiping.
As mentioned, it is not perfect however it is a lot better than random and if we could reduce processing time and have a perfect dataset,
then with a lot of swiping it would certainly possible to determine the attraction of a person.

Final comments: Though a brief summary of division of work was mentioned that is not the end all. There were so many issues throughout this
project that everybody helped solve in their own ways. Everybody was a team player and we are happy with our project as a beta version.
If we were to continue this in the future we would definitely want to fix the aforementioned errors and get it working as accurately and efficiently as possible.
