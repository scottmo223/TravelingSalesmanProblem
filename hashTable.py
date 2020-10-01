# Robert S Morales 000954923
# This is the hash table

class HashTable():
    """A Custom hash table."""

    def __init__(self, length=1000):
        self.array = [None] * length

    def addItem(self, key, data):
        index = self.getIndex(key)
        if self.array[index] is None:
            self.array[index] = []
        self.array[index].append([key, data])        

    def getItem(self, key):
        index = self.getIndex(key)
        if self.array[index] is None:
            return print('no worky')
        for i in self.array[index]:
            if i[0] == key:
                return i

    #indexing an int just gives the int - should pass it in as a string.
    def getIndex(self, key): 
        index = hash(str(key)) % len(self.array)
        return index