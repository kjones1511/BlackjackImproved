import unittest
from bjObjects import *

#class TestHand(TestCase):
class TestDeck(unittest.TestCase):
    #counts number of matching cards, if greater than 45 assuming deck didn't shuffle
    def test_shuffle(self):
        tDeck = Deck(1)
        tDeckNonShuffle = Deck(1)
        tDeck.shuffle()
        error = 0
        for i in range(52):
            if tDeck.cards[i] == tDeckNonShuffle.cards[i]:
                error += 1
        self.assertTrue( error < 45, "More than 45 cards are the same, deck probably didn't shuffle")

    def test_pop(self):
        tDeck = Deck(2)
        tCard = tDeck.pop()
        self.assertEqual( tCard, Card("C",2), "Top card is still 2 of Clubs, deck failed to shuffle")

if __name__ == '__main__':
    unittest.main()
