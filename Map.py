class Map:
    map
    height
    width

    def __init__(self, newMap):
        self.map = newMap
        height = len(self.map)
        width = len(self.map[0])

    def setMap(self, newMap):
        self.map = newMap
        self.height = len(self.map)
        self.width = len(self.map[0])

    def setTile(self, x, y, tile):
        self.map[y][x] = tile

    def getMap(self):
        return self.map

    def getTile(self, x, y):
        return map[y][x];

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width
