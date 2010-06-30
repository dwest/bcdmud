from Proxy import Proxy

class Map:
    
    player = None
    
    def __init__(self, player):
        self.player = player
        
    def getMap(self):
        # this should be interacting with proxy !!
        f = open('map.txt')
        vizmap = f.readlines()
        return vizmap

