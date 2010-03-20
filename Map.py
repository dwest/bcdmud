class Map:
    level
    height
    width

    def __init__(self, level):
        self.level = level
        self.height = len(self.level)
        self.width = len(self.level[0])

    def setMap(self, level):
        self.level = level
        self.height = len(self.level)
        self.width = len(self.level[0])

    def setTile(self, x, y, tile):
        self.level[y][x] = tile

    def getMap(self):
        return self.level

    def getTile(self, x, y):
        return self.level[y][x];

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

class VisibleMap(Map):
    pass

class Remembered(Map):
    pass
