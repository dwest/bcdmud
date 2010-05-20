class Tile:
    passable = 0
    visibility = 0
    stack = []

    def __init__(self, passable, visibility, base):
        self.passable = passable
        self.visibility = visibility
        self.stack.append(base)

    def setPassable(self, passable):
        self.passable = passable
        
    def setVisibility(self, visibility):
        self.visibility = visibility

    def getObjectStack(self):
        return self.stack

    def addObject(self, obj):
        self.stack.append(obj)

    def removeObject(self, obj):
        self.stack.remove(obj)

    def getTopObject(self):
        return self.stack[-1:]

    def getPassable(self):
        return self.passable

    def getVisibility(self):
        return self.visibility
