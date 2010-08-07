#!/usr/bin/python
from Proxy import Proxy
from Map import Map
from Player import Player
# import chat view
from MainView import MainView
from MapView import MapView
from ChatView import ChatView
from InventoryView import InventoryView

import sys
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
        mapView = MapView(self.screen, self.mapModel, self.playerModel)
        inventoryView = InventoryView(self.screen, self.playerModel)
        
        viewTuple = (chatView, mapView, inventoryView)
        self.mainView = MainView(viewTuple)

    def getMainView(self):
        return self.mainView

###################
# Main
###################    
proxy = Proxy('localhost',int(sys.argv[1]))
scr = urwid.raw_display.Screen()
client = Client(proxy, scr)

m = client.getMainView()
fill = urwid.Filler(m, 'top')

def handle(input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    elif input is 'w':
        client.playerModel.moveNorth()
    elif input is 's':
        client.playerModel.moveSouth()
    elif input is 'a':
        client.playerModel.moveWest()
    elif input is 'd':
        client.playerModel.moveEast()
    elif input is 'W':
        client.playerModel.moveNorthFast()
    elif input is 'S':
        client.playerModel.moveSouthFast()
    elif input is 'A':
        client.playerModel.moveWestFast()
    elif input is 'D':
        client.playerModel.moveEastFast()

    m.mapView.updateMap()
    m.chatView.setContent("chat lolz")
    m.inventoryView.setContent("")
    

loop = urwid.MainLoop(fill, unhandled_input=handle)
loop.run()

