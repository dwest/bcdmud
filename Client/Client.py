from Proxy import Proxy
from Map import Map
from Player import Player
# import chat view
from MainView import MainView
from MapView import MapView
from ChatView import ChatView
from InventoryView import InventoryView

import urwid

class Client:
    
    proxy = None
    screen = None
    mainView = None
    mapModel = None
    playerModel = None

    def __init__(self, proxy, screen):
        self.proxy = proxy
        self.screen = screen


        self.playerModel = Player(self.proxy)
        self.playerModel.initPlayer()
        self.mapModel = Map(self.playerModel)
        # create chat model
        
        chatView = ChatView(self.screen)
        mapView = MapView(self.screen, self.mapModel)
        inventoryView = InventoryView(self.screen, self.playerModel)
        
        viewTuple = (chatView, mapView, inventoryView)
        self.mainView = MainView(viewTuple)

    def getMainView(self):
        return self.mainView

###################
# Main
###################    
proxy = Proxy('localhost',12345)
scr = urwid.raw_display.Screen()
client = Client(proxy, scr)

m = client.getMainView()
fill = urwid.Filler(m, 'top')

def handle(input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    if input is 'w':
        client.playerModel.moveNorth()
    if input is 's':
        client.playerModel.moveSouth()
    if input is 'a':
        client.playerModel.moveWest()
    if input is 'd':
        client.playerModel.moveEast()

    m.mapView.updateMap()
    m.chatView.setContent("chat lolz")
    m.inventoryView.setContent("")
    

loop = urwid.MainLoop(fill, unhandled_input=handle)
loop.run()

