import urwid
from UI import *
from Proxy import *

class Client:
    
    ui = UI()
    proxy = None
    
    def __init__(self, host, port):
        self.proxy = Proxy(host, port)

    def start(self):
        loop = urwid.MainLoop(self.ui.getGamePlayCol(),
                              unhandled_input=self.unhandled_input)
        loop.run()

    def unhandled_input(self, input):
        self.proxy.handleInput(input)
