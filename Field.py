from typing import *
from Card import *

class PlayResult:
    class  Success:
        type = "Success"
    class Failed:
        type = "Failed"

class Field:
    def __init__(self):
        self.played = []
        self.trash = []
        self.completeColors = 0
        self.hintRemain = 8
        self.hintInitial = 8
        self.failedCount = 0
        self.thresholdFailGameOver = 3

    def play(self, card: Card) -> Union[PlayResult.Success, PlayResult.Failed]:
        """judge card if valid."""
        theCardNumIsOne = False
        playedOnceBefore = False
        playedSame = False

        if card.number == 1:
            theCardNumIsOne = True

        # check if the card have same color and have once before number is played
        for p in self.played:
            if card.getSameColorOnceBefore() == p.toShort():
                playedOnceBefore = True
                break

        # check if the same card is played
        for p in self.played:
            if card.toShort() == p.toShort():
                playedSame = True
                break

        if (theCardNumIsOne or playedOnceBefore) and (not playedSame):
            # print(theCardNumIsOne, playedOnceBefore, playedSame)
            # recover a hint when you complete a color
            if (card.number == 5) and ( self.hintRemain < self.hintInitial):
                self.completeColors += 1
                self.hintRemain += 1
            self.played.append(card)
            return PlayResult.Success()
        else:
            self.trash.append(card)
            return PlayResult.Failed()

    def recoverHint(self, card):
        """trash a card and recovery hint count"""
        if self.hintRemain >= self.hintInitial:
            raise ValueError("already the hint count is initial")
        self.hintRemain += 1
        self.trash.append(card)
        return (card, self.hintRemain)

    def consumeHint(self):
        if self.hintRemain <= 0:
            raise ValueError("no hint remains")
        self.hintRemain -= 1
        return self.hintRemain
