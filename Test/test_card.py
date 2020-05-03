from unittest import TestCase


class TestCard(TestCase):
    def setUp(self):
        self.Card = Card()

    def est_initial_speed(self):
          self.assertEqual(self.car.speed, 0)

    pass
