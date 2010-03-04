from sqlobject import *

class Game(SQLObject):
    """Big ball of game state, stored in the db"""

    #SQL stored fields
    gameName = StringCol()
    players = MultipleJoin('Player')

    def run():
        pass

    def getPlayerState(player):
        pass

    def load(gameId):
        pass
