class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                res += nums[i-1] - nums[i]
        return res
