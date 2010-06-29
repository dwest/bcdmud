from Item import Item
from Inventory import Inventory

class Player:
    
    x = None
    y = None
    inventory = None
    
    def __init__(self, proxy):
        self.proxy = proxy
        self.initPlayer()
        
    def initPlayer(self):
        # (self.__x, self.__y) = self.proxy.getPosition()
        #self.__x = self.proxy.getX()
        #self.__y = self.proxy.getY()
        #self.__inventory = self.proxy.getInventory()
        
        self.x = self.proxy.getX()
        self.y = self.proxy.getY()

        self.inventory = self.proxy.getInventory()

    def canMove(self):
        # TODO: Do tests handicaps here
        return True
    
    def moveNorth(self):
        if self.canMove and self.canMoveNorth:
            self.y -= 1

    def moveSouth(self):
        if self.canMove and self.canMoveSouth:
            self.y += 1

    def moveEast(self):
        if self.canMove and self.canMoveEast:
            self.x += 1
    def moveWest(self):
        if self.canMove and self.canMoveWest:
            self.x -= 1

    def canMoveNorth(self):
        # Check for walls and mess
        return True

    def canMoveSouth(self):
        # Check for walls and mess
        return True

    def canMoveWest(self):
        # Check for walls and mess
        return True

    def canMoveEast(self):
        # Check for walls and mess
        return True
                        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getInventory(self):
        return self.inventory
    
    def getItemByName(self, name):
        return a[a.index(name)]
    
