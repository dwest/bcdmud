class Player:
    
    __x = None
    __y = None
    __inventory = None
    
    def __init__(self, proxy):
        self.proxy = proxy
        self.initPlayer()
        
    def initPlayer(self):
        # (self.__x, self.__y) = self.proxy.getPosition()
        #self.__x = self.proxy.getX()
        #self.__y = self.proxy.getY()
        #self.__inventory = self.proxy.getInventory()
        
        # TODO: (x, y) will be retrieved from server
        self.__x = 3
        self.__y = 4
        # TODO: this should contain 'Items' (class)
        self.__inventory = ['sword', 'wand']

    def moveNorth(self):
        # TODO: continue here
        pass 

    def getX(self):
        return self.__x

    def getY(self):
        return self.__Y

    def getInventory(self):
        return self.__inventory
    
    def getItemByName(self, name):
        return a.[a.index(name)]
    
