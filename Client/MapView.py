import math
import urwid
from Window import Window

class MapView(Window):

    def __init__(self, screen, proxy, start_text = "Map"):
        Window.__init__(self, screen, start_text)

        self.proxy = proxy
        self.updateMap()

    def updateMap(self):
        text = ""
        (cols, rows) = self.screen.get_cols_rows()
        # Multiplying by 2/3 because MapView takes up
        # 2/3's of the mapChatPile
        maxRow = int(rows*(2/3.0))
        maxCol = int(cols*(2/3.0))
        vizMap = self.proxy.getMap(maxRow, maxCol)
        self.content.set_text(vizMap)
