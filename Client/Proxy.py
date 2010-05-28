import socket
import json

class Proxy:

    socket = None

    def __init__(self, host, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        except socket.error, msg:
            print "Exception thrown trying to connect to server "
            print msg
#        self.player = self.getPlayer()

    def getMap(self, maxRow, maxCol):
        """ This is just for testing now
        Should be accessing server here"""

        (playerX, playerY) = (45,37)
        f = open('map.txt')
        vizmap = f.readlines()
        vizmap[playerY] = vizmap[playerY][:playerX] + "@" + vizmap[playerY][playerX+1:]

        # These create a box that centers
        # the player in the map
        topY = playerY-(maxRow/2)
        bottomY = playerY+(maxRow/2)
        leftX = playerX-(maxCol/2)
        rightX = playerX+(maxCol/2)
        # slicing with negative number doesn't work
        if topY < 0:
            topY = 0
        if leftX < 0:
            leftX = 0

        # trim off rows
        vizmap = vizmap[topY:bottomY]        
        # trim off columns
        for i in range(0,len(vizmap)):
            vizmap[i] = vizmap[i].strip()[leftX:rightX-2]+"\n"
        
        return vizmap


        
