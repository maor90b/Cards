from unittest import TestCase, mock
# from unittest.mock import patch
from Game_Card2.Player import Player
from Game_Card2.DeckOfCards import DeckOfCards


# from Game_Card2.Card import Card

class TestPlayer(TestCase):

    def setUp(self):
        print('setup')
        self.d = DeckOfCards()
        self.d2 = DeckOfCards()
        self.d3 = DeckOfCards()

        self.p = Player('maor')
        self.p2 = Player('philips')
        self.p3 = Player('mike')

    def tearDown(self):
        print('TearDown')

    def test_setHand(self):
        # self.d = DeckOfCards()
        # self.d2 = DeckOfCards()
        # self.p = Player('maor')

        self.p.setHand(self.d)

        for i in self.p.list_cards:
            for j in range(len(self.d.deck)):
                self.assertFalse(i == self.d.deck[j])
        self.assertTrue(len(self.d.deck) == len(self.d2.deck) - 5)
        self.assertTrue(len(self.p.list_cards) == 5)
        # for a in self.p.list_cards:
        #     self.assertIn(a, self.d2.deck)

    def test_getCard(self):
        # self.p = Player('maor')
        # self.p2 = Player('philips')
        self.p.setHand(self.d)
        self.p2.setHand(self.d)

        self.p2.getCard()
        self.assertTrue(len(self.p2.list_cards) == (len(self.p.list_cards) - 1))

        for i in range(len(self.p2.list_cards) + 10):
            self.p2.getCard()
        self.assertTrue(len(self.p2.list_cards) == 0)

    def test_addCard(self):
    #     self.p = Player('maor')
    #     self.p2 = Player('philips')
    #     self.d = DeckOfCards()

        self.p.setHand(self.d)
        self.p2.setHand(self.d)
        self.p2.addCard(self.d)
        self.assertTrue(len(self.p.list_cards) + 1 == len(self.p2.list_cards))
    #
    #     self.p3 = Player('mike')
    #     self.d2 = DeckOfCards
    #     self.d3=DeckOfCards()
        for i in range(100):
            self.p3.addCard(self.d2)
        print(self.p3.list_cards)
        print(len(self.p3.list_cards))
        self.assertEqual(len(self.p3.list_cards), len(self.d3.deck))

        self.assertEqual(len(self.p3.list_cards), len(self.d3.deck))

    # # def test_reduceAmount(self):
    # #     # self.p.reduceAmount(80000)
    # #     self.assertTrue(self.p.money == 0)
    # #
    # # def test_addAmount(self):
    #     # self.p2.addAmount(10001)
    #     self.assertTrue(self.p2.money == 10000)
    #
    #
    # def test_print(self):
    #     pass
    #
