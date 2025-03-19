class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.arr = []
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.hmap[val] = self.len
        self.len += 1
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        i = self.hmap[val]
        del self.hmap[val]
        self.hmap[self.arr[-1]], self.arr[-1], self.arr[i] = i, self.arr[i], self.arr[-1]
        self.arr.pop()
        self.len -= 1
        return True

    def getRandom(self) -> int:
        i = random.randint(0, self.len - 1)
        return self.arr[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()