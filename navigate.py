from locations import *
import utility
import pyautogui

def gotoNextCard():
    # clicks on the player tab
    moveX = utility.r(cardTab[0], cardTab[2])
    moveY = utility.r(cardTab[1], cardTab[3])
    pyautogui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pyautogui.click(moveX, moveY, 1, utility.r(0.5, 0.2)) # x, y, number of clicks, pause

    # scrolls down to next card and selects
    pyautogui.scroll(int(scroll / 2 * -1 + 3), None, None, utility.r(0.5, 0.2)) # clicks, x, y, pause
    pyautogui.click()



def droidGotoNextCard():
    # clicks on the right arrow tab
    moveX = utility.r(droidRightCard[0], droidRightCard[2])
    moveY = utility.r(droidRightCard[1], droidRightCard[3])
    pyautogui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pyautogui.click(moveX, moveY, 1, utility.r(1, 0.2)) # x, y, number of clicks, pause



def refreshPage():
    # refreshes the page
    moveX = refreshButton[0]
    moveY = refreshButton[1]
    pyautogui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pyautogui.click(moveX, moveY, 1, utility.r(0.5, 0.2)) # x, y, number of clicks, pause

    # checks for login button and presses if present
    utility.s(10)
    moveX = utility.r(loginButton[0], loginButton[2])
    moveY = utility.r(loginButton[1], loginButton[3])
    pyautogui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pyautogui.click(moveX, moveY, 1, utility.r(0.5, 0.2)) # x, y, number of clicks, pause
    
    # pauses to make sure that main menu is displayed
    utility.s(20)



def gotoUnassigned():
    # clicks on home button
    moveX = utility.r(homeButton[0], homeButton[2])
    moveY = utility.r(homeButton[1], homeButton[3])
    pyautogui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pyautogui.click(moveX, moveY, 1, utility.r(2.2, 0.3)) # x, y, number of clicks, pause

    # clicks on unassigned
    moveX = utility.r(unassignedButton[0], unassignedButton[2])
    moveY = utility.r(unassignedButton[1], unassignedButton[3])
    pyautogui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pyautogui.click(moveX, moveY, 1, utility.r(2.2, 0.3)) # x, y, number of clicks, pause

    
    
