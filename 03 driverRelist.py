import utility
import listcard
import locations
import whichcard

# driver program to relist cards


# records the start time
time1 = utility.t()
# tabs out to the web app
utility.tabOut()

# instantiates variable
more = True
cards = 0

# runs loop for number of cards to relist
while more:
    # relists the card
    listcard.relistCard()
    # pauses the program before the next card
    utility.s(utility.r(3, 3))
    # checks if next card needs to be relisted
    more = whichcard.didNotSell()
    cards += 1

# output at the end of the program
print("Number of cards: " + str(cards))
print("Time: " + str(utility.t() - time1) + " seconds")
