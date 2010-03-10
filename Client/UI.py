import urwid     
from urwid import raw_display                                              
from GamePanel import *

class UI:

    gameplayCol = None
    itemCol = None
    gamePanel  = None
    chatPanel  = None
    equipPanel = None
    invenPanel = None

    def __init__(self):
        self.gamePanel = GamePanel()
        self.chatPanel = urwid.Text("Chat Panel")
        self.equipPanel = urwid.Text("Equipment Panel")
        self.invenPanel = urwid.Text("Inventory Panel")

        fill = urwid.Filler(self.gamePanel, 'top')
        fill2 = urwid.Filler(self.chatPanel, 'top')
        fill3 = urwid.Filler(self.equipPanel, 'top')
        fill4 = urwid.Filler(self.invenPanel, 'top')
        pile = urwid.Pile([('weight', 4, fill), fill2])
        pile2 = urwid.Pile([fill3, fill4])
        
        self.gameplayCol = urwid.Columns([('weight', 4, pile), pile2])

    def getGamePlayCol(self):
        return self.gameplayCol
