
import unittest
from bjObjects import *

#class TestHand(TestCase):
class TestHand(unittest.TestCase):
    def test_newHand(self):
        testHand = Hand()
        self.assertIsNotNone(testHand,"Fails if new hand not generated")

    def test_deal(self):
        testHand = Hand()
        tDeck = Deck(2)
        testHand.deal(tDeck)
        self.assertEqual( len(testHand.hand) , 2, "Passed if new hand has 2 cards")

    def test_splitCheck(self):
        testHandPass = Hand()
        testHandPass.hand = [Card("H", 7), Card("D", 7)]
        self.assertTrue(testHandPass.splitCheck(), "Fails if testHand1 is not eligible to split")

        testHandFail = Hand()
        testHandFail.hand = [Card("H", 6), Card("H", 8)]
        self.assertFalse(testHandFail.splitCheck(), "Passes if testHand1 is not eligible to split")

    def test_total(self):
        testHands = [
            [ [Card("H", 7), Card("D", 7)], 14], #test matching values
            [ [Card("H", 7), Card("D", 7), Card("D", 10)], 24],  # test bust
            [[Card("H", 3), Card("J", 4),Card("J", 4)], 11], #test that 3+ cards can get scores
            [[Card("H", 2), Card("D", 10)], 12], #series of tests on face values
            [[Card("S", 4), Card("D", 11)], 14],
            [[Card("H", 3), Card("D", 12)], 13],
            [[Card("H", 11), Card("D", 13)], 20],
            [[Card("H", 11), Card("D", 14)], 21], #next few tests confirm Ace behavior
            [[Card("H", 4), Card("J", 14)], 15],
            [[Card("H", 6),Card("J", 6), Card("J", 14)], 13]
            #todo: test that 1 card shouldn't be scored alone [Card("J", 4)]
        ]

        i = 0
        for hand in testHands:
            i += 1
            tHand = Hand()
            for card in hand[0]:
                tHand.hand.append(card)
            self.assertEqual( tHand.total(), hand[1], "test case #" + str(i) + " was not equal to expected output")


    def test_hit(self):
        testHand = Hand()
        tDeck = Deck(2)
        testHand.deal(tDeck)
        testHand.hit(tDeck)
        self.assertEqual(len(testHand.hand), 3, "Fails if after 1 hit there aren't 3 cards")

if __name__ == '__main__':
    unittest.main()
