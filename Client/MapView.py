import math
import urwid
from Window import Window

class MapView(Window):
    
    mapModel = None
    
    def __init__(self, screen, mapModel):
        Window.__init__(self, screen)

        self.mapModel = mapModel
        self.updateMap()

    def updateMap(self):
        rows = self.getRows()
        cols = self.getCols()
        # Multiplying by 2/3 because MapView takes up
        # 2/3's of the mapChatPile
        maxRow = int(rows*(2/3.0))
        maxCol = int(cols*(2/3.0))
        vizMap = self.mapModel.getFittedMap(maxRow, maxCol)
        self.content.set_text(vizMap)

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
