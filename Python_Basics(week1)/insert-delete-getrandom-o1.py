import random
class RandomizedSet:

    def __init__(self):
        self.collec = set()

    def insert(self, val: int) -> bool:
        if val in self.collec:
            return False
        else:
            self.collec.add(val)
            return True
            
        

    def remove(self, val: int) -> bool:
        if val in self.collec:
            self.collec.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.collec) >=1:
            return random.choice(tuple(self.collec))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()