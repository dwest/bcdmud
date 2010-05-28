import math
import urwid

class MapView(urwid.WidgetWrap):

    def __init__(self, screen, proxy):
        self.proxy = proxy
        self.screen = screen
        self.content = urwid.Text("")
        self.updateMap()
        urwid.WidgetWrap.__init__(self, self.content)

    def updateMap(self):
        text = ""
        (cols, rows) = self.screen.get_cols_rows()
        # Multiplying by 2/3 because MapView takes up
        # 2/3's of the mapChatPile
        maxRow = int(rows*(2/3.0))
        maxCol = int(cols*(2/3.0))
        vizMap = self.proxy.getMap(maxRow, maxCol)
        self.content.set_text(vizMap)
