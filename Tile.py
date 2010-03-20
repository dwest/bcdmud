class Tile:
    passable
    visibility
    material

    def __init__(self, passable, visibility, material):
        self.passable = passable
        self.visibility = visibility
        self.material = material

    def setPassable(passable):
        self.passable = passable
        
    def setVisibility(visibility):
        self.visibility = visibility

    def setMaterial(material):
        self.material = material

    def getPassable():
        return self.passable

    def getVisibility():
        return self.visibility

    def getMaterial():
        return self.Material
