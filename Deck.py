from Cards import *

rank = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suit = ["Clubs","Hears","Diamonds","Spades"]

deck = []

for x in suit:# Creates the deck of cards 
    for y in rank:
        deck.append(Card(x,y))

for x in deck:
    x.PrintAll()

BlackJackShuffle(deck)

print("DECK SHUFFLED")
for x in deck:
    x.PrintAll()








