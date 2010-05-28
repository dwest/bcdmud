import urwid
import sys
from Proxy import *
from MainView import *

proxy = Proxy('localhost',12345)
scr = urwid.raw_display.Screen()
m = MainView(scr, proxy)
fill = urwid.Filler(m, 'top')

def handle(input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    m.mapView.updateMap()
    m.chatView.setContent("chat lolz")
    m.inventoryView.setContent("")

loop = urwid.MainLoop(fill, unhandled_input=handle)
loop.run()

