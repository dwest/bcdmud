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
        
#        self.x = self.proxy.getX()
#        self.y = self.proxy.getY()
        self.x = 1
        self.y = 1

        self.inventory = self.proxy.getInventory()

    def canMove(self):
        # TODO: Do tests for handicaps here
        return True
    
    def moveNorth(self):
        #self.proxy.moveNorth()
        self.y -= 1

    def moveSouth(self):
#        self.proxy.moveSouth()
        self.y += 1

    def moveEast(self):
#        self.proxy.moveEast()
        self.x += 1

    def moveWest(self):
#        self.proxy.moveWest()
        self.x -= 1

####################################################
# These moveFast functions are really just for 
# testing. Unless, Daniel, you want to have some
# type of haste ability. BTW they are capital W,A,S,D
    def moveNorthFast(self):
        if self.canMove and self.canMoveNorth:
            self.y -= 2
    def moveSouthFast(self):
        if self.canMove and self.canMoveSouth:
            self.y += 2
    def moveEastFast(self):
        if self.canMove and self.canMoveEast:
            self.x += 2
    def moveWestFast(self):
        if self.canMove and self.canMoveWest:
            self.x -= 2
####################################################

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
    
