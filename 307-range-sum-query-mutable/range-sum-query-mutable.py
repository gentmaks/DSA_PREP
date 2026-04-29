class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.nums = nums[:]
        for i, num in enumerate(nums):
            self._add(i, num)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def _add(self, index: int, val: int) -> None:
        index += 1
        while index <= self.n:
            self.bit[index] += val
            index += index & (-index)
        
    def query(self, index: int) -> int:
        s = 0
        while index >= 1:
            s += self.bit[index]
            index -= index & (-index)
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)