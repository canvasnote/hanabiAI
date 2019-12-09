import os

from Player import *
from PlayerAI import *
from Deck import *
from Field import *


class GameMaster:
    def __init__(self, playersNum: int, playerAI: PlayerAI):
        self.defaultHandsNum = 5 if playersNum == 3 else 4
        if playersNum == 3:
            self.turnTable = ((1, 2), (2, 0), (1, 2))
        if playersNum == 4:
            self.turnTable = ((1, 2, 3), (2, 3, 0), (3, 0, 1), (0, 1, 2))
        if playersNum == 5:
            self.turnTable = ((1, 2, 3, 4), (2, 3, 4, 0), (3, 4, 0, 1), (4, 0, 1, 2), (1, 2, 3, 4))
        self.deck = Deck()
        self.players: List[Player] = [
            Player(
                id=id,
                hand=Hand(cards=[self.deck.draw() for _ in range(self.defaultHandsNum)]),
                playerAI=playerAI)
            for id
            in range(playersNum)
        ]
        self.field = Field()
        self.turnNum = 1
        self.currentPlayer = 0
        self.isGameOver = False

    def start(self):
        while True:
            self.turn()
            if self.isGameOver:
                score: int = self.calcScore()
                print('Game Over.')
                print(f'Score: {score}')
                return score

    def calcScore(self) -> int:
        return len(self.field.played) + self.field.completeColors

    def turn(self):
        print(
            f'Turn {self.turnNum}: Hands {[player.hand for player in self.players]}, Hint: {self.field.hintRemain}, Fail: {self.field.failedCount}, Deck: {self.deck.remainCardNum()}, Field: {self.field.played}, Trash: {self.field.trash}')
        otherHands: List[Hand] = []
        for i in self.turnTable[self.currentPlayer]:
            otherHands.append(self.players[i].hand)

        # play card
        print(f' => currentPlayer: {self.currentPlayer}')
        playerChoice = self.players[self.currentPlayer].guess(field=self.field, otherPlayerCoveredHands=otherHands)
        if type(playerChoice) == PlayCard:
            playResult = self.field.play(playerChoice.card)
            self.players[self.currentPlayer].playCard(playerChoice.cardIndex)
            self.players[self.currentPlayer].draw(self.deck)
            print(f' => playCard: {playerChoice.card}, {playResult.type}')
            if type(playResult) == PlayResult.Success:
                pass
            if type(playResult) == PlayResult.Failed:
                self.field.failedCount += 1
                if self.field.failedCount == self.field.thresholdFailGameOver:
                    self.isGameOver = True

        # trash a card
        if type(playerChoice) == TrashCard:
            self.players[playerChoice.playerID].trash(playerChoice.cardIndex)

        # hint info to a player
        if type(playerChoice) == Hint:
            self.players[playerChoice.playerID].hinted(playerChoice.hint)

        self.currentPlayer += 1
        if self.currentPlayer == len(self.players):
            self.currentPlayer = 0
        self.turnNum += 1
