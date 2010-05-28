import urwid

class ChatView(urwid.WidgetWrap):
    
    def __init__(self, screen):
        self.screen = screen
        # TODO: Change this to ListWalker
        self.content = urwid.Text("chat lolz")

        urwid.WidgetWrap.__init__(self, self.content)

    def setContent(self, content):
        self.content.set_text(content)
