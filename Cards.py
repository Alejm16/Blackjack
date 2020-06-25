class Card:

    def __init__(self,suit,number):
        self.suit = suit
        self.number = number

    def GetSuit(self):
        print(self.suit)

    def GetNumber(self):
        print(self.number)
    
    def PrintAll(self):
        print(self.suit + " " + self.number)

rank = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suit = ["Clubs","Hears","Diamonds","Spades"]

deck = []


for x in rank:
    for y in suit:
       deck.append(Card(x,y))

for x in deck:
    print (x.GetNumber) 
   

