import socket
import json
from Item import Item
from Inventory import Inventory

class Proxy:

    socket = None

    def __init__(self, host, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        except socket.error, msg:
#            print "Exception thrown trying to connect to server "
            print msg
#        self.player = self.getPlayer()

    def getX(self):
        return 37

    def getY(self):
        return 45

    def getInventory(self):
        return Inventory([Item('sword'), Item('lazers')])

    def moveNorth(self):
        self.sendMessage('move', 'UP')

    def moveSouth(self):
        self.sendMessage('move', 'DOWN')

    def moveEast(self):
        self.sendMessage('move', 'RIGHT')

    def moveWest(self):
        self.sendMessage('move', 'LEFT')

    def sendMessage(self, key, value):
        message = json.dumps({key:value})+"\n"
        self.socket.send(message)
