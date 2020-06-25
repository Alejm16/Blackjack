class Card:

    def __init__(self,suit,number):
        self.suit = suit
        self.number = number

    def GetSuit(self):
        print(self.suit)

    def GetNumber(self):
        print(self.number)
    
    def PrintAll(self):
        print(self.suit,self.number ) 

def BlackJackShuffle(aList):
    length = len(aList)
    middleNum = length//2 #Divides with inegral result
    firstHalf = aList[:middleNum] # Gets first half
    secondHalf = aList[middleNum:] #Gets second half

    i = 0
    j = 0
    k = 0
    for x in aList:
        if i%2 == 0:
            aList[i] = firstHalf[j]
            j+=1
        else:
            aList[i] = secondHalf[k]
            k+=1
        i+=1

    



