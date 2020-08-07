import utility
import listcard
import whichcard
import navigate

# set the number of cards to list
cards = 8

# sets whether there is a coin variance between cards
#modeVariance = True
modeVariance = False
variance = 100


# records the start time
time1 = utility.t()
# tabs out to the android app
utility.tabOut()

# phone screen location

# runs loop for number of cards to sell
for x in range(cards):
    # finds the price of the card by checking player image
    price = whichcard.droidPlayer()
    # moves on to the next card if no price is found
    if price is None:
        navigate.droidGotoNextCard()
        # pauses the program before the next card
        utility.s(utility.r(1, 2))
    else:
        # adds price variance if in variance mode
        if modeVariance == True:
            price = int(utility.r(price, variance))
        # lists the card
        listcard.droidListCard(price)

        # uncomment if listing from transfer list
        utility.s(0.5)
        navigate.droidGotoNextCard()
        
        # pauses the program before the next card
        utility.s(utility.r(2, 2))


# output at the end of the program
print("Number of cards: " + str(cards))
print("Time: " + str(utility.t() - time1) + " seconds")
