# file with different utility functions

import random
import pyautogui
import time

# adds a bit of range to the value
def r(num, rand):
    return num + rand*random.random()

# tabs out to the program
def tabOut():
    pyautogui.keyDown('alt')
    # pyautogui.typewrite(['tab', 'tab'], 0.1)
    pyautogui.typewrite(['tab'], 0.1)
    pyautogui.keyUp('alt')

# finds screen size and current mouse position
def screen():
    print(pyautogui.position())
    print(pyautogui.size())

# returns the time
def t():
    return time.time()

# pauses all functions for a specified time
def s(duration):
    time.sleep(duration)
