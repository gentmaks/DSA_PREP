class TimeMap:

    def __init__(self):
        self.kv_store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.kv_store[key]) - 1
        candidate = ""
        while l <= r:
            mid = (l + r) // 2
            if self.kv_store[key][mid][1] <= timestamp:
                candidate = self.kv_store[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return candidate
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)