from Proxy import Proxy

class Map:
    
    player = None
    
    def __init__(self, player):
        self.player = player
        
    def getFittedMap(self, maxRow, maxCol):

        (playerX, playerY) = (self.player.getX(), self.player.getY())
        f = open('map.txt')
        vizmap = f.readlines()
        vizmap[playerY] = vizmap[playerY][:playerX] + "@" + vizmap[playerY][playerX+1:]

        # These create a box that centers
        # the player in the map
        topY = playerY-(maxRow/2)
        bottomY = playerY+(maxRow/2)
        leftX = playerX-(maxCol/2)
        rightX = playerX+(maxCol/2)
        # slicing with negative number doesn't work
        if topY < 0:
            topY = 0
        if leftX < 0:
            leftX = 0

        # trim off rows
        vizmap = vizmap[topY:bottomY]        
        # trim off columns
        for i in range(0,len(vizmap)):
            vizmap[i] = vizmap[i].strip()[leftX:rightX-2]+"\n"
        
        return vizmap
