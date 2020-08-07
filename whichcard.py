# module that finds which card is being looked at

from locations import *
from imagesearch import *
import playerprices

def player():
    # finds the card on the screen
    im = region_grabber((playerCard[0], playerCard[1],
                         playerCard[2], playerCard[3]))

    # compares the image region with images of players
    if imagesearcharea("images/adan.png", 0, 0, 0, 0, 0.8, im):
        player = "adan"
    elif imagesearcharea("images/balotelli.png", 0, 0, 0, 0, 0.8, im):
        player = "balotelli"
    elif imagesearcharea("images/banega.png", 0, 0, 0, 0, 0.8, im):
        player = "banega"
    elif imagesearcharea("images/baumann.png", 0, 0, 0, 0, 0.8, im):
        player = "baumann"
    elif imagesearcharea("images/carrasco.png", 0, 0, 0, 0, 0.8, im):
        player = "carrasco"
    elif imagesearcharea("images/casteels.png", 0, 0, 0, 0, 0.8, im):
        player = "casteels"
    elif imagesearcharea("images/bruno.png", 0, 0, 0, 0, 0.8, im):
        player = "bruno"
    elif imagesearcharea("images/danilo.png", 0, 0, 0, 0, 0.8, im):
        player = "danilo"
    elif imagesearcharea("images/fahrmann.png", 0, 0, 0, 0, 0.8, im):
        player = "fahrmann"
    elif imagesearcharea("images/felipe.png", 0, 0, 0, 0, 0.8, im):
        player = "felipe"
    elif imagesearcharea("images/giuliano.png", 0, 0, 0, 0, 0.8, im):
        player = "giuliano"
    elif imagesearcharea("images/glik.png", 0, 0, 0, 0, 0.8, im):
        player = "glik"
    elif imagesearcharea("images/gustavo.png", 0, 0, 0, 0, 0.8, im):
        player = "gustavo"
    elif imagesearcharea("images/hazard.png", 0, 0, 0, 0, 0.8, im):
        player = "hazard"
    elif imagesearcharea("images/horn.png", 0, 0, 0, 0, 0.8, im):
        player = "horn"
    elif imagesearcharea("images/jose.png", 0, 0, 0, 0, 0.8, im):
        player = "jose"
    elif imagesearcharea("images/kagawa.png", 0, 0, 0, 0, 0.8, im):
        player = "kagawa"
    elif imagesearcharea("images/kepa.png", 0, 0, 0, 0, 0.8, im):
        player = "kepa"
    elif imagesearcharea("images/kramaric.png", 0, 0, 0, 0, 0.8, im):
        player = "kramaric"
    elif imagesearcharea("images/leiva.png", 0, 0, 0, 0, 0.8, im):
        player = "leiva"
    elif imagesearcharea("images/malcom.png", 0, 0, 0, 0, 0.8, im):
        player = "malcom"
    elif imagesearcharea("images/mandanda.png", 0, 0, 0, 0, 0.8, im):
        player = "mandanda"
    elif imagesearcharea("images/morata.png", 0, 0, 0, 0, 0.8, im):
        player = "morata"
    elif imagesearcharea("images/moreno.png", 0, 0, 0, 0, 0.8, im):
        player = "moreno"
    elif imagesearcharea("images/pickford.png", 0, 0, 0, 0, 0.8, im):
        player = "pickford"
    elif imagesearcharea("images/pizzi.png", 0, 0, 0, 0, 0.8, im):
        player = "pizzi"
    elif imagesearcharea("images/reina.png", 0, 0, 0, 0, 0.8, im):
        player = "reina"
    elif imagesearcharea("images/rui.png", 0, 0, 0, 0, 0.8, im):
        player = "rui"
    elif imagesearcharea("images/sarabia.png", 0, 0, 0, 0, 0.8, im):
        player = "sarabia"
    elif imagesearcharea("images/savic.png", 0, 0, 0, 0, 0.8, im):
        player = "savic"
    elif imagesearcharea("images/strootman.png", 0, 0, 0, 0, 0.8, im):
        player = "strootman"
    elif imagesearcharea("images/subasic.png", 0, 0, 0, 0, 0.8, im):
        player = "subasic"
    elif imagesearcharea("images/suso.png", 0, 0, 0, 0, 0.8, im):
        player = "suso"
    elif imagesearcharea("images/trigueros.png", 0, 0, 0, 0, 0.8, im):
        player = "trigueros"
    elif imagesearcharea("images/vazquez.png", 0, 0, 0, 0, 0.8, im):
        player = "vazquez"
    elif imagesearcharea("images/visca.png", 0, 0, 0, 0, 0.8, im):
        player = "visca"
    elif imagesearcharea("images/viviano.png", 0, 0, 0, 0, 0.8, im):
        player = "viviano"
    else:
        return None
        
    # returns the price
    return playerprices.pricedict[player]


def droidPlayer():
    # finds the card on the screen
    im = region_grabber((droidPlayerCard[0], droidPlayerCard[1],
                         droidPlayerCard[2], droidPlayerCard[3]))

    # compares the image region with images of players
    if imagesearcharea("images/droid/adan.png", 0, 0, 0, 0, 0.8, im):
        player = "adan"
    elif imagesearcharea("images/droid/balotelli.png", 0, 0, 0, 0, 0.8, im):
        player = "balotelli"
    elif imagesearcharea("images/droid/banega.png", 0, 0, 0, 0, 0.8, im):
        player = "banega"
    elif imagesearcharea("images/droid/baumann.png", 0, 0, 0, 0, 0.8, im):
        player = "baumann"
    elif imagesearcharea("images/droid/carrasco.png", 0, 0, 0, 0, 0.8, im):
        player = "carrasco"
    elif imagesearcharea("images/droid/casteels.png", 0, 0, 0, 0, 0.8, im):
        player = "casteels"
    elif imagesearcharea("images/droid/danilo.png", 0, 0, 0, 0, 0.8, im):
        player = "danilo"
    elif imagesearcharea("images/droid/felipe.png", 0, 0, 0, 0, 0.8, im):
        player = "felipe"
    elif imagesearcharea("images/droid/giuliano.png", 0, 0, 0, 0, 0.8, im):
        player = "giuliano"
    elif imagesearcharea("images/droid/glik.png", 0, 0, 0, 0, 0.8, im):
        player = "glik"
    elif imagesearcharea("images/droid/gustavo.png", 0, 0, 0, 0, 0.8, im):
        player = "gustavo"
    elif imagesearcharea("images/droid/hazard.png", 0, 0, 0, 0, 0.8, im):
        player = "hazard"
    elif imagesearcharea("images/droid/jose.png", 0, 0, 0, 0, 0.8, im):
        player = "jose"
    elif imagesearcharea("images/droid/kagawa.png", 0, 0, 0, 0, 0.8, im):
        player = "kagawa"
    elif imagesearcharea("images/droid/kramaric.png", 0, 0, 0, 0, 0.8, im):
        player = "kramaric"
    elif imagesearcharea("images/droid/leiva.png", 0, 0, 0, 0, 0.8, im):
        player = "leiva"
    elif imagesearcharea("images/droid/malcom.png", 0, 0, 0, 0, 0.8, im):
        player = "malcom"
    elif imagesearcharea("images/droid/mandanda.png", 0, 0, 0, 0, 0.8, im):
        player = "mandanda"
    elif imagesearcharea("images/droid/morata.png", 0, 0, 0, 0, 0.8, im):
        player = "morata"
    elif imagesearcharea("images/droid/moreno.png", 0, 0, 0, 0, 0.8, im):
        player = "moreno"
    elif imagesearcharea("images/droid/pickford.png", 0, 0, 0, 0, 0.8, im):
        player = "pickford"
    elif imagesearcharea("images/droid/pizzi.png", 0, 0, 0, 0, 0.8, im):
        player = "pizzi"
    elif imagesearcharea("images/droid/sarabia.png", 0, 0, 0, 0, 0.8, im):
        player = "sarabia"
    elif imagesearcharea("images/droid/savic.png", 0, 0, 0, 0, 0.8, im):
        player = "savic"
    elif imagesearcharea("images/droid/strootman.png", 0, 0, 0, 0, 0.8, im):
        player = "strootman"
    elif imagesearcharea("images/droid/suso.png", 0, 0, 0, 0, 0.8, im):
        player = "suso"
    elif imagesearcharea("images/droid/trigueros.png", 0, 0, 0, 0, 0.8, im):
        player = "trigueros"
    elif imagesearcharea("images/droid/vazquez.png", 0, 0, 0, 0, 0.8, im):
        player = "vazquez"
    elif imagesearcharea("images/droid/visca.png", 0, 0, 0, 0, 0.8, im):
        player = "visca"
    elif imagesearcharea("images/droid/viviano.png", 0, 0, 0, 0, 0.8, im):
        player = "viviano"
    else:
        return None
        
    # returns the price
    return playerprices.pricedict[player]



# function used for determining if card sold or needs to be relisted
def didNotSell():
    # checks whether there is a card that did not sell
    im = region_grabber((redX[0], redX[1],
                         redX[2], redX[3]))
    # compares the image region with image of red X
    if imagesearcharea("images/redX.png", 0, 0, 0, 0, 0.8, im):
        return True
    else:
        return False
