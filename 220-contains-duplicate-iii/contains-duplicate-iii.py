class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        s = SortedList()
        for i, num in enumerate(nums):
            if i > indexDiff:
                s.remove(nums[i-indexDiff-1])
            pos1 = bisect_left(s, num - valueDiff)
            pos2 = bisect_right(s, num + valueDiff)
            if pos1 != pos2:
                return True
            s.add(num)
        return False
        