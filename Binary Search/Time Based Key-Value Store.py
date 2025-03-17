class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        if not arr:
            return ""
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] > timestamp:
                r = mid - 1
            elif arr[mid][0] < timestamp:
                l = mid + 1
            else:
                return arr[mid][1]
        
        return arr[r][1] if arr[r][0] <= timestamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)