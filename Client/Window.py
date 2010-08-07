import urwid

class Window(urwid.WidgetWrap):
    
    def __init__(self, screen):
        self.screen = screen
        # Internal widget is set to Text widget by default
        self.content = urwid.Text("")

        urwid.WidgetWrap.__init__(self, self.content)
        
    def setContent(self, content):
        self.content.set_text(content)
