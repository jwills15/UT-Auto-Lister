import utility
import listcard
import whichcard
import navigate

# set the number of cards to list
cards = 64

# sets whether there is a coin variance between cards
#modeVariance = True
modeVariance = False
variance = 50


# records the start time
time1 = utility.t()
# tabs out to the web app
utility.tabOut()

# runs loop for number of cards to sell
for x in range(cards):
    # finds the price of the card by checking player image
    price = whichcard.player()
    # moves on to the next card if no price is found
    if price is None:
        navigate.gotoNextCard()
        # pauses the program before the next card
        utility.s(utility.r(1, 2))
    else:
        # adds price variance if in variance mode
        if modeVariance == True:
            price = int(utility.r(price, variance))
        # lists the card
        listcard.listCard(price)
        # pauses the program before the next card
        utility.s(utility.r(2, 2))

    # if x is 49 or x is 99:
    #     # end of unassigned, refreshes page
    #     navigate.refreshPage()
    #     navigate.gotoUnassigned()

# output at the end of the program
print("Number of cards: " + str(cards))
print("Time: " + str(utility.t() - time1) + " seconds")
