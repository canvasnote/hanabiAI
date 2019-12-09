import unittest
from Deck import *
from Card import *


class TestDeck(unittest.TestCase):
    def test_init(self):
        # starter
        assumeResult = \
            "Y1 Y1 Y1 Y2 Y2 Y3 Y3 Y4 Y4 Y5 " + \
            "G1 G1 G1 G2 G2 G3 G3 G4 G4 G5 " + \
            "W1 W1 W1 W2 W2 W3 W3 W4 W4 W5 " + \
            "R1 R1 R1 R2 R2 R3 R3 R4 R4 R5 " + \
            "B1 B1 B1 B2 B2 B3 B3 B4 B4 B5"
        starterDeck = Deck()
        self.assertEqual(assumeResult, starterDeck.reprCards())

        # given initial, [Y1, G2, W3, R4, B5]
        assumeResult = "Y1 G2 W3 R4 B5"
        initial = [
            Card(cardId=0),
            Card(cardId=13),
            Card(cardId=25),
            Card(cardId=37),
            Card(cardId=49),
        ]
        initialGivenDeck = Deck(initial=initial)
        self.assertEqual(assumeResult, initialGivenDeck.reprCards())

    def test_draw(self):
        deck = Deck(_seed=12345)
        assumeResult = ("W3", "B4", "Y1", "W1", "W3", "G2", "G5", "B1", "R2")
        for assume in assumeResult:
            # print(deck.draw().toShort())
            self.assertEqual(assume, deck.draw().toShort())

    def test_remainCardNum(self):
        deck = Deck()
        assumeResult = (49 - x for x in range(50))

        # initial
        self.assertEqual(50, deck.remainCardNum())

        # each draws
        for assume in assumeResult:
            deck.draw()
            self.assertEqual(assume, deck.remainCardNum())

    def test_remainCardList(self):
        deck = Deck(_seed=12345)
        assumeResult = (
            "W3", "B4", "Y1", "W1", "W3",
            "G2", "G5", "B1", "R2", "G1",
            "R1", "Y4", "R4", "W1", "B5",
            "G3", "G3", "R3", "Y3", "W4",
            "B1", "W2", "R2", "R1", "Y4",
            "Y3", "G1", "Y2", "G4", "W5",
            "R1", "Y1", "B2", "R4", "Y1",
            "R3", "B3", "B3", "W2", "Y2",
            "Y5", "G4", "W1", "W4", "G1",
            "B2", "G2", "B4", "R5", "B1")
        for assume in assumeResult:
            # print(deck.draw())
            self.assertEqual(assume, deck.draw().toShort())

    def test_drewCardList(self):
        deck = Deck(_seed=12345)
        assumeResult = (
            "W3", "B4", "Y1", "W1", "W3",
            "G2", "G5", "B1", "R2", "G1",
            "R1", "Y4", "R4", "W1", "B5",
            "G3", "G3", "R3", "Y3", "W4",
            "B1", "W2", "R2", "R1", "Y4",
            "Y3", "G1", "Y2", "G4", "W5",
            "R1", "Y1", "B2", "R4", "Y1",
            "R3", "B3", "B3", "W2", "Y2",
            "Y5", "G4", "W1", "W4", "G1",
            "B2", "G2", "B4", "R5", "B1")
        for _ in range(len(assumeResult)):
            deck.draw()
        remains = (
            card.toShort()
            for card
            in deck.remainCardList()
        )
        for assume, remain in zip(assumeResult, remains):
            self.assertEqual(assume, remains)


if __name__ == '__main__':
    unittest.main()
