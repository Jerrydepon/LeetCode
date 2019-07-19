import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.li = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        
        self.dic[val] = len(self.li)
        self.li.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        
        idx = self.dic[val]
        last = len(self.li) - 1
        self.li[idx], self.li[last] = self.li[last], self.li[idx]
        self.dic[self.li[idx]] = idx
        self.li.pop()
        self.dic.pop(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.li[random.randint(0, len(self.li)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()