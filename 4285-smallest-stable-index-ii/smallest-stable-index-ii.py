class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx = []
        mn = []
        for num in nums:
            if not mx:
                mx.append(num)
                continue
            mx.append(max(mx[-1], num))
        for num in reversed(nums):
            if not mn:
                mn.append(num)
                continue
            mn.append(min(mn[-1], num))
        mn = mn[::-1]
        for i in range(len(nums)):
            if mx[i] - mn[i] <= k:
                return i
        return -1