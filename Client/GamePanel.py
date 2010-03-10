import urwid

class GamePanel(urwid.FlowWidget):

    content = " "

    def __init__(self, content=" "):
        if not content or not content == "":
            self.content = content

    def setContent(self, content=" "):
        if not content or not content == "":
            self.content = content

    def selectable(self):
        return False
    
    def rows(self, size, focus=False):
        w = self.display_widget(size, focus)
        return w.rows(size, focus)

    def render(self, size, focus=False):
        w = self.display_widget(size, focus)
        return w.render(size, focus)

    def display_widget(self, size, focus):
        (maxcol,) = size
        padding = maxcol/ len(self.content)
        return urwid.Text(self.content)
