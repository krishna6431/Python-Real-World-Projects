# Python Mini Project ScreenShot APP
# Code is Written By Krishna 

#Module Needed;
# time Module
# pyautogui module

# import time and pyatogui module 
import time
import pyautogui

# lets create a function which takes screenshot 

def screenshot():
    name = int(round(time.time()*1000)) #this statement generates a random no which works as a file name
    # lets create a variable name and format it
    name = 'D:\Python Real World Mini Projects\ScreenShotAPP\ScreenShots\{}.png'.format(name)
    #lets intialize a time delay of 5 sec after running this program
    time.sleep(5)

    # lets create a variable which store the screenshot image
    img = pyautogui.screenshot(name)
    img.show()  # .show() function displays the captured image screenshot
# lets invoke the screenshot function

screenshot()
