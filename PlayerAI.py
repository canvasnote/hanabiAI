from Player import *
from Field import *


class PlayerAI:
    def guess(self, player: Player, field: Field, otherPlayerCoveredHands: List[Hand]) -> Play:
        pass


class AlwaysPlaysFirstCard(PlayerAI):
    def guess(self, player: Player, field: Field, otherPlayerCoveredHands: List[Hand]) -> Play:
        return PlayCard(card=player.hand.cards[0], cardIndex=0)
