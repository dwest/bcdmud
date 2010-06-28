import urwid
from Window import Window

class ChatView(Window):
    
    def __init__(self, screen, start_text = "Chat"):
        Window.__init__(self, screen, start_text)

