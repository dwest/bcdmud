import math
import urwid
from Window import Window

class MapView(Window):
    
    map = None
    player = None

    def __init__(self, screen, mapModel, playerModel):
        Window.__init__(self, screen)

        self.map = mapModel
        self.player = playerModel
        self.updateMap()

    def updateMap(self):
        rows = self.getRows()
        cols = self.getCols()
        # Multiplying by 2/3 because MapView takes up
        # 2/3's of the mapChatPile
        maxRow = int(rows*(2/3.0))
        maxCol = int(cols*(2/3.0))
        
        vizmap = self.map.getMap()

        (playerX, playerY) = (self.player.getX(), self.player.getY())
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


        self.content.set_text(vizmap)

    def getCols(self):
        (cols,rows) = self.screen.get_cols_rows()
        return cols

    def getRows(self):
        (cols,rows) = self.screen.get_cols_rows()
        return rows
        
    def getMaxCols(self):
        cols = self.getCols()
        return int(cols*(2/3.0))

    def getMaxRows(self):
        rows = self.getRows()
        return int(rows*(2/3.0))

    def setContent(self, content):
        self.content.set_text(content)
