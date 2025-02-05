# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.RandomizedSet =[]
        self.dict={}
    def insert(self, val: int) -> bool:
        if val in self.RandomizedSet :
            return False
        else:
            self.dict[val]=len(self.RandomizedSet)
            self.RandomizedSet.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.dict:
            self.dict[self.RandomizedSet[-1]]=self.dict[val]
            self.RandomizedSet[-1],self.RandomizedSet[self.dict[val]]=self.RandomizedSet[self.dict[val]],self.RandomizedSet[-1]
            del self.dict[val]
            self.RandomizedSet.pop()
            return True
        else:
            return False
    def getRandom(self) -> int:
        random_i=randint(0,len(self.RandomizedSet)-1)
        return self.RandomizedSet[random_i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()