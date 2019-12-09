import unittest
from Card import *

class TestCard(unittest.TestCase):
    @staticmethod
    def getAllCards() -> Card:
        for id in range(50):
            yield Card(cardId=id)

    def test_toShort(self):
        assumeResult = (
            "Y1", "Y1", "Y1", "Y2", "Y2", "Y3", "Y3", "Y4", "Y4", "Y5",
            "G1", "G1", "G1", "G2", "G2", "G3", "G3", "G4", "G4", "G5",
            "W1", "W1", "W1", "W2", "W2", "W3", "W3", "W4", "W4", "W5",
            "R1", "R1", "R1", "R2", "R2", "R3", "R3", "R4", "R4", "R5",
            "B1", "B1", "B1", "B2", "B2", "B3", "B3", "B4", "B4", "B5",
        )
        for card, assume in zip(TestCard.getAllCards(), assumeResult):
            # print(card.toShort(), assume)
            self.assertEqual(assume, card.toShort())

    def test_repr(self):
        assumeResult = (
            "Y1", "Y1", "Y1", "Y2", "Y2", "Y3", "Y3", "Y4", "Y4", "Y5",
            "G1", "G1", "G1", "G2", "G2", "G3", "G3", "G4", "G4", "G5",
            "W1", "W1", "W1", "W2", "W2", "W3", "W3", "W4", "W4", "W5",
            "R1", "R1", "R1", "R2", "R2", "R3", "R3", "R4", "R4", "R5",
            "B1", "B1", "B1", "B2", "B2", "B3", "B3", "B4", "B4", "B5",
        )
        for card, assume in zip(TestCard.getAllCards(), assumeResult):
            # print(card.toShort(), assume)
            self.assertEqual(card.toShort(), assume)

    def test_getSameColorOnceBefore(self):
        assumeResult = (
            "", "", "", "Y1", "Y1", "Y2", "Y2", "Y3", "Y3", "Y4",
            "", "", "", "G1", "G1", "G2", "G2", "G3", "G3", "G4",
            "", "", "", "W1", "W1", "W2", "W2", "W3", "W3", "W4",
            "", "", "", "R1", "R1", "R2", "R2", "R3", "R3", "R4",
            "", "", "", "B1", "B1", "B2", "B2", "B3", "B3", "B4",
        )
if __name__ == '__main__':
    unittest.main()
