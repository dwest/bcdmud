import urwid
from Window import Window

class InventoryView(Window):
    
    player = None
    
    def __init__(self, screen, player):
        # Use a ListWalker here also
        # Get Items from player class
        Window.__init__(self, screen)
        self.player = player

    def setContent(self, content):
        (cols, rows) = self.screen.get_cols_rows()
        self.content.set_text("Invetory goes here\nColumns: "+str(cols)+" Rows: "+str(rows))

    
