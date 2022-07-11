class Hand:

    hand = []
    ace = False

    def addCard(self, card):
        if(card == "A"):
            ace = True
        self.hand.append(card)

    def isSplitPossible(self):
        if(self.hand[0] == self.hand[1]):
            return True
        return False

    def isDoubleDownPossible(self):
        if(self.handCount == 2):
            return True
        else:
            return False

    def handCount(self):
        return self.hand.count()

        
