import random

class Deck:

    deck_start = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    num = 0

    def __init__(self, num):
        self.num = num
        self.deck = self.deck_start
        for i in range(0, num):
            self.deck.extend()
        self.shuffle()

    def shuffle(self):
        self.deck.shuffle()
    
    def draw(self):
        if(self.deckCount() == 0):
            self.reShuffle()
        return self.deck.pop()

    def deckCount(self):
        return self.deck.count() 

    def reShuffle(self):
        for i in range(0, self.num):
            self.deck.extend()
        self.shuffle()

    # prob want to do this in hand class
        """  def getValue(self, card):
        if(card == "A"):
            return 1
        else if(card == "J" or card == "Q" or card == "K"):
            return 10
        else:
            return int(card)
         """
    
    
