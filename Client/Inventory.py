from collections import MutableSet

class Inventory(MutableSet):

    def __init__(self, iterable):
        self.elements = []
        for value in iterable:
            self.elements.append(value)
            
    def __iter__(self):
        return iter(self.elements)
    
    def __contains__(self, key):
        return key in self.elements

    def __len__(self):
        return len(self.elements)
    
    def add(self, key):
        if isinstance(key, Item) and key not in self.elements:
            self.elements.append(key)
            return true
        else:
            return false
        
    def discard(self, key):
        if key in self.elements:
            self.elements.remove(key)
            return true
        else:
            return false
    
