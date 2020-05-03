from unittest import TestCase


class TestHand(TestCase):
    def test_newHand(self):
        self.fail()

    def test_deal(self):
        self.deal()
        self.assertEqual(len(self.hand),2,"Passed if new hand has 2 cards")
        self.fail()

    def test_splitCheck(self):
        self.fail()

    def test_total(self):
        self.fail()

    def test_hit(self):
        self.fail()
