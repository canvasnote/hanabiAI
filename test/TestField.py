import unittest
from Field import *

class TestField(unittest.TestCase):
    def test_played(self):
        field = Field()
        field.hintRemain -= 1
        # O1 => Success
        self.assertEqual(
            type(PlayResult.Success()),
            type(field.play(Card(cardId=0))))
        # print(field.played)
        # O1 => Fail because the same card already played
        self.assertEqual(
            type(PlayResult.Failed()),
            type(field.play(Card(cardId=0))))
        # print(field.played)
        # O3 => Fail
        self.assertEqual(
            type(PlayResult.Failed()),
            type(field.play(Card(cardId=5))))
        # print(field.played)
        # O2 => Success
        self.assertEqual(
            type(PlayResult.Success()),
            type(field.play(Card(cardId=3))))
        # print(field.played)
        # O3 => Success
        self.assertEqual(
            type(PlayResult.Success()),
            type(field.play(Card(cardId=5))))
        # print(field.played)
        # O4 => Success
        self.assertEqual(
            type(PlayResult.Success()),
            type(field.play(Card(cardId=7))))
        # print(field.played)
        # O5 => Success and recovery a hint
        self.assertEqual(
            type(PlayResult.Success()),
            type(field.play(Card(cardId=9))))
        # print(field.played)
        # check if hint is recovered
        self.assertEqual(
            8,
            field.hintRemain
        )

    def test_recoverHint(self):
        field = Field()
        field.hintRemain = 0
        self.assertEqual(1, field.recoverHint(Card(cardId=0))[1])
        self.assertEqual(2, field.recoverHint(Card(cardId=0))[1])
        self.assertEqual(3, field.recoverHint(Card(cardId=0))[1])
        self.assertEqual(4, field.recoverHint(Card(cardId=0))[1])
        self.assertEqual(5, field.recoverHint(Card(cardId=0))[1])
        self.assertEqual(6, field.recoverHint(Card(cardId=0))[1])
        self.assertEqual(7, field.recoverHint(Card(cardId=0))[1])
        self.assertEqual(8, field.recoverHint(Card(cardId=0))[1])
        with self.assertRaises(ValueError):
            field.recoverHint(Card(cardId=0))

    def test_consumeHint(self):
        field = Field()
        self.assertEqual(7, field.consumeHint())
        self.assertEqual(6, field.consumeHint())
        self.assertEqual(5, field.consumeHint())
        self.assertEqual(4, field.consumeHint())
        self.assertEqual(3, field.consumeHint())
        self.assertEqual(2, field.consumeHint())
        self.assertEqual(1, field.consumeHint())
        self.assertEqual(0, field.consumeHint())
        with self.assertRaises(ValueError):
            field.consumeHint()


if __name__ == '__main__':
    unittest.main()
