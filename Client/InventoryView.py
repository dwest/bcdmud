import urwid

class InventoryView(urwid.WidgetWrap):
    
    def __init__(self, screen):
        self.screen = screen
        # Use a ListWalker here also
        # Get Items from player class
        (cols, rows) = screen.get_cols_rows()
        self.content = urwid.Text("Invetory goes here\nColumns: "+str(cols)
                                  +" Rows: "+str(rows))
        
        urwid.WidgetWrap.__init__(self, self.content)

    def setContent(self, content):
        (cols, rows) = self.screen.get_cols_rows()
        self.content.set_text("Invetory goes here\nColumns: "+str(cols)+" Rows: "+str(rows))
