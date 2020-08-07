# Soccer UT Auto Lister
As a big fan of soccer, I have played Ultimate Team for almost a decade. I 
spent hours as a trader in the in-game economy and worked hard to earn coins
to build the ultimate team. Finally, after years of listing  thousands cards, 
I had had enough. I frequently heard of automatic trading programs, and I was 
determined to make my own version using my knowledge of coding. I decided to 
use Python because it was a language that I had not used for many projects and 
I wanted to increase my ability. Also, Python has many libraries that are easy
to utilize, making it a simple task to quickly implement a working image-recognition
library in my program. 

I created a program that was tailored to list cards by using image recognition
at specific locations on my computer. I created a version to run on the UT web
app and a version to run on the Android UT app, which I ran on an Android Studio
virtual device. With my program, I listed thousands of cards and made millions
of coins in profit without grinding through the hours of work.

Created in February 2019

# Inspiration
https://steemit.com/python/@howo/image-recognition-for-automation-with-python

# Packages Necessary for Installation
pip3 install opencv-python
<br />pip3 install numpy
<br />pip3 install python3_xlib
<br />pip3 install pyautogui

# Steps to Implementation
In order for the program to work on your computer, complete the following steps:
1. Modify the locations in "locations.py" to the pixel locations on your screen.
2. In the same folder as the Python files, create a folder with images of the cards that you would like to list.
3. Modify the players in "playerprices.py" and "whichcard.py" to the cards that you would like to list.

# Steps to Use
1. Update the prices of players in "playerprices.py".
2. Select a mode of operation: Web App list ("driverList.py"), Android list ("driverListDroid.py"), or relist ("driverRelist.py").
3. Modify the file to select the number of cards that you would like to list.
4. Optionally modify the file to determine the amount of variance to the price (prevents all cards from being close together with the same price when set).
5. Run the program.
