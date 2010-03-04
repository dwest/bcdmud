from ClientMessage import *
import json
#from Game import *

class GameInstance:
    """Takes queries about game state and returns the results"""
    game = None

    def __init__(self, gameId):
        game = Game(gameId)

    def addPlayer(self):
        if self.game is not None:
            return json.dumps(self.game.addPlayer())

    def getPlayer(self, playerId):
        return json.dumps(game.playerInfo(playerId))

    def getInventory(self, playerId):
        return json.dumps(game.inventoryInfo(playerId))

    def getLevel(self, playerId):
        return json.dumps(game.levelInfo(playerId))
    
    def getVisible(self, playerId):
        return json.dumps(game.visibleInfo(playerId))

class Game:
    """Replace with db backed version ASAP"""
    playercount = 0
    players = {}
    
    level = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    items = [(15, 10, 7),
             ( 8,  5, 2),
             ( 9, 10, 3)]

    monsters = []

    def playerInfo(self, playerId):
        if playerId in self.players:
            return players[playerId]['info']

    def inventoryInfo(self, playerId):
        if playerId in self.players:
            return players[playerId]['inven']

    def levelInfo(self, playerId):
        if playerId in self.players:
            return players[playerId]['explored']

    def getVisible(self, playerId):
        if playerId in self.players:
            return players[playerId]['visible']

    def addPlayer(self):
        players["player"+self.playercount]['info'] = {"name": "Player "+playercount, "level": 1, "dlvl": 0, "xp": 42, "nlvl": 42000, "x": 7, "y", 7}
        players["player"+self.playercount]['inven'] = {[0, 1, 2, 3]}
        players["player"+self.playercount]['explored'] = self.level
        players["player"+self.playercount]['visible'] = self.level
