unseen = -1
from Tile import *

class Map:
    level = []
    height = 0
    width = 0

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
    actualMap = []

    def __init__(self, height, width):
        self.actualMap = actualMap
        Map.__init__(self, [height * [unseen] for count in range(0, width)])

    def updateMap(self, x, y, sightLine, actualMap):
        startX = x - sightLine
        startY = y - sightLine
        endX = x + sightLine
        endY = y + sightLine
        if(startX < 0):
            startX = 0
        if(startY < 0):
            startY = 0
        if(endX >= self.width):
            endX = self.width - 1
        if(endY >= self.height):
            endY = self.height - 1

        # I want to change this later to be more efficient and actually work
        self.level = [self.height * [unseen] for count in range(0, self.width)]
        for y in range(startY, endY + 1):
            for x in range(startX, endX + 1):
                self.level[y][x] = actualMap[y][x].getTopObject()

class RememberedMap(Map):

    def __init__(self, height, width):
        Map.__init__(self, [height * [unseen] for count in range(0, width)])

    def updateMap(self, visMap): # later change to more efficient
        for y in range(0, self.height):
            for x in range(0, self.width):
                if(visMap[y][x] != unseen):
                    self.level[y][x] = visMap[y][x]
