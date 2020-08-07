# module that lists card when given a price

import pyautogui as pygui
import utility
from locations import *

def listCard(price):
    # clicks on the "List on Transfer Market" tab
    moveX = utility.r(listTab[0], listTab[2])
    moveY = utility.r(listTab[1], listTab[3])
    pygui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(0.5, 0.2)) # x, y, number of clicks, pause

    # scrolls down to reveal price buttons
    pygui.scroll(scroll * -1, None, None, utility.r(0.1, 0.2)) # clicks, x,  y, pause

    # inputs the start price
    moveX = utility.r(startPrice[0], startPrice[2])
    moveY = utility.r(startPrice[1], startPrice[3])
    pygui.moveTo(moveX, moveY, utility.r(0.2, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(0, 0.2)) # x, y, number of clicks, pause
    pygui.typewrite(str(price))

    # inputs the BIN price
    moveX = utility.r(BINPrice[0], BINPrice[2])
    moveY = utility.r(BINPrice[1], BINPrice[3])
    pygui.moveTo(moveX, moveY, utility.r(0.2, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(0, 0.2)) # x, y, number of clicks, pause
    pygui.typewrite(str(price))

    # clicks on the "List Item" button
    moveX = utility.r(listButton[0], listButton[2])
    moveY = utility.r(listButton[1], listButton[3])
    pygui.moveTo(moveX, moveY, utility.r(0.2, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(3, 0.2)) # x, y, number of clicks, pause

    # scrolls up to reveal card
    pygui.scroll(scroll, None, None, utility.r(0.1, 0.2)) # clicks, x, y, pause



def droidListCard(price):
    # clicks on the "List on Transfer Market" tab
    moveX = utility.r(droidListTab[0], droidListTab[2])
    moveY = utility.r(droidListTab[1], droidListTab[3])
    pygui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(1, 0.2)) # x, y, number of clicks, pause

    # scrolls down to reveal price buttons
    pygui.mouseDown()
    pygui.moveTo(moveX, moveY - scroll, utility.r(0.3, 0.2)) # x, y, duration
    pygui.mouseUp()
    utility.s(0.5)

    # inputs the start price
    moveX = utility.r(droidStartPrice[0], droidStartPrice[2])
    moveY = utility.r(droidStartPrice[1], droidStartPrice[3])
    pygui.moveTo(moveX, moveY, utility.r(0.2, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(0, 0.2)) # x, y, number of clicks, pause
    utility.s(0.5)
    pygui.typewrite(str(price))
    utility.s(1)

    # inputs the BIN price
    moveX = utility.r(droidBINPrice[0], droidBINPrice[2])
    moveY = utility.r(droidBINPrice[1], droidBINPrice[3])
    pygui.moveTo(moveX, moveY, utility.r(0.2, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(0, 0.2)) # x, y, number of clicks, pause
    utility.s(0.5)
    pygui.typewrite(str(price))
    utility.s(1)

    # clicks on the "List Item" button
    moveX = utility.r(droidListButton[0], droidListButton[2])
    moveY = utility.r(droidListButton[1], droidListButton[3])
    pygui.moveTo(moveX, moveY, utility.r(0.2, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(3, 0.2)) # x, y, number of clicks, pause
    utility.s(0.5)

    # scrolls up to reveal card
    pygui.moveTo(moveX, moveY - scroll, utility.r(0.3, 0.2)) # x, y, duration
    pygui.mouseDown()
    pygui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pygui.mouseUp()



def relistCard():
    # clicks on the "List on Transfer Market" tab
    moveX = utility.r(listTab[0], listTab[2])
    moveY = utility.r(listTab[1], listTab[3])
    pygui.moveTo(moveX, moveY, utility.r(0.3, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(0.5, 0.2)) # x, y, number of clicks, pause

    # scrolls down to reveal price buttons
    pygui.scroll(scroll * -1, None, None, utility.r(0.1, 0.2)) # clicks, x,  y, pause

    # clicks on the "List Item" button
    moveX = utility.r(listButton[0], listButton[2])
    moveY = utility.r(listButton[1], listButton[3])
    pygui.moveTo(moveX, moveY, utility.r(0.2, 0.2)) # x, y, duration
    pygui.click(moveX, moveY, 1, utility.r(2, 0.2)) # x, y, number of clicks, pause

    # scrolls up to reveal card
    pygui.scroll(scroll, None, None, utility.r(0.1, 0.2)) # clicks, x, y, pause

