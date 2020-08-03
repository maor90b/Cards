from unittest import TestCase
from unittest.mock import patch
from Game_Card2.DeckOfCards import DeckOfCards
from Game_Card2.Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        print('setup')
        self.d = DeckOfCards()
        self.d2 = DeckOfCards()
        self.d3 = DeckOfCards()


    def tearDown(self):
        print('TearDown')


    def test_deal_one(self):
        self.assertTrue(self.d.deck[-1] == self.d.deal_one())
        card=self.d.deal_one()
        self.assertTrue(type(card)==Card)
        for i in range(len(self.d.deck)):
            self.d.deal_one()
        self.assertTrue(self.d.deck == [])
        self.assertTrue(len(self.d.deck)==0)


    def test_new_game(self):
        self.d.new_game()
        self.assertTrue(len(self.d.deck) == 52)



    def test_show(self):
        pass
