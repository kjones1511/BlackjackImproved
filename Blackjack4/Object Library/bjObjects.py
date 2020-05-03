import random
import json
#todo: destructors?
#adding comment to commit

class Card:
    #suit is string, value should be integer
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
#        self.__dict__ = {"suit": self.suit, "value": self.value}

#    def __dict__(self):
#        return {"suit": self.suit, "value": self.value}

    def __str__(self):
        pVal = self.value
        if self.value == 11: pVal = "J"
        elif self.value == 12: pVal = "Q"
        elif self.value == 13: pVal = "K"
        elif self.value == 14: pVal = "A"
        return "[" + self.suit + ", " + str(pVal) + "]"

class Hand:
    def __init__(self):
        self.hand = []
        self.blackjack = 0
        self.win = 0
        self.split = 0
        self.double = 0
        self.hitState = 0 # 0 if stand, 1 if hit
        self.dealerHand = []
        self.dealerScore = 0
        self.score = 0
        self.originalScore = 0

    def newHand(self,deck):
        self.hand.clear()
        self.blackjack = 0
        self.win = 0
        self.double = 0
        self.state = 0
        self.deal(deck)

    def deal(self, deck):
        for i in range(2):
            self.hand.append( deck.pop() )
        self.originalScore = self.total() #todo: testing if score function works

    #function to see if a split is possible. Assumes new hand (only 2 elements)
    def splitCheck(self):
        if len(self.hand) != 2:
            print("Hand not appropriate for a splitCheck()")
            return False
        if self.hand[0].value == self.hand[1].value:
            return True
        return False

    def __str__(self):
        handStr = str(self.hand[0])
        for card in self.hand[1:]:
            handStr = handStr + ", " + str(card)
        return handStr

    def total(self):
        total = 0
        for card in self.hand:
            card = card.value
            if card in [11, 12, 13]:
                total += 10
            elif card == 14:
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += int(card)
        return total

    def hit(self, deck):
        card = deck.pop()
        self.hand.append(card)

class Deck:
    def __init__(self, deckCount):
        dSuit = ["C","H","S","D"]  * 13 * deckCount
        dValue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4 * deckCount
        self.cards = []
        for i in range(52*deckCount):
            self.cards.append( Card(dSuit.pop(),dValue.pop()) )

    def shuffle(self):
        random.shuffle(self.cards)

    def peek(self, number):
        for i in range(number):
            print(self.cards[-1*i])

    def pop(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, initial_money):
        self.name = name
        self.hands = []
        self.currentHand = [] #will be array of hands
        self.money = initial_money

    #handIndex assumes moving through currentHand index in ascending order
    def split(self, handIndex,deck):
        #ends the function if handIndex throws an error
        if handIndex == -1:
            return
        self.currentHand.insert(handIndex+1, Hand())
        #adds last card in currentHand point, to new empty hand
        self.currentHand[handIndex+1].hand.append( self.currentHand[handIndex].hand.pop() )
        #adds new card to each hand
        for i in range(handIndex,handIndex++2):
            self.currentHand[i].hit(deck)
            self.currentHand[i].split = 1
            self.currentHand[i].originalScore = self.currentHand[i].total() #todo: testing if this works, score is in diff library

if __name__ == "__main__":

    player =Player("kile",100)

    card1 = Card("S",7)
    card2 = Card("D",7)
    card3 = Card("D",7)
    deck = Deck(2)
    deck.shuffle()
    hand = Hand()
    player.currentHand.append(hand)
    player.currentHand[0].hand = [ card1, card2, card3]

    data = json.dumps(player.__dict__, default = lambda o:o.__dict__)
    print(data)
    #print( vars(card1) )
    #print(vars(player.currentHand[0]))
